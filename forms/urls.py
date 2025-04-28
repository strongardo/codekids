from django.urls import path
from .views import *

urlpatterns = [
    path('review_form/', review_form, name='review_form'),
]
