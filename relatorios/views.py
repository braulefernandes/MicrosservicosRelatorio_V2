import requests
from django.shortcuts import render, redirect
from .models import RelatorioEstoque, RelatorioVenda, ItemVenda

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


def obter_vendas(request):
    url_vendas = "https://vendasmicroservice-production.up.railway.app/vendas"
    try:
        response = requests.get(url_vendas)
        response.raise_for_status()  # Gera uma exceção para códigos de status 4xx ou 5xx

        dados_vendas = response.json().get('vendas', [])

        # Processa os dados das vendas
        for venda in dados_vendas:
            # Cria ou atualiza a venda
            venda_obj, created = RelatorioVenda.objects.update_or_create(
                id_venda=venda['id_venda'],
                defaults={
                    'valor_total': venda['valor_total'],
                    'data_venda': venda['data_venda'],
                }
            )

            # Processa os itens de cada venda
            for item in venda['produtos']:
                ItemVenda.objects.update_or_create(
                    venda=venda_obj,
                    produto_id=item['id_produto'],
                    defaults={
                        'quantidade': item['quantidade'],
                        'valor_unitario': item['valor_unitario'],
                    }
                )

    except requests.exceptions.RequestException as e:
        # Log de erro ou mensagem para o desenvolvedor
        print(f"Erro ao acessar a API de vendas: {e}")
        dados_vendas = []  # Define uma lista vazia em caso de erro

    # Redireciona para a página de vendas (ou outra página de sua escolha)
    return redirect('relatorio_vendas')

def relatorio_vendas(request):
    # Obtém todas as vendas registradas no banco de dados
    vendas = RelatorioVenda.objects.all()
    return render(request, 'relatorio_vendas.html', {'vendas': vendas})


