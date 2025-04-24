from django.db import models


from django.db import models

class Course(models.Model):
    class Level(models.TextChoices):
        BEGINNER = 'beginner', 'Начальный'
        INTERMEDIATE = 'intermediate', 'Средний'
        ADVANCED = 'advanced', 'Продвинутый'

    title = models.CharField(max_length=200, verbose_name="Название курса")
    description = models.TextField(verbose_name="Описание курса")
    level = models.CharField(
        max_length=20,
        choices=Level.choices,
        default=Level.BEGINNER,
        verbose_name="Уровень подготовки"
    )
    duration = models.PositiveIntegerField(verbose_name="Продолжительность (занятий)")
    min_age = models.PositiveIntegerField(verbose_name="Минимальный возраст")

    is_hit = models.BooleanField(verbose_name="Отображение курса на главной", default="False")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title


