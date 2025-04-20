from django import forms
from django.contrib.auth.models import User

class Registro_Usuario(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'senha')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nome'
        self.fields['senha'].label = 'Senha'