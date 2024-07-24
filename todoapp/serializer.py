from rest_framework import serializers
from .models import Breed,Dog


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dog
        fields='__all__'
        
class BreedSerializer(serializers.ModelSerializer):
    dogs=DogSerializer(many=True,read_only=True)
    # breeds=BreedSerializer(many=True,read_only=True)
    class Meta:
        model=Breed
        fields='__all__'
        

