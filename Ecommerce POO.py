class Cliente:
    def __init__(self, nome, email, endereco):
        self.nome = nome
        self.email = email
        self.endereco = endereco

    def exibir_cliente(self):
        return f"Nome: {self.nome} | E-mail: {self.email} | Endereço: {self.endereco}"


class Produto:
    def __init__(self, id, nome, descricao, preco, estoque):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque

    def exibir_produto(self):
        return f"ID: {self.id} | {self.nome} - {self.descricao} | Preço: R${self.preco:.2f} | Estoque: {self.estoque}"


class Pedido:
    def __init__(self, cliente, produto, quantidade):
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.total = produto.preco * quantidade

    def processar_pagamento(self, metodo):
        if metodo == "1":
            return f"Pagamento de R${self.total:.2f} realizado via Cartão de Crédito."
        elif metodo == "2":
            return f"Pagamento de R${self.total:.2f} realizado via Boleto Bancário."
        else:
            return "Método de pagamento inválido."


# Lista de Produtos
produtos = [
    Produto(1, "Camiseta", "Camiseta de algodão", 49.90, 10),
    Produto(2, "Tênis", "Tênis esportivo", 199.90, 5),
    Produto(3, "Calça", "Calça jeans", 89.90, 8)
]

# Lista de Clientes
clientes = []


# Funções auxiliares
def cadastrar_cliente():
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    endereco = input("Digite seu endereço: ")
    cliente = Cliente(nome, email, endereco)
    clientes.append(cliente)
    print("Cadastro realizado com sucesso!")


def listar_produtos():
    print("\nLista de Produtos:")
    for produto in produtos:
        print(produto.exibir_produto())


def realizar_compra():
    listar_produtos()
    produto_id = int(input("\nEscolha o ID do produto que deseja comprar: "))
    quantidade = int(input("Quantas unidades deseja comprar? "))

    produto = next((p for p in produtos if p.id == produto_id), None)
    
    if produto and produto.estoque >= quantidade:
        nome_cliente = input("\nDigite seu nome para associar ao pedido: ")
        cliente = next((c for c in clientes if c.nome == nome_cliente), None)

        if not cliente:
            print("Cliente não encontrado! Faça o cadastro primeiro.")
            return
        
        pedido = Pedido(cliente, produto, quantidade)
        print(f"\nTotal da compra: R${pedido.total:.2f}")
        
        print("\nEscolha o método de pagamento:")
        print("1. Cartão de Crédito")
        print("2. Boleto Bancário")
        opcao_pagamento = input("Escolha a opção (1 ou 2): ")
        
        print(pedido.processar_pagamento(opcao_pagamento))
        produto.estoque -= quantidade  # Atualiza o estoque
    else:
        print("Produto não encontrado ou estoque insuficiente.")


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
