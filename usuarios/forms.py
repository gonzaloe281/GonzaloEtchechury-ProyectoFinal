from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
<<<<<<< HEAD
from usuarios.models import MetaDataUsuarios
=======

>>>>>>> 5c49fb87b60539352bf54de9f342e3469343c334
class FormularioDeRegistro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {key: '' for key in fields}
    
        
class EditarUsuario(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    avatar = forms.ImageField(required=False)
<<<<<<< HEAD
    hobbie = forms.CharField(required=False, max_length=100, label='Hobbies')
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar', 'hobbie']
=======
    
    class Meta:
        model = User
        fields = ['email','first_name', 'last_name', 'avatar']
    
>>>>>>> 5c49fb87b60539352bf54de9f342e3469343c334
