from django.contrib import admin
from django.urls import path
from genres.views import genre_create_list_view, genre_detail_view


app_name = 'namespace'

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('genres/', genre_create_list_view, name='create-list'),
    path('genres/<int:pk>/',genre_detail_view, name='detail-view'),
]
