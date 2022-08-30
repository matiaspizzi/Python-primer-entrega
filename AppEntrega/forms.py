from django import forms


class formDeporte(forms.Form):
    nombre = forms.CharField()
    turno = forms.CharField()
    comision = forms.IntegerField()


class formProfesor(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()

class formSocio(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    dni = forms.IntegerField()
    