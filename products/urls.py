from django.urls import path, include
from .views import *

urlpatterns = [
    path('axiom/', axiom, name='product_axiom'),
    path('edusphere/', edusphere, name='product_edusphere'),
    path('genesis/', genesis, name='product_genesis'),
    path('solutions/', solutions, name='solutions_all')
]