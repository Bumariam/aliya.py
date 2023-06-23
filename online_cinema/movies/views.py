from django.shortcuts import render
from .models import Genre, Movie

def genre_movies(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    movies = Movie.objects.filter(genre=genre)
    return render(request, 'movies/genre_movies.html', {'genre': genre, 'movies': movies})


def movie_details(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request, 'movies/movie_details.html', {'movie': movie})
