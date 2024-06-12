from django.test import TestCase
from django.urls import reverse

# Testando url genres de list 
class GenresURlsTeste(TestCase):
    def test_genres_list_create_is_url_correct(self):
        url = reverse('namespace:list')
        self.assertEqual(url, '/genres/')
            
    # teste de url genres de update e delete detail por id 
    def test_genres_update_delete_is_url_correct(self):
        url = reverse('namespace:detail', kwargs={'pk': 1})
        self.assertEqual(url, '/genres/1/')
