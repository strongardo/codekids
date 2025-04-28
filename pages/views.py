from django.shortcuts import render, redirect, get_object_or_404
from education.models import Course, Teacher
from forms.forms import ApplicationForm
from info.models import Feature, Hero, About, ThankYouText, ContactInfo


def home(request):
    context = {
        'hero': Hero.objects.first(),
        'features': Feature.objects.all(),
        'courses': Course.objects.filter(is_hit=True),
    }

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/thanks/application/')
        context['form'] = form


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
