from django.shortcuts import render
from django.db.models import F, Sum, Max, Min, Count, Avg, Value

# Create your views here.

"""Импортируем наши записи класса"""
from .models import Movie


def show_all_movies(request):
    # manage.py createsuperusermovies = Movie.objects.order_by('name')
    movies = Movie.objects.annotate(
        true_bool=Value(True),
        false_bool=Value(False),
        new_budget=F('budget') + 100,
        new_rating_and_year=F('rating') + F('year')

    )
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('name'))

    for movie in movies:
        movie.save()
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg': agg,
    })


def show_one_movies(request, slug_movie: str):
    movie = Movie.objects.get(slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie,
    })
