
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from django.shortcuts import render
from django.utils.http import urlencode

from django.views import View
from django.views.generic import TemplateView, ListView

from webapp.forms import WorkForm, SearchForm
from webapp.models import Work



class IndexView(ListView):
    model = Work
    template_name = "works/index.html"
    context_object_name = "workes"
    ordering = "-updated_at"
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        if self.search_value:
            return Work.objects.filter(Q(summary__icontains=self.search_value))
        return Work.objects.all()

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


class WorkView(TemplateView):
    template_name = "works/work_view.html"

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


class CreateWork(View):
    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            form = WorkForm()
            return render(request, "works/create.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = WorkForm(data=request.POST)
        if form.is_valid():
            summary = form.cleaned_data.get("summary")
            description = form.cleaned_data.get("description")
            status = form.cleaned_data.get("status")
            types = form.cleaned_data.get("types")
            new_work = Work.objects.create(summary=summary, description=description, status=status)
            new_work.types.set(types)
            return redirect("work_view", pk=new_work.pk)
        return render(request, "works/create.html", {"form": form})


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
