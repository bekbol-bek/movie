from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from .forms import MovieFrom


def add_movie(request,):
    if request.method == "POST":
        form = MovieFrom(request.POST, request.FILES, )
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieFrom()
    return render(request, 'htm/movie_add.html', {'form': form})

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'htm/movie_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movies = Movie.objects.all()
    return render(request, 'htm/movie_detail.html', {'movie': movie, 'movies': movies })

def movie_delete(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == "POST":
        movie.delete()
        return redirect('movie_list')
    return render(request, 'htm/movie_delete.html', {'movie': movie})

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


