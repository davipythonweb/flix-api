from rest_framework import serializers
from movies.models import Movie

# from genres.models import Genre
# from actors.models import Actor
from django.db.models import Avg

from actors.serializers import ActorSerializer
from genres.serializers import GenreSerializer




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

# Serializer para o modelo Movie com todas as operações CRUD
class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'  # Inclui todos os campos do modelo Movie
    
    # Validação personalizada para a data de lançamento
    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990.')
        return value
    
    # Validação personalizada para o resumo
    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('Resumo não deve ser maior do que 200 caracteres.')
        return value


# Serializer detalhado para listagem de filmes, incluindo relações
class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)  # Serializa os atores relacionados
    genre = GenreSerializer()  # Serializa o gênero relacionado
    rate = serializers.SerializerMethodField()  # Campo calculado para a média das avaliações

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    # Método para obter a média das avaliações (rate)
    def get_rate(self, obj):
        average_rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if average_rate:
            return round(average_rate, 1)  # Retorna a média arredondada para uma casa decimal


# Serializer para estatísticas de filmes
class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()  # Campo para o total de filmes
    movies_by_genre = serializers.ListField()  # Campo para a contagem de filmes por gênero
    total_reviews = serializers.IntegerField()  # Campo para o total de avaliações
    average_stars = serializers.FloatField()  # Campo para a média de estrelas das avaliações





"""
Explicação dos componentes principais:

1-Imports:

    serializers do Django REST framework para criar serializers.
    Movie do aplicativo de filmes.
    Avg do Django para calcular a média dos valores.
    ActorSerializer e GenreSerializer para serializar relações de atores e gêneros.

2-MovieSerializer:

    Serializa todos os campos do modelo Movie.
    Inclui validações personalizadas para a data de lançamento (release_date) e o resumo (resume).

3-MovieListDetailSerializer:

    Inclui campos relacionados (atores e gênero) usando serializers aninhados.
    Adiciona um campo calculado (rate) para a média das avaliações.

4-MovieStatsSerializer:

    Define os campos para estatísticas de filmes, 
    incluindo total de filmes, contagem de filmes por gênero,
    total de avaliações e média de estrelas.

"""