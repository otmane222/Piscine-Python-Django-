from django.shortcuts import render

# Create your views here.

def ex01_view(request):
    return render(request, 'index.html')