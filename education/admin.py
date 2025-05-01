from django.contrib import admin
from .models import *


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title',)  # запятая обязательна
    search_fields = ('title',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialization', 'email', 'start_date',)
    search_fields = ('first_name', 'last_name',)


@admin.register(Student)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'start_date',)
    search_fields = ('first_name', 'last_name',)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        'student', 'course', 'teacher',
        'next_lesson_date', 'balance_lessons', 'is_active'
    )
    list_filter = ('is_active', 'course', 'teacher')
    search_fields = ('student__account__username', 'course__title')

    readonly_fields = ('date_enrolled',)

    fieldsets = (
        ('Основная информация', {
            'fields': ('student', 'course', 'teacher', 'is_active')
        }),
        ('Занятия и доступ', {
            'fields': ('next_lesson_date', 'balance_lessons', 'meet_link')
        }),
        ('Домашнее задание', {
            'fields': ('last_homework',)
        }),
        ('Служебное', {
            'fields': ('date_enrolled',),
        }),
    )
