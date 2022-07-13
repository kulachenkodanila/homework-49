from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Work


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ["summary", "description", "status", "types"]
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


