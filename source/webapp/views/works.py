from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode

from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import WorkForm, SearchForm, UserWorkForm, WorkDeleteForm
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


class DeleteWork(DeleteView):
    model = Work
    template_name = "works/delete.html"
    success_url = reverse_lazy('index')
    form_class = WorkDeleteForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, instance=self.get_object())
        if form.is_valid():
            return self.delete(request, *args, **kwargs)
        else:
            return self.get(request, *args, **kwargs)


