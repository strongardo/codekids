from django.shortcuts import render, get_object_or_404
from education.models import Course, Teacher
from info.models import Feature, Hero, About, ThankYouText, ContactInfo


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
    contact_info = ContactInfo.objects.all().first()
    print(contact_info.phone)
    return render(request, 'pages/contacts.html', {'contacts': contact_info})


def register(request):
    return render(request, 'pages/register.html')


def login(request):
    return render(request, 'pages/login.html')


def dashboard(request):
    return render(request, 'pages/dashboard.html')


def thanks(request, page_type):
    thank_you = get_object_or_404(ThankYouText, type=page_type)

    return render(request, 'pages/thanks.html', {
        'thank_you': thank_you,
    })
