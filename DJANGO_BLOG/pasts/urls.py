from django.urls import path
from . import views

app_name = 'pasts'

urlpatterns = [
    path('past_life', views.past_life, name='past_life'),
    path('', views.index, name='index'),
]