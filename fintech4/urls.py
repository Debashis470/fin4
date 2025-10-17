from django.urls import path
from .views import tax_calculator

urlpatterns = [
    path('calculate-tax/', tax_calculator, name='calculate-tax'),
]




