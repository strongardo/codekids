from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def courses(request):
    return render(request, 'pages/courses.html')

def about(request):
    return render(request, 'pages/about.html')

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