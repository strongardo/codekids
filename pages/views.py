from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from education.forms import EnrollmentUpdateForm
from education.models import Course, Teacher, Enrollment
from forms.forms import ApplicationForm, ReviewForm
from forms.models import Review
from info.models import Feature, Hero, About, ThankYouText, ContactInfo


def home(request):
    context = {
        'hero': Hero.objects.first(),
        'features': Feature.objects.all(),
        'courses': Course.objects.filter(is_hit=True),
        'reviews': Review.objects.all(),
    }

    if request.method == 'POST':
        submit_type = request.POST.get('submit_type')
        if submit_type == 'application_form':
            application_form = ApplicationForm(request.POST)
            if application_form.is_valid():
                application_form.save()
                return redirect('/thanks/application/')
            context['application_form'] = application_form
        elif submit_type == 'review_form':
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review_form.save()
                return redirect('/thanks/review/')
            context['review_form'] = review_form

    return render(request, 'pages/home.html', context)


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


def login_form(request):
    return render(request, 'pages/login.html')


def thanks(request, page_type):
    thank_you = get_object_or_404(ThankYouText, type=page_type)

    return render(request, 'pages/thanks.html', {
        'thank_you': thank_you,
    })


@login_required
def dashboard(request):
    context = {}

    role = get_user_role(request.user)
    context['role'] = role

    if role == 'student':
        context['student_profile'] = request.user.student
    elif role == 'teacher':
        teacher = request.user.teacher
        enrollments = teacher.enrollments.select_related('student', 'course')
        context['teacher_profile'] = teacher
        context['enrollments'] = enrollments

        if request.method == 'POST':
            enrollment_id = request.POST.get('enrollment_id')
            enrollment = get_object_or_404(Enrollment, id=enrollment_id, teacher=teacher)
            form = EnrollmentUpdateForm(request.POST, instance=enrollment)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
            else:
                for enrollment in enrollments:
                    if enrollment.id == int(enrollment_id):
                        enrollment.errors = form.errors
                context['enrollments'] = enrollments

    return render(request, 'pages/dashboard/dashboard.html', context)


def get_user_role(user):
    if hasattr(user, 'student'):
        return 'student'
    elif hasattr(user, 'teacher'):
        return 'teacher'
    else:
        return 'unknown'
