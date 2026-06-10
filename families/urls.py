from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vasti-patrak/', views.family_directory, name='family_directory'),
    path('family/<int:pk>/', views.family_detail, name='family_detail'),
    path('family/<int:pk>/pdf/', views.family_pdf, name='family_pdf'),
    path('contact/', views.contact_page, name='contact'),
]
