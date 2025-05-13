from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('courses/', courses, name='courses'),
    path('about/', about, name='about'),
    path('login_form/', login_form, name='login_form'),
    path('dashboard/', dashboard, name='dashboard'),
    path('thanks/<str:page_type>/', thanks, name='thanks'),
]
