from rest_framework import viewsets
from .serializers import MusicSerializer
from myapp.models import Music


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer