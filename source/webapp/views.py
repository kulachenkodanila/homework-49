from django.shortcuts import render, redirect, get_object_or_404

from django.shortcuts import render

from django.views import View
from django.views.generic import TemplateView

from webapp.models import Work


class IndexView(View):
    def get(self, request, *args, **kwargs):
        workes = Work.objects.order_by("-updated_at")
        context = {"workes": workes}
        return render(request, "index.html", context)


class WorkView(TemplateView):
    template_name = "work_view.html"

    def get_context_data(self, **kwargs):
        pk = kwargs.get("pk")
        work = get_object_or_404(Work, pk=pk)
        kwargs["work"] = work
        return super().get_context_data(**kwargs)
