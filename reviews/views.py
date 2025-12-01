from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .models import Review
from .serializers import ReviewSerializers

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        
class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)        

# Create your views here.
