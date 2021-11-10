from django import forms
from django.db.models.base import Model
from django.forms import fields
from myapp.models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        # fields = ['name', 'email', 'jersey_no', 'role']
        fields = '__all__'
        # exclude = ['email']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'jersey_no': forms.NumberInput(attrs={'class':'form-control'}),
            'role': forms.TextInput(attrs={'class':'form-control'}),
        }