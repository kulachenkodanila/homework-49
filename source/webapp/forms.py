from django import forms
from django.forms import widgets

from webapp.models import Work


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ["summary", "description", "status", "types"]
        widgets = {
            "types": widgets.CheckboxSelectMultiple
        }
