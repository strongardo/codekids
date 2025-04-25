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


class Teacher(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    photo = models.ImageField(upload_to='teachers_photos/', null=True, blank=True, verbose_name="Фото")
    bio = models.TextField(verbose_name="Описание", blank=True)
    specialization = models.CharField(max_length=200, verbose_name="Специализация", null=True, blank=True)
    courses = models.ManyToManyField('Course', related_name='teachers', verbose_name="Курсы")
    email = models.EmailField(verbose_name="Электронная почта", null=True, blank=True)
    social_links = models.JSONField(default=dict, blank=True, verbose_name="Ссылки на социальные сети")
    start_date = models.DateField(verbose_name="Дата начала работы", null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"
