from django.forms import ModelForm, EmailInput

from personas.models import Persona


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'  # Para usar todos los atributos del objeto persona
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }