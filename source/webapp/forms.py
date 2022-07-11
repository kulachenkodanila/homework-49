from django import forms


from webapp.models import Type, Status


class WorkForm(forms.Form):
    summary = forms.CharField(max_length=150, required=True, label='Summary')
    description = forms.CharField(max_length=100, required=True, label='Description')
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    type = forms.ModelChoiceField(queryset=Type.objects.all())
