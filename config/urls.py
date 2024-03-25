from django.contrib import admin
from django.urls import path, include
from appcolegio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name= "inicio"),
    path('AppColegio/', include('appcolegio.urls')),
    path('users/', include('users.urls'))
]