from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from cinemaPlus.models import Movie, Review,Genre,Director,Actor,Play
from django.db.models import Q, Avg, Count
from django.contrib.auth import authenticate, login
from .forms import ReviewForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.
# def home(request):
#     cat = request.GET.get('cat', "")
#     txt = request.GET.get('text', "")
#     try:
#         cat = int(cat)
#     except:
#         cat = False
#     if cat is False:
#         if txt == '':
#             movies = Movie.objects.all()
#         else:
#             movies = Movie.objects.filter(Q(summary__icontains=txt) | Q(title__icontains=txt))
#     else:
#         movies = Movie.objects.filter(genre_id=cat)
#     return render(request, 'cinemaPlus/home.html', {'movies': movies})


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    reviews = Review.objects.filter(movie=movie)
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.author = request.user.username
            review.save()
            return redirect('movie_detail', pk=pk)
    else:
        form = ReviewForm()
    return render(request, 'cinemaPlus/movie_detail.html',
                  {'movie': movie, 'reviews': reviews, 'form': form,
                   'average_rating': average_rating})


def aboutus(request):
    return render(request, 'cinemaPlus/aboutus.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')  # Change 'home' to the name of your home page URL pattern.
        else:
            # Return an 'invalid login' error message.
            return render(request, 'cinemaPlus/login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'cinemaPlus/login.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'You have successfully registered!')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
    else:
        form = UserCreationForm()
    return render(request, 'cinemaPlus/register.html', {'form': form})

def home(request):
    genres = Genre.objects.all()
    directors = Director.objects.all()
    actors = Actor.objects.annotate(movie_count=Count('play__movie')).order_by('-movie_count')

    cat_id = request.GET.get('cat', "")
    dir_id = request.GET.get('dir', "")
    actor_id = request.GET.get('actor', "")
    txt = request.GET.get('text', "")
    try:
        cat_id = int(cat_id)
    except:
        cat_id = False
    try:
        dir_id = int(dir_id)
    except:
        dir_id = False
    try:
        actor_id = int(actor_id)
    except:
        actor_id = False

    if cat_id is False and dir_id is False and actor_id is False:
        if txt == '':
            movies = Movie.objects.all()
        else:
            movies = Movie.objects.filter(Q(summary__icontains=txt) | Q(title__icontains=txt))
    elif cat_id is not False and dir_id is False and actor_id is False:
        movies = Movie.objects.filter(genre_id=cat_id)
    elif cat_id is False and dir_id is not False and actor_id is False:
        movies = Movie.objects.filter(director_id=dir_id)
    elif cat_id is False and dir_id is False and actor_id is not False:
        movies = Movie.objects.filter(play__actor_id=actor_id)
    else:
        movies = Movie.objects.filter(genre_id=cat_id, director_id=dir_id)

    return render(request, 'cinemaPlus/home.html',
                  {'movies': movies, 'genres': genres, 'directors': directors, 'actors': actors})