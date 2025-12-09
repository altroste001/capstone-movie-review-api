from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied, NotFound
from .models import Review, Movie
from .serializers import ReviewSerializer, MovieSerializer


class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Attach current user to review
        serializer.save(user=self.request.user)
        
        
        
class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self):
        try:
            return super().get_object()
        except:
            raise NotFound("Review not found.")

    def perform_update(self, serializer):
        review = serializer.instance
        if review.user != self.request.user:
            raise PermissionDenied("You can only update your own review.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied("You can only delete your own review.")
        instance.delete()
        
class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Only admin/staff can create movies
    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            raise PermissionDenied("Only admin users can add movies.")
        serializer.save()     
        
class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # 404 handling
    def get_object(self):
        try:
            return super().get_object()
        except:
            raise NotFound("Movie not found.")

    # Only admin/staff can update movies
    def perform_update(self, serializer):
        if not self.request.user.is_staff:
            raise PermissionDenied("Only admin users can update movies.")
        serializer.save()

    # Only admin/staff can delete movies
    def perform_destroy(self, instance):
        if not self.request.user.is_staff:
            raise PermissionDenied("Only admin users can delete movies.")
        instance.delete()
           



