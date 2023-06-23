from django.contrib import admin
from django.urls import path
from movies.views import genre_movies, movie_details


urlpatterns = [
    path('admin/', admin.site.urls),
    path('genre/<int:genre_id>/', genre_movies, name='genre_movies'),
    path('movie/<int:movie_id>/', movie_details, name='movie_details'),
]


