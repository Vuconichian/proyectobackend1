from django import forms

from futbolistas.models import Futbolista, Director, Estadio, User

class FutbolistaForm(forms.ModelForm):
       class Meta:
        model = Futbolista
        fields = [
            'name',
            'number',
            'team',
            'worldchampion',
        ]

class DirectorForm(forms.ModelForm):
       class Meta:
        model = Director
        fields = [
            'name',
            'country',
            'team',
            'worldchampion',
        ]

class EstadioForm(forms.ModelForm):
       class Meta:
        model = Estadio
        fields = [
            'name',
            'country',
            'capacity'
        ]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'futbolistas',
            'directors',
            'estadios',
        ]