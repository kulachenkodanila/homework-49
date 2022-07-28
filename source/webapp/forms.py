from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Work, Project


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ["summary", "description", "status", "types", "project"]
        widgets = {
            "types": widgets.CheckboxSelectMultiple
        }

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) > 100:
            raise ValidationError("Длина описания должна быть меньше 100 символов")
        return description

    def clean_summary(self):
        summary = self.cleaned_data.get('description')
        if len(summary) > 100:
            raise ValidationError("Длина заголовка должна быть меньше 100 символов")
        return summary


class UserWorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ["summary", "description", "status", "types"]


class UserProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description_project", "finish_date"]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description_project"]

    def clean_description_project(self):
        description_project = self.cleaned_data.get('description_project')
        if len(description_project) > 150:
            raise ValidationError("Длина описания должна быть меньше 100 символов")
        return description_project

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) > 100:
            raise ValidationError("Длина наименования должна быть меньше 50 символов")
        return name


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='Найти')
