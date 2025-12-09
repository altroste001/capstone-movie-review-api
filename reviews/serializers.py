from rest_framework import serializers
from .models import Review, Movie


        

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['user', 'created_at']


    def validate_rating(self, value):
        if value < 1 or value > 10:
            raise serializers.ValidationError("Rating must be between 1 and 10.")
        return value



class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    # Validate title
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    # Validate release year (simple check)
    def validate_release_year(self, value):
        if value < 1800 or value > 2100:
            raise serializers.ValidationError("Invalid release year.")
        return value
