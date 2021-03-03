from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from trend.models import contactModel



class contactForm(forms.ModelForm):
    class Meta:
        model= contactModel
        fields= '__all__'
        widgets = {
            'Name':forms.TextInput(attrs={'class': 'form-control'}),
            'Email':forms.TextInput(attrs={'class': 'form-control'}), 
            'Ask_us_anything':forms.Textarea(attrs={'class': 'form-control'}),
            
        }
