from django.shortcuts import render
from django.http import HttpResponse
from .models import curso, prof, estu, mate
from appcolegio.forms import cargarcurso, buscarCursos, cargarprof, cargarestu,cargarmateria
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages


def inicio(request):
    return render(request, "appcolegio/index.html")

def buscarCurso(request):
    if request.method == "POST":
        miFormulario = buscarCursos(request.POST)
        
        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            cursos = curso.objects.filter(nombre__icontains=informacion["curso"])
        
            return render(request, "appcolegio/ver_busqueda.html", {"cursos": cursos})
    else:
        miFormulario = buscarCursos()

    return render(request, "appcolegio/mostrar_busqueda.html", {"miFormulario": miFormulario})

#CURSOS BASADO EN CLASES
def cursos(request):

    if request.method == "POST":
        miFormulario = cargarcurso(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cursos = curso(nombre=informacion["curso"], division=informacion["division"])
            cursos.save()
            return render(request, "appcolegio/cursos_list.html")
    else:
        miFormulario = cargarcurso()

    return render(request, "appcolegio/curso_list.html", {"miFormulario": miFormulario})

class cursolista(PermissionRequiredMixin,LoginRequiredMixin, ListView):
    model = curso
    template_name = "appcolegio/curso_list.html"
    permission_required = 'appcolegio.view_curso'

        
class cursodetalle(LoginRequiredMixin, DetailView):
    model = curso
    template_name = "appcolegio/curso_detalle.html"
    
class cursocreate(LoginRequiredMixin,CreateView):
  
    model = curso
    template_name = "appcolegio/curso_create.html"
    fields = ["nombre", "division"]
    success_url = reverse_lazy("cursoLista")
    

class cursomodificacion(LoginRequiredMixin, UpdateView):
    model = curso
    success_url = reverse_lazy("cursoLista")
    fields = ["nombre", "division"]
    template_name = "appcolegio/curso_modificacion.html"

class cursoborrar(LoginRequiredMixin, DeleteView):
    model = curso
    template_name = 'appcolegio/curso_confirmacion_borrar.html'
    success_url = reverse_lazy("cursoLista")
    

#PROFESORES BASADO EN CLASES
def profesores(request):

    if request.method == "POST":
        miFormulario = cargarprof(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profe = prof(nombre=informacion["nombre"], apellido=informacion["apellido"]
                         , dni=informacion["dni"], email=informacion["email"])
            profe.save()
            return render(request, "appcolegio/index.html")
    else:
        miFormulario = cargarprof()

    return render(request, "appcolegio/profesores.html", {"miFormulario": miFormulario})

class profesoreslista(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    model = prof
    template_name = "appcolegio/profesores_list.html"
    permission_required = 'appcolegio.view_prof'
    success_url = reverse_lazy("cursoLista")

class profesoresdetalle(LoginRequiredMixin,DetailView):
    model = prof
    template_name = "appcolegio/profesores_detalle.html"
    
    
class profesorescreate(LoginRequiredMixin,CreateView):
  
    model = prof
    template_name = "appcolegio/profesores_create.html"
    fields = ["nombre", "apellido", "dni", "email"]
    success_url = reverse_lazy("profesoresLista")

class profesoresmodificacion(LoginRequiredMixin,UpdateView):
    model = prof
    success_url = reverse_lazy("profesoresLista")
    fields = ["nombre", "apellido", "dni", "email"]
    template_name = "appcolegio/profesores_modificacion.html"

class profesoresborrar(LoginRequiredMixin,DeleteView):
    model = prof
    template_name = 'appcolegio/profesores_confirmacion_borrar.html'
    success_url = reverse_lazy("profesoresLista")


#ESTUDIANTES BASADO EN CLASES
def estudiantes(request):
    if request.method == "POST":
        miFormulario = cargarestu(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            estudiante = estu(nombre=informacion["nombre"], apellido=informacion["apellido"]
                         , dni=informacion["dni"], email=informacion["email"])
            estudiante.save()
            return render(request, "appcolegio/index.html")
    else:
        miFormulario = cargarestu()

    return render(request, "appcolegio/estudiantes.html", {"miFormulario": miFormulario})

class estudianteslista(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    model = estu
    template_name = "appcolegio/estudiantes_list.html"
    permission_required = 'appcolegio.view_estu'
    permission_denied_message = 'Usted no esta autorizado.'

class estudiantesdetalle(LoginRequiredMixin,DetailView):
    model = estu
    template_name = "appcolegio/estudiantes_detalle.html"
    
class estudiantescreate(LoginRequiredMixin,CreateView):
  
    model = estu
    template_name = "appcolegio/estudiantes_create.html"
    fields = ["nombre", "apellido", "dni", "email"]
    success_url = reverse_lazy("estudiantesLista")

class estudiantesmodificacion(LoginRequiredMixin,UpdateView):
    model = estu
    success_url = reverse_lazy("estudiantesLista")
    fields = ["nombre", "apellido", "dni", "email"]
    template_name = "appcolegio/estudiantes_modificacion.html"

class estudiantesborrar(LoginRequiredMixin,DeleteView):
    model = estu
    template_name = 'appcolegio/estudiantes_confirmacion_borrar.html'
    success_url = reverse_lazy("estudiantesLista")





#MATERIAS BASADO EN CLASES
def materias(request):
    if request.method == "POST":
        miFormulario = cargarmateria(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            materia = mate(nombre=informacion["nombre"], codigo=informacion["codigo"])
            materia.save()
            return render(request, "appcolegio/index.html")
    else:
        miFormulario = cargarmateria()

    return render(request, "appcolegio/materias.html", {"miFormulario": miFormulario})

class materiaslista(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    model = mate
    template_name = "appcolegio/materias_list.html"
    permission_required = 'appcolegio.view_mate'
    permission_denied_message = 'Usted no esta autorizado.'

class materiasdetalle(LoginRequiredMixin,DetailView):
    model = mate
    template_name = "appcolegio/materias_detalle.html"
    
class materiascreate(LoginRequiredMixin,CreateView):
  
    model = mate
    template_name = "appcolegio/materias_create.html"
    fields = ["nombre", "codigo"]
    success_url = reverse_lazy("materiasLista")

class materiasmodificacion(LoginRequiredMixin,UpdateView):
    model = mate
    success_url = reverse_lazy("materiasLista")
    fields = ["nombre", "codigo"]
    template_name = "appcolegio/materias_modificacion.html"

class materiasborrar(LoginRequiredMixin,DeleteView):
    model = mate
    template_name = 'appcolegio/materias_confirmacion_borrar.html'
    success_url = reverse_lazy("materiasLista")




# quienes somos

def quienesSomos(request):
    return render(request, "appcolegio/quienesSomos.html")






