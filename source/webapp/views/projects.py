
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from django.shortcuts import render
from django.utils.http import urlencode

from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from webapp.forms import WorkForm, SearchForm
from webapp.models import Work, Project


class IndexView(ListView):
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


