from django.contrib import admin

from movie_app.models import Movie, Review

# Register your models here.
admin.site_app.register(Movie)
admin.site_app.register(Review)
