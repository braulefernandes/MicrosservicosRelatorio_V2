from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('relatorio_estoque/', views.relatorio_estoque, name='relatorio_estoque'),  # Página de relatório de estoque
    path('relatorio_vendas/', views.relatorio_vendas, name='relatorio_vendas'),  # Página de relatório de vendas
    path('obter_estoque/', views.obter_estoque, name='obter_estoque'),
    path('obter_vendas/', views.obter_vendas, name='obter_vendas'),  # Nova URL para obter vendas
]