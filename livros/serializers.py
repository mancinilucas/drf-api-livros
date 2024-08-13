from .models import Livro
from rest_framework import serializers


class LivrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
