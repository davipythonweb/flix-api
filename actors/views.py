from rest_framework import generics
from actors.models import Actor

from actors.serializers import ActorSerializer

from rest_framework.permissions import IsAuthenticated

from core.permissions import GlobalDefaultPermission


class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission) # permissao para as views com acesso via token jwt
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission) # permissao para as views com acesso via token jwt
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer