from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def oi_view(request):
    return JsonResponse({'message': 'Ola Mundo!'})
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', oi_view),
]
