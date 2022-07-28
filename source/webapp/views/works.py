from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from django.shortcuts import render
from django.urls import reverse
from django.utils.http import urlencode

from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from webapp.forms import WorkForm, SearchForm, UserWorkForm
from webapp.models import Work, Project


class WorkView(DetailView):
    template_name = "works/work_view.html"
    model = Work

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.object.project
        return context


class UpdateWork(UpdateView):
    form_class = WorkForm
    template_name = "works/update.html"
    model = Work

    def get_form_class(self):
        if self.request.GET.get("is_admin"):
            return WorkForm
        return UserWorkForm

    def get_success_url(self):
        return reverse("work_view", kwargs={"pk": self.object.pk})

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
