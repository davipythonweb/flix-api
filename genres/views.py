# import json
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import get_object_or_404

from rest_framework import generics
from genres.models import Genre
from genres.serializers import GenreSerializer

"""
fluxo de criação dos apps:
models
views
serializers
urls
tests
admin
"""


"""CRUD PARA API COM DJANGO-REST-FRAMEWORK ORM e ClassBasedViews"""
    
# endpoint listar todos e criar COM => ClassBasedViews
class GenereCreateLIstView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

# endpoint para listar por id , update e delete COM => ClassBasedViews    
class GenereRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    
     
"""CRUD PARA API COM DJANGO-REST-FRAMEWORK ORM e FunctionBasedViews"""

"""
# endpoint listar todos e criar
@csrf_exempt
def genre_create_list_view(request):
    if request.method == 'GET':
        genres = Genre.objects.all() # pega todos o genero e retorna a lista
        data = [{'id': genre.id, 'name': genre.name} for genre in genres] # for na lista de dados , usando list-comprehension
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8')) # pegando os dados do request e decodificando para os caracteres padrao.
        new_genre = Genre(name=data['name']) # criando um novo genero para salvar
        new_genre.save() # salvando no banco
        return JsonResponse({'id': new_genre.id,
                             'name': new_genre.name},
                            status=201,) # mensagem de confirmaçao

"""
    
"""    
# endpoint listar por id e update e delete
@csrf_exempt        
def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk) # pega o dado pelo id, ou mostra o erro nao encontrado
    
    if request.method == 'GET':    
        data = {'id': genre.id, 'name': genre.name} # armazena em data
        return JsonResponse(data) # retorna o json
    
    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8')) # pegando os dados do request e decodificando para os caracteres padrao.
        genre.name = data['name'] # atribuindo o novo dado
        genre.save() # salvando no banco
        return JsonResponse({'id': genre.id, 'name': genre.name}) # mensagem de confirmaçao com novo dado alterado
    
    elif request.method == 'DELETE':
        genre.delete() # deletando dado
        return JsonResponse({'message': 
            'Gênero excluído com sucesso.'}, status=204,) #sms de exclusao
         
         
"""         
