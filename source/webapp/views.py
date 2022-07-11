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

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        self.work = get_object_or_404(Work, pk=pk)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            form = WorkForm(initial={
                "summary": self.work.summary,
                "description": self.work.description,
                "status": self.work.status,
                "type": self.work.type
            })
            return render(request, "update.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = WorkForm(data=request.POST)
        if form.is_valid():
            self.work.summary = form.cleaned_data.get("summary")
            self.work.description = form.cleaned_data.get("description")
            self.work.status = form.cleaned_data.get("status")
            self.work.type = form.cleaned_data.get("type")
            self.work.save()
            return redirect("work_view", pk=self.work.pk)
        return render(request, "update.html", {"form": form})


class CreateWork(View):
    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            form = WorkForm()
            return render(request, "create.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = WorkForm(data=request.POST)
        if form.is_valid():
            summary = form.cleaned_data.get("summary")
            description = form.cleaned_data.get("description")
            status = form.cleaned_data.get("status")
            type = form.cleaned_data.get("type")
            new_work = Work.objects.create(summary=summary, description=description, status=status, type=type)
            return redirect("work_view", pk=new_work.pk)
        return render(request, "create.html", {"form": form})
