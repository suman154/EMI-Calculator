from django.urls import path
from .views import emi_calculator

urlpatterns = [
    path('emi-calculator/', emi_calculator, name='emi_calculator'),
]
