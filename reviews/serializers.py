from rest_framework import serializers
from .models import Review


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        models = Review
        fields = ['id', 'movie_title', ' content', 'rating', 'user', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']