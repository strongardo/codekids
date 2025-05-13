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

        parent_name_raw = cleaned_data.get('parent_name')
        child_age_raw = cleaned_data.get('child_age')
        phone_raw = cleaned_data.get('phone')

        parent_name = parent_name_raw.strip().lower() if parent_name_raw else ''
        child_age = str(child_age_raw).strip() if child_age_raw is not None else ''
        phone = phone_raw.strip() if phone_raw else ''

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

    def clean(self):
        cleaned_data = super().clean()

        honey = cleaned_data.get('user_notes')
        if honey:
            raise forms.ValidationError("Проверка на бота не пройдена.")

        name_raw = cleaned_data.get('name')
        text_raw = cleaned_data.get('text')

        name = name_raw.strip().lower() if name_raw else ''
        text = text_raw.strip().lower() if text_raw else ''

        today = timezone.now().date()

        if name and text:
            if Review.objects.filter(
                    created_at__date=today,
                    name=name,
                    text=text
            ).exists():
                raise forms.ValidationError(
                    "Такой отзыв уже был отправлен сегодня."
                )

        return cleaned_data
