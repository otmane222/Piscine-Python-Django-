from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse
from .forms import Search
from .models import People, Planets, Movies

# Create your views here.



def the_view(request):
    data = []
    if request.method == 'POST':
        form = Search(request.POST)
        if form.is_valid():
            minimum_date = form.cleaned_data['minimum_date']
            maximum_date = form.cleaned_data['maximum_date']
            diameter_num = form.cleaned_data['diameter_num']
            gendero = form.cleaned_data['gender']
            print(minimum_date, maximum_date, diameter_num, gendero, "+++++++++")

            movies = Movies.objects.filter(release_date__gte=minimum_date, release_date__lte=maximum_date)
            print(movies, "-----------")

            if movies:
                for movie in movies:
                    people = People.objects.filter(movies__title__icontains=movie, gender=gendero)
                    for char in people:
                        if char.homeworld:
                            homeworld_name = char.homeworld.name
                            homeworld_diameter = char.homeworld.diameter
                        else:
                            homeworld_name = "Unknown"
                            homeworld_diameter = "Unknown"
                        obj = {
                            'title' : movie,
                            'name' : char.name,
                            'gender' : char.gender,
                            'homeworld': homeworld_name,
                            'diameter': homeworld_diameter
                        }
                        data.append(obj)
                        
            else:
                context = {
                    'no_resalt': True,
                    'get': False,
                }
            return render (request, 'ex10/display.html', {'data':data})
    else:
        form = Search()
    context = {
        'get': True,
        'form': form,
    }
    return render (request, 'ex10/display.html', context)
