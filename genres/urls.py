from django.urls import path
from . import views


app_name = 'namespaceGenres'

urlpatterns = [
    path('genres/', views.GenereCreateLIstView.as_view(), name='list'),
    path('genres/<int:pk>/',views.GenereRetrieveUpdateDestroyView.as_view(), name='detail'),
    # path('genres/', views.genre_create_list_view, name='list'),
    # path('genres/<int:pk>/',views.genre_detail_view, name='detail'),
]
