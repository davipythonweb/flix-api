from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from movies.models import Movie

from movies.serializers import MovieSerializer, MovieListDetailSerializer, MovieStatsSerializer
from reviews.models import Review

# from movies.serializers import MovieTesteSerializer



# Definição da view para criação e listagem de filmes
class MovieCreateListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()  # Consulta para obter todos os filmes
    
    # Método para determinar o serializer a ser usado com base no método HTTP
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer  # Serializer para listagem detalhada de filmes
        return MovieSerializer  # Serializer para criação de filmes


# Definição da view para recuperação, atualização e exclusão de um filme específico
class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()  # Consulta para obter todos os filmes
    
    # Método para determinar o serializer a ser usado com base no método HTTP
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer  # Serializer para detalhamento do filme
        return MovieSerializer  # Serializer para atualização e exclusão de filmes


# View personalizada para obter estatísticas sobre os filmes e avaliações
class MovieStatsView(views.APIView):
    queryset = Movie.objects.all()  # Consulta para obter todos os filmes

    def get(self, request):
        total_movies = self.queryset.count()  # Contagem total de filmes
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))  # Contagem de filmes por gênero
        total_reviews = Review.objects.count()  # Contagem total de avaliações
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']  # Média de estrelas das avaliações

        # Dados a serem enviados na resposta
        data = {
            'total_movies': total_movies,
            'movies_by_genre': movies_by_genre,
            'total_reviews': total_reviews,
        
        # garante que o valor seja arredondado para uma casa decimal e,
        # se não houver avaliações (average_stars for None), retorna 0.
            'average_stars': round(average_stars, 1) if average_stars else 0,
        }
        

        # Serialização dos dados
        serializer = MovieStatsSerializer(data=data)
        serializer.is_valid(raise_exception=True)  # Validação dos dados serializados

        return response.Response(
            data=serializer.data,  # Dados serializados na resposta
            status=status.HTTP_200_OK,  # Código de status HTTP 200 (OK)
        )
    



"""
Explicação dos componentes principais:

1-Imports:

    Count e Avg são funções de agregação do Django para contar registros e calcular a média.

    generics e views são classes base do Django REST framework para criar views.

    response e status são utilizados para criar respostas HTTP e definir códigos de status HTTP.

    Movie e Review são modelos importados dos respectivos aplicativos.

    MovieSerializer, MovieListDetailSerializer e MovieStatsSerializer são 
    serializers para manipular os dados dos filmes.

2-Views genéricas:

    MovieCreateListView e MovieRetrieveUpdateDestroyView são 
    views genéricas para operações CRUD em filmes, utilizando 
    diferentes serializers dependendo do método HTTP.

3-View personalizada MovieStatsView:

    Coleta estatísticas sobre os filmes e avaliações.

    Usa consultas e agregações para obter dados como contagem total de filmes,
    contagem de filmes por gênero, total de avaliações e média de estrelas.

    Serializa esses dados e os retorna em uma resposta HTTP 200 (OK).

"""