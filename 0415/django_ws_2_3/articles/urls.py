from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('send/', views.send, name = 'send'),
    path('recieve/', views.catch, name='catch'),
]