from django.urls import path
from .views import emi_calculator

urlpatterns = [
    path('', emi_calculator, name='emi_calculator'),
]
