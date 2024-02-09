from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    duration = models.IntegerField()  # Duration in minutes
    release_date = models.DateField()
    imdb_url = models.URLField()
    image = models.ImageField(upload_to='movie_images/')
    summary = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genres = models.ForeignKey(Genre, null=True, on_delete=models.CASCADE)  # giati to evala many to many

    def __str__(self):
        return self.title


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Play(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

# class Review(models.Model):
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
#     author = models.CharField(max_length=100)
#     rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)])
#     comment = models.TextField()
#
#     def __str__(self):
#         return f"Review for {self.movie}: {self.rating}"
