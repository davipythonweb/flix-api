from django.test import TestCase
from django.urls import reverse


# # Testando url actors de list 
class ActorsURlsTeste(TestCase):
    def test_actors_list_create_is_url_correct(self):
        url = reverse('namespaceActors:list')
        self.assertEqual(url, '/actors/')
            
#     # testando url actors de update e delete por id
    def test_actors_update_delete_is_url_correct(self):
        url = reverse('namespaceActors:retrive', kwargs={'pk': 1})
        self.assertEqual(url, '/actors/1/')
