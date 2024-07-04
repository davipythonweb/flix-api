from django.urls import path
from . import views

app_name = 'namespaceReviews'

urlpatterns = [
    path('reviews/', views.ReviewCreateListView.as_view(), name='list'),
    path('reviews/<int:pk>/',views.ReviewRetrieveUpdateDestroyView.as_view(), name='retrieve'),
]
