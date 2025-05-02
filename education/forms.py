from django import forms
from .models import Enrollment


class EnrollmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['schedule_text', 'balance_lessons', 'last_homework', 'meet_link']
