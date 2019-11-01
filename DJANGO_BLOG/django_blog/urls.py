from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('movies/', include('movies.urls')),
    path('pasts/', include('pasts.urls')),
    path('students/', include('students.urls')),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
]
