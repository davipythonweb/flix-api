from rest_framework import serializers
from movies.models import Movie

# from genres.models import Genre
# from actors.models import Actor


# criando serializer na mão, sem o [ModelSerializer] 
# obs:só funciona GET,não tem metodo create
"""
class MovieTesteSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    genre = serializers.PrimaryKeyRelatedField(
        queryset = Genre.objects.all(),
    )
    release_date = serializers.DateField()
    actors = serializers.PrimaryKeyRelatedField(
        queryset = Actor.objects.all(),
        many = True,
    )
    resume = serializers.CharField()
"""

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'