from django.shortcuts import render
from .models import People, Planets
# Create your views here.



def display(request):
    ppl = People.objects.select_related('homeworld').filter(homeworld__climate__in=['windy', 'moderately wind']).order_by('name')
    print(ppl)

    data = []
    return render(request, 'ex09/display.html', {'data', data})