from django import forms
from app.models import *
class SchoolForms(forms.ModelForm):
    class Meta:
        model=School
        fields='__all__'
class collegeForms(forms.ModelForm):
    class Meta:
        model=college
        fields='__all__'

