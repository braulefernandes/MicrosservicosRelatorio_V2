import requests
from django.shortcuts import render, redirect
from .models import RelatorioEstoque

def obter_estoque(request):
    url_estoque = "https://estoquepadaria-production-bf51.up.railway.app/estoque/todos"
    try:
        response = requests.get(url_estoque)
        response.raise_for_status()  # Gera uma exceção para códigos de status 4xx ou 5xx

        dados_estoque = response.json()

        # Atualiza o banco de dados com os dados da API
        for item in dados_estoque:
            RelatorioEstoque.objects.update_or_create(
                id_produto=item['idProduto'],
                defaults={
                    'nome': item['nome'],
                    'valor_unitario': item['valorUnitario'],
                    'quantidade': item['quantidade'],
                    'descricao': item['descricao'],
                    'categoria': item['categoria'],
                }
            )
    except requests.exceptions.RequestException as e:
        # Log de erro ou mensagem para o desenvolvedor
        print(f"Erro ao acessar a API: {e}")
        dados_estoque = []  # Define uma lista vazia em caso de erro

    # Renderiza o template ou redireciona para o relatório atualizado
    return redirect('relatorio_estoque')


# Página inicial
def home(request):
    return render(request, 'home.html')

# Página de relatório de estoque
def relatorio_estoque(request):
    # Obtém os dados de estoque do banco de dados
    produtos = RelatorioEstoque.objects.all()
    return render(request, 'relatorio_estoque.html', {'produtos': produtos})

