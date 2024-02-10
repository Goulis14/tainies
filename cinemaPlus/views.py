from django.shortcuts import render, get_object_or_404
from cinemaPlus.models import Movie, Genre
from django.db.models import Q

# Create your views here.
def home(request):
    cat = request.GET.get('cat', "")
    txt = request.GET.get('text', "")
    try:
        cat = int(cat)
    except:
        cat = False
    if cat is False:
        if txt == '':
            movies = Movie.objects.all()
        else:
            movies = Movie.objects.filter(Q(summary__icontains=txt) | Q(title__icontains=txt))
    else:
        movies = Movie.objects.filter(genre_id=cat)
    return render(request, 'cinemaPlus/home.html', {'movies': movies})


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'cinemaPlus/movie_detail.html', {'movie': movie})

def aboutus(request):
    return render(request, 'cinemaPlus/aboutus.html')
