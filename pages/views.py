from django.shortcuts import render
from education.models import Course, Teacher
from info.models import Feature, Hero, About, ThankYouText


def home(request):
    hero = Hero.objects.first()
    hit_courses = Course.objects.filter(is_hit=True)
    features = Feature.objects.all()

    return render(request, 'pages/home.html', {
        'hero': hero,
        'features': features,
        'courses': hit_courses,
    })


def courses(request):
    all_courses = Course.objects.all()
    return render(request, 'pages/courses.html', {
        'courses': all_courses,
    })


def about(request):
    about_info = About.objects.first()
    teachers = Teacher.objects.all()
    return render(request, 'pages/about.html', {
        'teachers': teachers,
        'about_info': about_info,
    })


def contacts(request):
    return render(request, 'pages/contacts.html')


def register(request):
    return render(request, 'pages/register.html')


def login(request):
    return render(request, 'pages/login.html')


def dashboard(request):
    return render(request, 'pages/dashboard.html')


def thanks(request, page_type):
    thank_you_text = ThankYouText.objects.filter(type=page_type).first()

    title = thank_you_text.title
    text = thank_you_text.text

    if not thank_you_text:
        title = 'Спасибо!'
        text = 'Мы получили ваше сообщение'

    return render(request, 'pages/thanks.html', {
        'title': title,
        'text': text,
    })
