from django import forms
from .models import Enrollment
from django.utils import timezone


class EnrollmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['next_lesson_date', 'balance_lessons', 'last_homework', 'meet_link']

    def clean_next_lesson_date(self):
        date = self.cleaned_data.get('next_lesson_date')
        if date and date < timezone.now():
            raise forms.ValidationError("Дата следующего урока не может быть в прошлом.")
        return date
