from django.shortcuts import render
from .models import People, Planets
from django.http import HttpResponse
# Create your views here.



def display(request):
    ppl = People.objects.select_related('homeworld').order_by('name')


    data = []
    for person in ppl:
        homeworld = person.homeworld 
        homeworld_name = homeworld.name if homeworld else 'unknown'
        homeworld_climate = homeworld.climate if homeworld else 'unknown' 
        character_data = {
            'name': person.name,
            'homeworld': homeworld_name,
            'climate': homeworld_climate,
        }
        data.append(character_data)
    return render(request, 'ex09/display.html', {'data': data})