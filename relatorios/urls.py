from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('relatorio_estoque/', views.relatorio_estoque, name='relatorio_estoque'),  # Página de relatório
    path('obter_estoque/', views.obter_estoque, name='obter_estoque'),
]
