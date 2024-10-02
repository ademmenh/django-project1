from django.urls import path
from . import views

urlpatterns = [
    path('form3/', views.form3),
    path('form300/', views.form300),
    path('home/', views.home),

]
