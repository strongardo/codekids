from django.contrib import admin
from .models import Feature, Hero, About, ThankYouText


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title',)  # запятая обязательна
    search_fields = ('title',)

    def has_add_permission(self, request):
        # Разрешить добавление, если количество объектов Feature меньше 3
        return Feature.objects.count() < 3


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Разрешить добавление только если нет ни одного Hero
        return not Hero.objects.exists()


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not About.objects.exists()


@admin.register(ThankYouText)
class ThankYouTextAdmin(admin.ModelAdmin):
    list_display = ('type',)  # запятая обязательна
