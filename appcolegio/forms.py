from django import forms

class cargarcurso(forms.Form):
    curso = forms.CharField()
    division = forms.IntegerField()

class buscarCursos(forms.Form):
    curso = forms.CharField()
    







class BuscaCursoForm(forms.Form):
    curso = forms.CharField()





class cargarprof(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()
    email = forms.EmailField()





class cargarestu(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.IntegerField()
    email = forms.EmailField()


class cargarmateria(forms.Form):
    nombre = forms.CharField()
    codigo = forms.IntegerField()