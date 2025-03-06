# PyCommerce
Simulação de E-commerce em Python

Este é um programa simples de e-commerce desenvolvido em Python. Ele permite que os clientes se cadastrem, visualizem produtos e realizem compras, com a opção de pagamento via Cartão de Crédito ou Boleto Bancário. O código foi projetado para aplicar os conceitos fundamentais de um sistema de compras online, utilizando manipulação de dados em memória (sem integração com banco de dados) e interação por meio do terminal.

Funcionalidades

1. Cadastro de Clientes: O programa permite que os clientes se cadastrem informando nome, e-mail e endereço. Após o cadastro, o cliente será adicionado à lista de clientes.

2. Exibição de Produtos: A lista de produtos disponíveis para venda é exibida com informações como ID, nome, descrição, preço e quantidade disponível em estoque.

3. Realização de Compras: O cliente pode escolher um produto, informar a quantidade desejada e o sistema calcula o valor total da compra. Caso o estoque seja suficiente, a compra prossegue para a escolha do método de pagamento.

4. Método de Pagamento: O cliente pode escolher entre duas formas de pagamento:

 - Cartão de Crédito: O pagamento será realizado diretamente.
 - Boleto Bancário: Um boleto será gerado.

5. Menu de Navegação: O programa oferece um menu com as opções de cadastrar cliente, realizar compras ou sair do sistema.

Estrutura do Código

 - Clientes: Lista que armazena os dados dos clientes cadastrados.
 - Produtos: Lista de produtos disponíveis para venda. Cada produto é representado por um dicionário com informações como ID, nome, descrição, preço e quantidade em estoque.

Funções principais:

- Cadastrar_cliente: Permite o cadastro de novos clientes.
- Listar_produtos: Exibe os produtos disponíveis para compra.
- Realizar_compra: Lida com o processo de compra de produtos, verificando estoque e calculando o valor total.
- Metodo_pagamento: Processa o pagamento, oferecendo duas opções: Cartão de Crédito ou Boleto Bancário.
- Menu: Controla o fluxo do programa, exibindo as opções e executando as funções apropriadas.

Observações
- O programa mantém os dados dos clientes e produtos em memória durante a execução, portanto, após o programa ser fechado, as informações são perdidas.
- A validação de entradas de dados é simples, sem verificação de erros complexos (como e-mails ou endereços inválidos).
- Não há integração com bancos de dados ou sistemas externos de pagamento.
