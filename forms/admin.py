from django.contrib import admin

from .models import Application, Review


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('parent_name', 'created_at', 'is_processed',)
    list_filter = ('created_at', 'is_processed')
    search_fields = ('parent_name', 'message')
    ordering = ('is_processed', '-created_at')

    # Все поля кроме email и phone сделать readonly
    readonly_fields = [
        field.name for field in Application._meta.fields
        if field.name not in ('id', 'is_processed', 'note')
    ]

    def has_add_permission(self, request):
        return False  # запретить добавление через админку

    # def has_change_permission(self, request, obj=None):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return request.user.is_superuser


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'is_published')
    list_filter = ('is_published', 'created_at')
    search_fields = ('name', 'text')
    list_editable = ('is_published',)
