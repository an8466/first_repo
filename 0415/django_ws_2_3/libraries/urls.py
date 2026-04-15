# libraries/urls.py

from django.urls import path
from . import views

app_name = 'libraries'

urlpatterns = [
    # 127.0.0.1:8000/ 주소
    path('', views.index, name='index'),
    
    # 127.0.0.1:8000/recommend/ 주소
    path('recommend/', views.recommend, name='recommend'),
]