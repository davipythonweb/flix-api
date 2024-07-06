from django.test import TestCase
from django.urls import reverse

# # Testando url reviews de list 
class ReviewsURlsTeste(TestCase):
    def test_reviews_list_create_is_url_correct(self):
        url = reverse('namespaceReviews:list')
        self.assertEqual(url, '/api/v1/reviews/')
            
#     # testando url reviews de update e delete por id
    def test_reviews_update_delete_is_url_correct(self):
        url = reverse('namespaceReviews:retrieve', kwargs={'pk': 1})
        self.assertEqual(url, '/api/v1/reviews/1/')
