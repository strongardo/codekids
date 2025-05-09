from django.contrib.auth.models import User
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
    email = models.EmailField(verbose_name="Электронная почта")
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    courses = models.ManyToManyField('Course', related_name='teachers', verbose_name="Курсы")
    bio = models.TextField(verbose_name="Описание", blank=True)
    specialization = models.CharField(max_length=200, verbose_name="Специализация")
    photo = models.ImageField(upload_to='teachers_photos/', null=True, blank=True, verbose_name="Фото")
    social_links = models.JSONField(default=dict, null=True, blank=True, verbose_name="Ссылки на социальные сети")
    start_date = models.DateField(verbose_name="Дата начала работы", null=True, blank=True)
    account = models.OneToOneField(User, on_delete=models.PROTECT, null=True, blank=True, related_name='teacher')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"


class Student(models.Model):
    email = models.EmailField(verbose_name="Электронная почта")
    phone = models.CharField(verbose_name="Номер телефона", max_length=20)
    parent_name = models.CharField(max_length=100, verbose_name="Имя родителя")
    first_name = models.CharField(max_length=100, verbose_name="Имя ученика")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия ученика", null=True, blank=True)
    birthday = models.DateField(verbose_name="День рождения", null=True, blank=True)
    age = models.PositiveIntegerField(verbose_name="Возраст ученика", null=True, blank=True)
    start_date = models.DateField(verbose_name="Дата начала обучения", null=True, blank=True)
    account = models.OneToOneField(User, on_delete=models.PROTECT, null=True, blank=True, related_name='student')

    def __str__(self):
        return f"{self.first_name} ({self.email})"

    class Meta:
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments', verbose_name="Ученик")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments', verbose_name="Курс")
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, related_name='enrollments', null=True, blank=True, verbose_name="Преподаватель")

    date_enrolled = models.DateField(auto_now_add=True, verbose_name="Дата записи")
    is_active = models.BooleanField(default=True, verbose_name="Активна?")

    schedule_text = models.TextField(max_length=500, blank=True, verbose_name="Расписание")
    meet_link = models.URLField(blank=True, verbose_name="Ссылка на урок")
    balance_lessons = models.PositiveIntegerField(default=0, verbose_name="Количество уроков")
    last_homework = models.TextField(blank=True, verbose_name="Домашнее задание")

    def __str__(self):
        return f"Запись {self.student.first_name} ({self.student.email}) на {self.course.title}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

        constraints = [
            models.UniqueConstraint(fields=['student', 'course'], name='unique_student_course')
        ]

    def is_paid(self):
        return self.balance_lessons > 0
