from rest_framework import authentication
from waqur.models import Test123
from .serializers import Test123Serializer
from rest_framework import viewsets


class Test123ViewSet(viewsets.ModelViewSet):
    serializer_class = Test123Serializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Test123.objects.all()
