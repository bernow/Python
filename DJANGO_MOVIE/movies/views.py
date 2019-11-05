from django.shortcuts import render
from .models import Genre, Movie, Score

def index(request):
    movies = Movie.objects.order_by('-pk')
    return render(request, 'movies/index.html', {'movies':movies})


