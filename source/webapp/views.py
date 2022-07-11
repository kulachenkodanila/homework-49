from django.shortcuts import render, redirect, get_object_or_404

from django.shortcuts import render

from django.views import View
from django.views.generic import TemplateView

from webapp.forms import WorkForm
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


class UpdateWork(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        work = get_object_or_404(Work, pk=pk)
        if request.method == "GET":
            form = WorkForm(initial={
                "summary": work.summary,
                "description": work.description,
                "status": work.status,
                "type": work.type
            })
            return render(request, "update.html", {"form": form})

    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        work = get_object_or_404(Work, pk=pk)
        form = WorkForm(data=request.POST)
        if form.is_valid():
            work.summary = form.cleaned_data.get("summary")
            work.description = form.cleaned_data.get("description")
            work.status = form.cleaned_data.get("status")
            work.type = form.cleaned_data.get("type")
            work.save()
            return redirect("work_view", pk=work.pk)
        return render(request, "update.html", {"form": form})
