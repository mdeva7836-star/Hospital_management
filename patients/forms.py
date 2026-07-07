# patients/forms.py
from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'height', 'weight', 'age', 'bp_level']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'bp_level': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '120/80'}),
        }