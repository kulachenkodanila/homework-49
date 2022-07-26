
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from django.shortcuts import render
from django.utils.http import urlencode

from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from webapp.forms import WorkForm, SearchForm
from webapp.models import Work, Project



# class WorkView(TemplateView):
#     template_name = "works/work_view.html"
#
#     def get_context_data(self, **kwargs):
#         pk = kwargs.get("pk")
#         work = get_object_or_404(Work, pk=pk)
#         kwargs["work"] = work
#         return super().get_context_data(**kwargs)

class WorkView(DetailView):
    template_name = "works/work_view.html"
    model = Work

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['projects'] = self.object.projects.order_by("name")
    #     return context


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
                "types": self.work.types.all
            })
            return render(request, "works/update.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = WorkForm(data=request.POST)
        if form.is_valid():
            types = form.cleaned_data.pop('types')
            self.work.summary = form.cleaned_data.get("summary")
            self.work.description = form.cleaned_data.get("description")
            self.work.status = form.cleaned_data.get("status")
            self.work.types.all = form.cleaned_data.get("types")
            self.work.save()
            self.work.types.set(types)
            return redirect("work_view", pk=self.work.pk)
        return render(request, "works/update.html", {"form": form})



class CreateWork(CreateView):
    form_class = WorkForm
    template_name = "works/create.html"

    def form_valid(self, form):
        work = form.save(commit=False)
        work.save()
        form.save_m2m()
        return redirect("work_view", pk=work.pk)

class DeleteWork(View):

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        self.work = get_object_or_404(Work, pk=pk)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            return render(request, "works/delete.html", {"work": self.work})

    def post(self, request, *args, **kwargs):
        self.work.delete()
        return redirect("index")
