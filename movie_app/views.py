from django.shortcuts import render
from django.db.models import F, Sum, Max, Min, Count, Avg, Value

# Create your views here.

"""Импортируем наши записи класса"""
from .models import Movie
from .models import Director
from .models import Actor


def show_all_movies(request):
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


'------------------------------------------------------------------------------------------------------'


def show_all_directors(request):
    directors = Director.objects.all()

    for director in directors:
        director.save()
    return render(request, 'movie_app/all_directors.html', {
        'directors': directors,
    })


def show_one_director(request, id_dir: int):
    dir = Director.objects.get(id=id_dir)
    return render(request, 'movie_app/one_director.html', {
        'dir': dir,
    })


'------------------------------------------------------------------------------------------------------'


def show_all_actors(request):
    actors = Actor.objects.all()

    for actor in actors:
        actor.save()
    return render(request, 'movie_app/all_actors.html', {
        'actors': actors,
    })


def show_one_actor(request, id_act: int):
    act = Actor.objects.get(id=id_act)
    return render(request, 'movie_app/one_actor.html', {
        'act': act,
    })
