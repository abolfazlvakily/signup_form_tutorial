from django.urls import path
from . import views

urlpatterns = [
    path('ok_you_are_superuser/', views.signup, name='signup'),
    path('', views.signup, name='index'),
]
