from myapp.models import Music
from rest_framework import serializers


class MusicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Music
        fields = ('title', 'genre',  'singer')