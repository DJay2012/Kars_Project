from django import forms
from .models import Kar

class KarForm(forms.ModelForm):
    class Meta:
        model = Kar
        fields = ['make', 'model', 'year', 'price', 'description', 'image']
