from django.shortcuts import render
from education.models import Course, Teacher


def home(request):
    hit_courses = Course.objects.filter(is_hit=True)
    return render(request, 'pages/home.html', {
        'courses': hit_courses,
    })


def courses(request):
    all_courses = Course.objects.all()
    return render(request, 'pages/courses.html', {
        'courses': all_courses,
    })


def about(request):
    teachers = Teacher.objects.all()
    return render(request, 'pages/about.html', {
        'teachers': teachers,
    })


def contacts(request):
    return render(request, 'pages/contacts.html')


def register(request):
    return render(request, 'pages/register.html')


def login(request):
    return render(request, 'pages/login.html')


def dashboard(request):
    return render(request, 'pages/dashboard.html')


def thanks(request):
    title = 'Спасибо за вашу заявку - CodeKids'
    text = 'Мы получили вашу информацию и свяжемся с вами в ближайшее время.'
    return render(request, 'pages/thanks.html', {
        'title': title,
        'text': text,
    })
