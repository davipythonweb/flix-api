from django.test import TestCase
from django.urls import reverse

# Testando as duas urls
class GenresURlsTeste(TestCase):
    def test_genres_list_create_is_url_correct(self):
        url = reverse('namespace:create-list')
        self.assertEqual(url, 'genres/')
