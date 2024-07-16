from django.shortcuts import render
from .models import Movies
from datetime import date
from django.db import IntegrityError

# Create your views here.

def display(request):
    movies = Movies.objects.all()
    return render (request, 'ex03/display.html', {'movies': movies})


def populate(request):
    movies_data = [
        {"title": "The Phantom Menace", "director": "George Lucas", "producer": "Rick McCallum", "release_date": date(1999, 5, 19)},
        {"title": "Attack of the Clones", "director": "George Lucas", "producer": "Rick McCallum", "release_date": date(2002, 5, 16)},
        {"title": "Revenge of the Sith", "director": "George Lucas", "producer": "Rick McCallum", "release_date": date(2005, 5, 19)},
        {"title": "A New Hope", "director": "George Lucas", "producer": "Gary Kurtz, Rick McCallum", "release_date": date(1977, 5, 25)},
        {"title": "The Empire Strikes Back", "director": "Irvin Kershner", "producer": "Gary Kurtz, Rick McCallum", "release_date": date(1980, 5, 17)},
        {"title": "Return of the Jedi", "director": "Richard Marquand", "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum", "release_date": date(1983, 5, 25)},
        {"title": "The Force Awakens", "director": "J. J. Abrams", "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "release_date": date(2015, 12, 18)},
    ]
    state = []
    try:    
        for movie_data in movies_data:
            new_movie = Movies(
                title=movie_data['title'],
                director=movie_data['director'],
                producer=movie_data['producer'],
                release_date=movie_data['release_date']
            )
            new_movie.save()
            state.append("OK")
    except IntegrityError:
        error_message = "One or more movies could not be added because they already exist."
        state.append(error_message)
        return render(request, 'ex03/populate.html', {'state': state})
    return render(request, 'ex03/populate.html', {'state': state})