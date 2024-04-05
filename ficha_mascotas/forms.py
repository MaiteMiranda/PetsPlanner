from django import forms
from .models import Usuarios

class RegistroForm(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuarios
        fields = ['nombre', 'apellido', 'email', 'contraseña', 'perfil', 'telefono', 'direccion']
