from django.urls import path
from appcolegio import views

urlpatterns = [
    path('', views.inicio, name= "inicio"),
     path('buscar/', views.buscarCurso, name="buscarCurso"),
     path('quienes-somos/', views.quienesSomos, name="quienesSomos")
]

#CURSOS
urlpatterns += [
    path('cursos/', views.cursos, name= "cursos"),

    path('curso_list/', views.cursolista.as_view(), name="cursoLista"),

    path('curso-detail/<int:pk>/', views.cursodetalle.as_view(), name="crusoDetalle"),

    path('curso-create/', views.cursocreate.as_view(), name="cursoCreate"),

    path('curso-update/<int:pk>/', views.cursomodificacion.as_view(), name="cursoModificacion"),

    path('curso-delete/<int:pk>/', views.cursoborrar.as_view(), name="cursoDelete"),

    
]


#ESTUDIANTES
urlpatterns += [
    path('estudiantes/', views.estudiantes, name= "estudiantes"),

    path('estudiantes_list/', views.estudianteslista.as_view(), name="estudiantesLista"),

    path('estudiantes-detail/<int:pk>/', views.estudiantesdetalle.as_view(), name="estudiantesDetalle"),

    path('estudiantes-create/', views.estudiantescreate.as_view(), name="estudiantesCreate"),

    path('estudiantes-update/<int:pk>/', views.estudiantesmodificacion.as_view(), name="estudiantesModificacion"),

    path('estudiantes-delete/<int:pk>/', views.estudiantesborrar.as_view(), name="estudiantesDelete"),
]

#PROFESORES
urlpatterns += [
    path('profesores/', views.estudiantes, name= "profesores"),

    path('profesores_list/', views.profesoreslista.as_view(), name="profesoresLista"),

    path('profesores-detail/<int:pk>/', views.profesoresdetalle.as_view(), name="profesoresDetalle"),

    path('profesores-create/', views.profesorescreate.as_view(), name="profesoresCreate"),

    path('profesores-update/<int:pk>/', views.profesoresmodificacion.as_view(), name="profesoresModificacion"),

    path('profesores-delete/<int:pk>/', views.profesoresborrar.as_view(), name="profesoresDelete"),
]

#MATERIAS
urlpatterns += [
    path('materias/', views.estudiantes, name= "materias"),

    path('materias_list/', views.materiaslista.as_view(), name="materiasLista"),

    path('materias-detail/<int:pk>/', views.materiasdetalle.as_view(), name="materiasDetalle"),

    path('materias-create/', views.materiascreate.as_view(), name="materiasCreate"),

    path('materias-update/<int:pk>/', views.materiasmodificacion.as_view(), name="materiasModificacion"),

    path('materias-delete/<int:pk>/', views.materiasborrar.as_view(), name="materiasDelete"),
]