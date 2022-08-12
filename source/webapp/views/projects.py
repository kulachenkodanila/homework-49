from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.http import request
from django.shortcuts import redirect, get_object_or_404

from django.urls import reverse
from django.utils.http import urlencode

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import SearchForm, ProjectForm, UserProjectForm
from webapp.models import Project


class IndexView_project(ListView):
    model = Project
    template_name = "projects/project_list.html"
    context_object_name = "projects"
    ordering = "name"
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        if self.search_value:
            return Project.objects.filter(Q(name__icontains=self.search_value))
        return Project.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["form"] = self.form
        if self.search_value:
            query = urlencode({'search': self.search_value})
            context['query'] = query
            context['search'] = self.search_value
        return context

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get("search")


class ProjectView(DetailView):
    template_name = "projects/project_view.html"
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.object.tasks
        return context


class UpdateProject(PermissionRequiredMixin, UpdateView):
    form_class = ProjectForm
    template_name = "projects/project_update.html"
    model = Project


    def get_form_class(self):
        if self.request.GET.get("is_admin"):
            return ProjectForm
        return UserProjectForm

    def get_success_url(self):
        return reverse("webapp:project_view", kwargs={"pk": self.object.pk})


class DeleteProject(DeleteView):
    model = Project

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("webapp:index")


class CreateProject(LoginRequiredMixin , CreateView):
    form_class = ProjectForm
    template_name = "projects/project_create.html"


    def get_success_url(self):
        return reverse("webapp:project_view", kwargs={"pk": self.object.pk})

