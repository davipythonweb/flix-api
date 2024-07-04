from django.test import TestCase
from django.urls import reverse

# # Testando url movies de list 
class MoviesURlsTeste(TestCase):
    def test_movies_list_create_is_url_correct(self):
        url = reverse('namespaceMovies:list')
        self.assertEqual(url, '/movies/')
            
#     # testando url movies de update e delete por id
    def test_movies_update_delete_is_url_correct(self):
        url = reverse('namespaceMovies:retrieve', kwargs={'pk': 1})
        self.assertEqual(url, '/movies/1/')
