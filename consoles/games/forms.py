from django import forms

from .models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'characters', 'release_date']
        widgets = {
            'release_date': forms.DateInput()
        }
        