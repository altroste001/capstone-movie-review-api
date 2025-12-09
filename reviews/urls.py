from django.urls import path
from .views import ReviewListCreateView, ReviewDetailView
from .views import (
    ReviewListCreateView,
    ReviewDetailView,
    MovieListCreateView,
    MovieDetailView
)

urlpatterns = [
    path('reviews/', ReviewListCreateView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    # Movie URLs
    path('movies/', MovieListCreateView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),

    # Review URLs
    path('reviews/', ReviewListCreateView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    
    ]