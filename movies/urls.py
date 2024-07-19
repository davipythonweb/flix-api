from django.urls import path
from . import views

app_name = 'namespaceMovies'

urlpatterns = [
    path('movies/', views.MovieCreateListView.as_view(), name='list'),
    path('movies/<int:pk>/',views.MovieRetrieveUpdateDestroyView.as_view(), name='retrieve'),
     path('movies/stats/', views.MovieStatsView.as_view(), name='movie-stats-view'),
]
