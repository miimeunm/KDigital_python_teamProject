from django.urls import path
from . import views

app_name = 'exercise'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('result/', views.result, name='result'),
    path('detail/<int:id>/', views.detail, name='detail'),
]
