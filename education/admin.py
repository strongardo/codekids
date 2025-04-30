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