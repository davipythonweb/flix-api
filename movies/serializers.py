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

    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990.')
        return value
    
    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('Resumo não deve ser maior do que 200 caracteres.')
        return value