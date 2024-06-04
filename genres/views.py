import json
from django.http import JsonResponse
from genres.models import Genre

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404


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


@csrf_exempt        
def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk) # pega o dado pelo id, ou mostra o erro nao encontrado
    
    data = {'id': genre.id, 'name': genre.name} # armazena em data
    return JsonResponse(data) # retorna o json
