from django.urls import path, include
from .views import *

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('cookie_policy/', cookie_policy, name='cookie_policy'),
    path('privacy_policy/', privacy_policy, name='privacy_policy'),
    path('terms_coditions/', terms_coditions, name='terms_coditions'),
]