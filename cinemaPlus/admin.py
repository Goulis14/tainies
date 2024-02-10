from django.contrib import admin
from .models import Movie, Genre, Play, Actor, Review, Director

# Register your models here.

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Review)
admin.site.register(Director)
admin.site.register(Play)
