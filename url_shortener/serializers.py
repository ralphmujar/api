# snippets/serializers
from rest_framework import serializers
from .models import Url

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ('short_url', 'long_url', 'created_at')
