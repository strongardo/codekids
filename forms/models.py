from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator


class Application(models.Model):
    min_age_validator = MinValueValidator(7, message="Минимальный возраст — 7 лет.")
    max_age_validator = MaxValueValidator(17, message="Максимальный возраст — 17 лет.")
    phone_validator = RegexValidator(
        regex=r'^\+?\d{10,15}$',
        message="Введите корректный номер телефона: только цифры, опциональный '+' в начале, всего от 10 до 15 цифр."
    )

    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    parent_name = models.CharField("Имя родителя", max_length=50)
    child_age = models.PositiveIntegerField("Возраст ребенка",
                                            validators=[min_age_validator, max_age_validator])
    phone = models.CharField("Номер телефона", max_length=20, validators=[phone_validator])
    email = models.EmailField("Email", blank=True, null=True)
    message = models.TextField("Сообщение", max_length=500, blank=True, null=True)

    is_processed = models.BooleanField("Обработано", default=False)
    note = models.TextField("Заметки", max_length=700, blank=True, null=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ['-created_at']

    def __str__(self):
        return f"Заявка от {self.parent_name}"


class Review(models.Model):
    name = models.CharField("Имя", max_length=50)
    text = models.TextField("Текст отзыва", max_length=500)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    is_published = models.BooleanField("Опубликовать на сайте", default=False)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_at']

    def __str__(self):
        return f"Отзыв от {self.name}"
