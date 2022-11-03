from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='getRoutes'),
    path('advocates/', views.getAdvocates, name='advocates'),
    path('advocates/<str:pk>/', views.getAdvocate, name='advocate'),
    path('companies/', views.getCompanies, name='companies'),
    path('companies/<str:pk>/', views.getCompany, name='company'),
]