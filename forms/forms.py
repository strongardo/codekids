from django import forms
from django.utils import timezone

from .models import *


class ApplicationForm(forms.ModelForm):
    user_notes = forms.CharField(required=False)  # Защита от ботов

    class Meta:
        model = Application
        fields = ['parent_name', 'child_age', 'phone', 'email', 'message']

    def clean(self):
        cleaned_data = super().clean()

        honey = cleaned_data.get('user_notes')
        if honey:
            raise forms.ValidationError("Проверка на бота не пройдена.")

        parent_name = cleaned_data.get('parent_name')
        child_age = cleaned_data.get('child_age')
        phone = cleaned_data.get('phone')

        today = timezone.now().date()

        if parent_name and child_age is not None and phone:
            if Application.objects.filter(
                    created_at__date=today,
                    parent_name=parent_name,
                    child_age=child_age,
                    phone=phone
            ).exists():  # Если такая есть (проверяем только совпадение)
                raise forms.ValidationError(
                    "Вы уже отправляли заявку с такими данными сегодня. Пожалуйста, проверьте информацию."
                )

        return cleaned_data


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'text']
