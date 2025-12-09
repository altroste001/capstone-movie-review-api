from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField()
    rating = models.IntegerField()  
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie.title} - {self.rating}/10 by {self.user.username}"
