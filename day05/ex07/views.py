# from django.shortcuts import render, redirect
# from datetime import date
# from django.db import connection, IntegrityError
# from .models import Movies07

# # Create your views here.

# def display(request):
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT episode_nb, title, opening_crawl, director, producer, release_date,created, updated FROM ex07_movies")
#         data = cursor.fetchall()
#     # Format data into a list of dictionaries for easier template rendering
#     data = [{'episode_nb':row[0], 'title':row[1], 'opening_crawl':row[2], 'director':row[3], 'producer':row[4], 'release_date':row[5], 'created':row[6], 'updated':row[7]} for row in data]

#     return render(request, 'ex07/display.html', {'data': data})

# def populate(request):
#     movies_data = [
#         {"title": "The Phantom Menace", "director": "George Lucas", "producer": "Rick McCallum", "release_date": date(1999, 5, 19)},
#         {"title": "Attack of the Clones", "director": "George Lucas", "producer": "Rick McCallum", "release_date": date(2002, 5, 16)},
#         {"title": "Revenge of the Sith", "director": "George Lucas", "producer": "Rick McCallum", "release_date": date(2005, 5, 19)},
#         {"title": "A New Hope", "director": "George Lucas", "producer": "Gary Kurtz, Rick McCallum", "release_date": date(1977, 5, 25)},
#         {"title": "The Empire Strikes Back", "director": "Irvin Kershner", "producer": "Gary Kurtz, Rick McCallum", "release_date": date(1980, 5, 17)},
#         {"title": "Return of the Jedi", "director": "Richard Marquand", "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum", "release_date": date(1983, 5, 25)},
#         {"title": "The Force Awakens", "director": "J. J. Abrams", "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "release_date": date(2015, 12, 18)},
#     ]
#     state = []
#     try:    
#         for movie_data in movies_data:
#             new_movie = Movies07(
#                 title=movie_data['title'],
#                 director=movie_data['director'],
#                 producer=movie_data['producer'],
#                 release_date=movie_data['release_date']
#             )
#             new_movie.save()
#             state.append("OK")
#     except IntegrityError:
#         error_message = "One or more movies could not be added because they already exist."
#         state.append(error_message)
#         return render(request, 'ex07/populate.html', {'state': state})
#     return render(request, 'ex07/populate.html', {'state': state})


# def update(request):
#     if (request.method == 'POST'):
#         titlo = request.POST.get('title')
#         text = request.POST.get('text')
#         movie = Movies07.objects.get(title=titlo)
#         movie.update_opening_crawl(text)
#         return redirect('display')
#     else:
#         with connection.cursor() as cursor:
#             cursor.execute("SELECT episode_nb, title FROM ex07_movies")
#             data = cursor.fetchall()
#         # Format data into a list of dictionaries for easier template rendering
#         movies = [{'title': row[1]} for row in data]
#         # cursor.close()
#         return render (request, 'ex07/update.html', {'movies': movies})