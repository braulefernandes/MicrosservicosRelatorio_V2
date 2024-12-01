from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Acesso ao painel de administração
    path('', include('relatorios.urls')),  # Rotas públicas do app 'relatorios'
]
