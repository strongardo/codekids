from django.db import models


class Feature(models.Model):
    FEATURE_ICONS = [
        ('rocket', 'Скорость 🚀 (rocket)'),
        ('lightbulb', 'Идеи и творчество 💡 (lightbulb)'),
        ('trophy', 'Достижения и награды 🏆 (trophy)'),
        ('star', 'Отличные результаты ⭐ (star)'),
        ('heart', 'Любовь к обучению ❤️ (heart)'),
        ('thumbs-up', 'Уверенность 👍 (thumbs-up)'),
        ('bolt', 'Энергия и мотивация ⚡ (bolt)'),
        ('award', 'Признание 🥇 (award)'),
        ('shield-alt', 'Безопасность 🛡️ (shield-alt)'),
        ('play', 'Игровой подход 🎮 (play)'),
        ('upload', 'Рост навыков ⬆️ (upload)'),
        ('check', 'Гарантия качества ✔️ (check)'),
        ('book', 'База знаний 📚 (book)'),
        ('code', 'Программирование 👨‍💻 (code)'),
        ('brain', 'Развитие мышления 🧠 (brain)'),
        ('puzzle-piece', 'Решение задач 🧩 (puzzle-piece)'),
        ('users', 'Дружное сообщество 👥 (users)'),
        ('chalkboard-teacher', 'Опытные наставники 👩‍🏫 (chalkboard-teacher)'),
    ]

    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=100, verbose_name='Описание')
    icon = models.CharField(max_length=20, choices=FEATURE_ICONS, verbose_name='Иконка')

    class Meta:
        verbose_name = "преимущество"
        verbose_name_plural = "Преимущества"

    def __str__(self):
        return self.title


class Hero(models.Model):
    top_text = models.CharField(max_length=100, verbose_name='Верхняя часть основного текста', default='')
    bottom_text = models.CharField(max_length=100, verbose_name='Нижняя часть основного текста', default='')
    description = models.CharField(max_length=200, verbose_name='Описание')

    class Meta:
        verbose_name = "Hero-блок"
        verbose_name_plural = "Hero-блок"

    def __str__(self):
        return "Настройки Hero-блока"


from django.db import models


class About(models.Model):
    about_text = models.TextField(verbose_name='О компании')
    mission_text = models.TextField(verbose_name='Наша миссия')

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

    def __str__(self):
        return "Тексты страницы 'О нас'"


class ThankYouText(models.Model):
    type = models.CharField(max_length=50, choices=[
        ('application', 'Заявка'),
        ('review', 'Отзыв'),
    ], verbose_name='Тип страницы', unique=True)

    title = models.CharField(max_length=50, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст благодарности')

    class Meta:
        verbose_name = "Текст благодарности"
        verbose_name_plural = "Тексты благодарностей"

    def __str__(self):
        return f"Текст для {self.get_type_display()}"


class ContactInfo(models.Model):
    phone = models.CharField("Номер телефона", max_length=20, blank=True)
    email = models.EmailField("Email", blank=True)
    whatsapp_number = models.CharField("Номер Whatsapp", max_length=20, blank=True, null=True)
    telegram_login = models.CharField("Логин Telegram(без @)", max_length=50, blank=True, null=True)

    instagram_link = models.URLField("Ссылка на Instagram", blank=True)
    vk_link = models.URLField("Ссылка на VK", blank=True)
    youtube_link = models.URLField("Ссылка на YouTube", blank=True)

    address = models.CharField("Адрес", max_length=255, blank=True)
    latitude = models.DecimalField("Широта (latitude)", max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField("Долгота (longitude)", max_digits=9, decimal_places=6, blank=True, null=True)

    class Meta:
        verbose_name = "Контактная информация"
        verbose_name_plural = "Контактная информация"

    def __str__(self):
        return "Контакты"
