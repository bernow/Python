from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('<int:movie_id>/scores/<int:score_id>/delete', views.score_delete, name='score_delete'),
    path('<int:movie_id>/scores/', views.score_create, name='score_create'),
    path('<int:movie_id>/delete/', views.delete, name='delete'),
    path('<int:movie_id>/update/', views.update, name='update'),
    path('<int:movie_id>/', views.detail, name='detail'),
    path('', views.index, name='index'),
]