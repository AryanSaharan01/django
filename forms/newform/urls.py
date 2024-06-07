from django.urls import path
from . import views

urlpatterns = [
    path('', views.newform, name='newform')
]