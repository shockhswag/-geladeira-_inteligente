import dados
import funcoes
import os

sair_do_programa = False

while not sair_do_programa:
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    usuario_encontrado = False
    for usuario_dict in dados.usuarios:
        if usuario in usuario_dict and usuario_dict[usuario] == senha:
            usuario_encontrado = True
            break
    if usuario_encontrado:
        print("Login bem-sucedido!")

        while True:
            print("\n1. Cadastrar um novo produto")
            print("2. Listar produtos")
            print("3. Registrar venda")
            print("4. Relatório de vendas")
            print("5. Sair")
        
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                funcoes.limpar_tela()
                nome_produto = input('Digite o nome do produto que quer cadastrar: ')
                if len(nome_produto.strip()) == 0:
                    print('Erro: O nome do produto não pode estar vazio!')
                else:
                    try:
                        quantidade_produto = int(input('Digite a quantidade de produtos que quer cadastrar: '))
                        if quantidade_produto < 0:
                            print('Erro: A quantidade não pode ser negativa!')
                        else:
                            for produto in dados.produtos:
                                if produto['nome'] == nome_produto:
                                    produto['quantidade'] += quantidade_produto
                                    print(f'Quantidade atualizada! {nome_produto} agora tem {produto["quantidade"]} unidades.')
                                    break
                            else:
                                funcoes.cadastrar_produto(nome_produto, quantidade_produto)
                                print('Produto cadastrado com sucesso!')
                    except ValueError:
                        print('Erro: Digite um número válido para a quantidade!')

            elif opcao == '2':
                funcoes.limpar_tela()
                funcoes.listar_produtos()

            elif opcao == '3':
                funcoes.limpar_tela()
                nome_da_venda = input('Digite o nome do produto vendido: ')
                if len(nome_da_venda.strip()) == 0:
                    print('Erro: O nome do produto não pode estar vazio!')
                else:
                    try:
                        quantidade_da_venda = int(input('Digite a quantidade do produto vendido: '))
                        if quantidade_da_venda <= 0:
                            print('Erro: A quantidade deve ser maior que zero!')
                        else:
                            for produto in dados.produtos:
                                    if produto['nome'] == nome_da_venda:
                                        if produto['quantidade'] >= quantidade_da_venda:
                                            funcoes.registrar_venda(nome_da_venda, quantidade_da_venda)
                                            print('Venda registrada com sucesso!')
                                        else:
                                            print(f'Erro: Estoque insuficiente! Disponível: {produto["quantidade"]} unidades.')
                                        break
                            else:
                                print('Erro: Produto não encontrado!')
                    except ValueError:
                        print('Erro: Digite um número válido para a quantidade!')
            elif opcao == '4':
                funcoes.limpar_tela()
                if dados.vendas:
                    funcoes.relatorio_de_vendas()
                else:
                    print('Não foram feito vendas!')

            elif opcao == '5':
                sair_do_programa = True
                break
    else:
        print("Usuário ou senha inválidos.")

print('Sistema encerrado!')