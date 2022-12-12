from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

LISTA_REGIONES = [
    ['Region Metropolitana', 'Region Metropolitana'],
]

LISTA_COMUNAS_RM = [
    ['Cerrillos', 'Cerrillos'],
    ['Cerro Navia', 'Cerro Navia'],
    ['Conchalí', 'Conchalí'],
    ['El Bosque', 'El Bosque'],
    ['Estación Central', 'Estación Central'],
    ['Huechuraba', 'Huechuraba'],
    ['Independencia', 'Independencia'],
    ['Cisterna', 'Cisterna'],
    ['La Florida', 'La Florida'],
    ['La Granja', 'La Granja'],
    ['La Pintana', 'La Pintana'],
    ['La Reina', 'La Reina'],
    ['Las Condes', 'Las Condes'],
    ['Lo Barnechea', 'Lo Barnechea'],
    ['Lo Espejo', 'Lo Espejo'],
    ['Lo Prado', 'Lo Prado'],
    ['Macul', 'Macul'],
    ['Maipú', 'Maipú'],
    ['Ñuñoa', 'Ñuñoa'],
    ['Pedro Aguirre Cerda', 'Pedro Aguirre Cerda'],
    ['Peñalolén', 'Peñalolén'],
    ['Providencia', 'Providencia'],
    ['Pudahuel', 'Pudahuel'],
    ['Quilicura', 'Quilicura'],
    ['Quinta Normal', 'Quinta Normal'],
    ['Recoleta', 'Recoleta'],
    ['Renca', 'Renca'],
    ['Santiago', 'Santiago'],
    ['San Joaquín', 'San Joaquín'],
    ['San Miguel', 'San Miguel'],
    ['San Ramón', 'San Ramón'],
    ['Vitacura', 'Vitacura'],
    ['Puente Alto', 'Puente Alto'],
    ['Pirque', 'Pirque'],
    ['San José de Maipo', 'San José de Maipo'],
    ['Colina', 'Colina'],
    ['Lampa', 'Lampa'],
    ['Tiltil', 'Tiltil'],
    ['San Bernardo', 'San Bernardo'],
    ['Buin', 'Buin'],
    ['Calera de Tango', 'Calera de Tango'],
    ['Paine', 'Paine'],
    ['Melipilla', 'Melipilla'],
    ['Alhué', 'Alhué'],
    ['Curacaví', 'Curacaví'],
    ['María Pinto', 'María Pinto'],
    ['San Pedro', 'San Pedro'],
    ['Talagante', 'Talagante'],
    ['El Monte', 'El Monte'],
    ['Isla de Maipo', 'Isla de Maipo'],
    ['Padre Hurtado', 'Padre Hurtado'],
    ['Peñaflor', 'Peñaflor'],

]

TIPO_USUARIO = [
    ['Administrador', 'Administrador'],
    ['Usuario', 'Usuario'],
    ['Recolector', 'Recolector'],
    ['Invitado', 'Invitado'],

]

class FotosForm(forms.ModelForm):

    class Meta:
        model = Fotos
        fields = '__all__'
class CuentaUsuarioCreationForm(UserCreationForm):
    # Perfil_usuario = forms.ChoiceField(choices=TIPO_USUARIO, label='Seleccione el tipo de rol para el sitio')
    Comuna = forms.ChoiceField(choices=LISTA_COMUNAS_RM, label='Seleccione la comuna')
    Region = forms.ChoiceField(choices=LISTA_REGIONES, label='Seleccione la region')


    class Meta:
        model = CuentaUsuario
        fields = ['Perfil_usuario', 'Rut', 'Rut_Empresa', 'Nombre_de_empresa', 'first_name', 'last_name', 'Correo', 'Telefono', 'Direccion', 'Comuna', 'Region', 'username', 'password1', 'password2', 'date_joined']


class RegistroAvisoForm(forms.ModelForm):
    Titulo_de_publicacion = forms.CharField(max_length=100, label='Ingrese un Titulo')
    Comuna = forms.ChoiceField(choices=LISTA_COMUNAS_RM, label='Seleccione la comuna')
    Region = forms.ChoiceField(choices=LISTA_REGIONES, label='Seleccione la region')

    class Meta:
        model = RegistroAviso
        fields = ['Region', 'Comuna', 'Titulo_de_publicacion', 'Descripcion', 'Fecha_publicacion']



# class RegistroForm(UserCreationForm):
#     username = forms.CharField(required=True, label= 'Crear una cuenta de usuario')
#     email = forms.EmailField(required=True, label='Ingrese el mail de validacion.')
#     password1 = forms.CharField(widget=forms.PasswordInput, label='Ingrese una contraseña')
#     password2 = forms.CharField(widget=forms.PasswordInput, label='Repita la contraseña')
#     is_active = forms.BooleanField(required=True)
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2','is_active']





# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2', 'user_permissions', 'date_joined', 'last_login']


