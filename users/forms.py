from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        # Si queremos EDIAR los mensajes de ayuda editamos este dict,
            # de lo contrario lo limpiamos de ésta forma.
        help_text = {k: "" for k in fields}


class UserEditForm(UserCreationForm):

    first_name = forms.CharField(label='Primer Nombre:')
    last_name = forms.CharField (label='Segundo Nombre:')
    
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Actual Contraseña ', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput)

    

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'password1',
            'password2',
            'email'
            
        ]
        help_texts = {k:"" for k in fields}