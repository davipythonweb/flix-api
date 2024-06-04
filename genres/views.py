import json
from django.http import JsonResponse
from genres.models import Genre

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def genre_view(request):
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
        
    