from django import forms
from .models import formvalidation


class formvalidationForm(forms.ModelForm):
    class Meta:
        model=formvalidation
        fields= ['name','email','age','password']
