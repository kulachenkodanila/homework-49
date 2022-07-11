from django.shortcuts import render, redirect, get_object_or_404

from django.shortcuts import render

from django.views import View

from webapp.models import Work


class IndexView(View):
    def get(self, request, *args, **kwargs):
        workes = Work.objects.order_by("-updated_at")
        context = {"workes": workes}
        return render(request, "index.html", context)
