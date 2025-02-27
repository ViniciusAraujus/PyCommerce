# Estrutura de dados para armazenar clientes e produtos
clientes = []
produtos = [
    {"id": 1, "nome": "Camiseta", "descricao": "Camiseta de algodão", "preco": 49.90, "estoque": 10},
    {"id": 2, "nome": "Tênis", "descricao": "Tênis esportivo", "preco": 199.90, "estoque": 5},
    {"id": 3, "nome": "Calça", "descricao": "Calça jeans", "preco": 89.90, "estoque": 8}
]

# Função para cadastrar um cliente
def cadastrar_cliente():
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    endereco = input("Digite seu endereço: ")
    cliente = {"nome": nome, "email": email, "endereco": endereco}
    clientes.append(cliente)
    print("Cadastro realizado com sucesso!")

# Função para exibir a lista de produtos
def listar_produtos():
    print("\nLista de Produtos:")
    for produto in produtos:
        print(f"ID: {produto['id']} | Nome: {produto['nome']} | Descrição: {produto['descricao']} | Preço: R${produto['preco']}")

# Função para selecionar um produto e calcular o total da compra
def realizar_compra():
    listar_produtos()
    produto_id = int(input("\nEscolha o ID do produto que deseja comprar: "))
    quantidade = int(input("Quantas unidades você deseja comprar? "))
    
    produto = next((p for p in produtos if p['id'] == produto_id), None)
    if produto:
        if produto['estoque'] >= quantidade:
            total = produto['preco'] * quantidade
            print(f"\nTotal da compra: R${total:.2f}")
            metodo_pagamento(total)
        else:
            print("Quantidade disponível insuficiente!")
    else:
        print("Produto não encontrado.")

# Função para escolher o método de pagamento
def metodo_pagamento(total):
    print("\nEscolha o método de pagamento:")
    print("1. Cartão de Crédito")
    print("2. Boleto Bancário")
    opcao = input("Escolha a opção (1 ou 2): ")
    
    if opcao == "1":
        print(f"\nPagamento de R${total:.2f} realizado com sucesso via Cartão de Crédito!")
    elif opcao == "2":
        print(f"\nPagamento de R${total:.2f} gerado com sucesso via Boleto Bancário!")
    else:
        print("\nOpção inválida.")

# Menu principal
def menu():
    while True:
        print("\n-- Menu E-Commerce --")
        print("1. Cadastrar Cliente")
        print("2. Realizar Compra")
        print("3. Sair")
        opcao = input("Escolha uma opção (1, 2 ou 3): ")
        
        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            realizar_compra()
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o sistema
menu()
