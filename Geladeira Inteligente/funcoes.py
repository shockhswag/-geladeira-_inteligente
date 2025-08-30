import dados
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[H\033[J", end="")

def listar_produtos():
    for produto in dados.produtos:
        print(f"{produto['nome']} - {produto['quantidade']} unidades")

def cadastrar_produto(nome, quantidade):
    dados.produtos.append({'nome': nome, 'quantidade': quantidade})

def registrar_venda(nome, quantidade):
    dados.vendas.append({'nome': nome, 'quantidade': quantidade})
    for produto in dados.produtos:
        if produto['nome'] == nome:
            produto['quantidade'] -= quantidade
            break

def relatorio_de_vendas():
    for venda in dados.vendas:
        print(f"{venda['nome']} - {venda['quantidade']} unidades vendidas")
    total = sum(venda['quantidade'] for venda in dados.vendas)
    print(f"Total de unidades vendidas: {total}")