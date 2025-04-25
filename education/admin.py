from django.contrib import admin
from .models import Course, Teacher


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title',)  # запятая обязательна
    search_fields = ('title',)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialization', 'email', 'start_date',)
    search_fields = ('first_name', 'last_name',)


admin.site.register(Course, CourseAdmin)
admin.site.register(Teacher, TeacherAdmin)

