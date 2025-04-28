from django.db import models


class Application(models.Model):
    parent_name = models.CharField("Имя родителя", max_length=50)
    child_age = models.PositiveIntegerField("Возраст ребенка")
    phone = models.CharField("Номер телефона", max_length=20)
    email = models.EmailField("Email", blank=True, null=True)
    message = models.TextField("Сообщение", max_length=500)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

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