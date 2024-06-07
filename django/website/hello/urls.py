from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    # path('<str:name>', views.greet, name='greet'),
    path('<str:name>', views.greet_html, name='greet_html')
]