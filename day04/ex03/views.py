from django.shortcuts import render
import random

# Create your views here.

def index(request):
    shades = generate_color_shades()

    context = {
        'shades': shades,
    }
    return render(request, 'ex03/index.html', context)

def generate_color_shades():
    # Generate 50 shades for each color
    shades = []
    for i in range(50):
        shades.append({
            'noir': f'hsl(0, 0%, {i * 2}%)',
            'rouge': f'hsl(0, 100%, {i * 2}%)',
            'bleu': f'hsl(240, 100%, {i * 2}%)',
            'vert': f'hsl(120, 100%, {i * 2}%)',
        })
    return shades
