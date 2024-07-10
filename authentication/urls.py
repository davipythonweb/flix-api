from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
     path('authentication/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

     path('authentication/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

     path('authentication/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

# token normal= validade 5min
# refresh-token = validade 24h, pode fazer refresh de 5min em 5 min
# token = Bearer Token