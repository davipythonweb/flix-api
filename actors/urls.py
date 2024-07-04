from django.urls import path
from . import views

app_name = 'namespaceActors'

urlpatterns = [
    path('actors/', views.ActorCreateListView.as_view(), name='list'),
    path('actors/<int:pk>/',views.ActorRetrieveUpdateDestroyView.as_view(), name='retrive'),
    
]
