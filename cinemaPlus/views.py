from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from cinemaPlus.models import Movie, Review
from django.db.models import Q, Avg
from django.contrib.auth import authenticate, login
from .forms import ReviewForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


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