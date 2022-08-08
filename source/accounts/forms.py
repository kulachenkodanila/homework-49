from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput)
    class MyForm(forms.Form):
        first_name = forms.CharField(label='first_name', required=False)
        last_name = forms.CharField(label='last_name', required=False)

    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        if not first_name and last_name:
            raise ValidationError("Укажите имя или фамилию")
        # return self.cleaned_data


    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

