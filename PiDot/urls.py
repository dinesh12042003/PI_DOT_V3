from django.urls import path, include
from .views import *

urlpatterns = [
    path('about/', about, name='PiDot_about'),
    path('careers/', careers, name='PiDot_careers'),
    path('leadership/', leadership, name='PiDot_leadership'),
    path('newsroom/', newsroom, name='PiDot_newsroom'),
    path('careers_register/', careers_register, name='PiDot_careers_register'),
]