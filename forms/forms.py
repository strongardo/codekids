from django import forms
from .models import *


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['parent_name', 'child_age', 'phone', 'email', 'message']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'text']
