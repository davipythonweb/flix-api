from django.test import TestCase
from django.urls import reverse

# # Testando url reviews de list 
class ReviewsURlsTeste(TestCase):
    def test_reviews_list_create_is_url_correct(self):
        url = reverse('namespaceReviews:list')
        self.assertEqual(url, '/reviews/')
            
#     # testando url reviews de update e delete por id
    def test_reviews_update_delete_is_url_correct(self):
        url = reverse('namespaceReviews:retrieve', kwargs={'pk': 1})
        self.assertEqual(url, '/reviews/1/')
