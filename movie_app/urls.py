from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movies),
    path('movie/<slug:slug_movie>', views.show_one_movies, name='movie-detail'),
    path('directors/', views.show_all_directors, name='list_directors'),
    path('directors/<int:id_dir>', views.show_one_director, name='one_dir'),
    path('actors/', views.show_all_actors, name='list_actors'),
    path('actors/<int:id_act>', views.show_one_actor, name='one_act'),
]
