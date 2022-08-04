from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect

from django.urls import reverse, reverse_lazy

from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import WorkForm, UserWorkForm, WorkDeleteForm
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
        return reverse("webapp:work_view", kwargs={"pk": self.object.pk})


class DeleteWork(DeleteView):
    model = Work
    template_name = "works/delete.html"
    success_url = reverse_lazy('webapp:index')
    form_class = WorkDeleteForm

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("webapp:project_view", kwargs={"pk": self.object.project.pk})


class CreateWork(LoginRequiredMixin, CreateView):
    form_class = WorkForm
    template_name = "works/create.html"

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get("pk"))
        form.instance.project = project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("webapp:project_view", kwargs={"pk": self.object.project.pk})

