from django.shortcuts import render

from cinemaPlus.models import Movie


# Create your views here.
def home(request):
    movies = Movie.objects.filter
    return render(request, 'cinemaPlus/home.html', {})
