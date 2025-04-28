from django.contrib import admin

from .models import Application, Review


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('parent_name', 'created_at',)
    list_filter = ('child_age', 'created_at')
    search_fields = ('parent_name', 'message')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'is_published')
    list_filter = ('is_published', 'created_at')
    search_fields = ('name', 'text')
    list_editable = ('is_published',)
