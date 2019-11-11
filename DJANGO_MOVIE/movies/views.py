from django.shortcuts import render, redirect
from .models import Genre, Movie, Score

def index(request):
    movies = Movie.objects.order_by('-pk')
    return render(request, 'movies/index.html', {'movies':movies})

def detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    scores = movie.score_set.order_by('-pk')
    # scores = movie.score_set.all()
    return render(request, 'movies/detail.html', {'movie':movie, 'scores': scores})
# 'scores':scores}

def delete(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie.pk)

def update(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if request.method == 'POST':
        movie.title = request.POST.get('title')
        movie.audience = request.POST.get('audience')
        movie.poster_url = request.POST.get('poster_url')
        movie.description = request.POST.get('description')
        movie.save()
        return redirect('movies:detail', movie.pk)
    else:
        return render(request, 'movies/edit.html', {'movie':movie}) 

def score_create(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if request.method == 'POST':
        score = Score()
        score.content = request.POST.get('content')
        score.score = request.POST.get('score')
        score.movie_id = movie
        score.save()
        return redirect('movies:detail', movie.pk)
    else:
        return redirect('movies:detail', movie.pk)

def score_delete(request, movie_id, score_id):
    if request.method == 'POST':
        score = Score.objects.get(pk=score_id)
        score.delete()
    return redirect('movies:detail',movie_id)   