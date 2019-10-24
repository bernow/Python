from django.urls import path
from . import views

app_name = 'artii'

urlpatterns = {
    path('', views.artii),
    path('result/', views.result),
}