from rest_framework import serializers

from futbolistas.models import Futbolista, Director, Estadio


class FutbolistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Futbolista
        fields = ['name', 'number', 'team', 'worldchampion']

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['name', 'country', 'team', 'worldchampion']

class EstadioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadio
        fields = ['name', 'country', 'capacity']


