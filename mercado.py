import os
from time import sleep
from sys import exit

#Menu
def menu():
    print("="*30)
    print(f'{"Bem-Vindo ao Menu inicial":^30}')
    print("="*30)
    sleep(1)
    user = usuario()
    os.system('cls')
    if user == "Administrador":
        menu_adm()
    elif user == "Cliente":
        menu_cliente()

#Estoque
def estoque():
    mercadoria = ['Pão', 'Café', 'Biscoito', 'Açúcar', 'Leite']
    quant = [50, 15, 20, 30, 30]
    preco = [0.40, 23.90, 5.00, 4.00, 6.99]
    return mercadoria, quant, preco

#Varável usada para exibir a tabela
produto, quantidade, preco = estoque()

def exibir_estoque(merc, quantidade, preco):
    print("="*35)
    print(f'{"Padaria Pedaço do céu":^35}')
    print("="*35)
    print(f"{'uni':<5}" + f"{'Produto':<20}" + f"{'Valor'}")
    print("="*35)
    for a, b, c in zip(merc, quantidade, preco):
        print(f"{b:<5} {a:<15} R$ {c:>6.2f}")
        print("="*35)

#Usuário
def usuario():
    user = ""
    escolha = 0
    while escolha not in (1,2,3):
        escolha = int(input("Você que entrar como \n[1]Cliente \n[2]Administrador \n[3]sair \n->"))
    match escolha:
        case 1:
            user = "Cliente"
        case 2:
            user = "Administrador"
        case 3:
            user = ""
            saida()
    return user

#Menu para os clientes
def menu_cliente():
    escolha = 0
    while escolha not in (1,2,3):
            escolha = int(input("Você deseja \n[1]Comprar \n[2]sair \n->"))
            os.system("cls")
    match escolha:
        case 1:
            compra()
        case 2:
            saida()

#Área de compra para o cliente
def compra():
        while True:
            exibir_estoque(produto, quantidade, preco)
            mercadoria = input("Digite o nome do produto que deseja: \n->").capitalize()
            disponivel, quantia, valor, local = verificacao_produto(mercadoria)
            if disponivel == True:
                break
            else:
                print("Produto não encontrado! Tente novamente")
                sleep(1)
                os.system("cls")
                continue
        while True:
            unidades = int(input("Quantas unidades você quer? \n->"))
           
            if verificacao_quantidade(unidades, quantia) == True:
                break
            else:
                print("Quantia inválida!")
        sleep(1)
        os.system('cls')
        print(f"O valor do produto é R$ {valor}")
        preco_final, desconto = pagamento(valor, unidades)
        print(f"O valor final ficou com {desconto}, ficou no total R$ {preco_final:.2f}")
        confimarpagamento = confimar_pagamento()
        if confimarpagamento == True:
            atualizar_estoque_cliente(local, unidades)
            relatorio(mercadoria, preco_final, unidades)

#verificar se tem
def verificacao_produto(nomedoproduto):
    mercadorias = produto
    if nomedoproduto in mercadorias:
        local = produto.index(nomedoproduto)
        indice = quantidade[local]
        valor = preco[local]
        verificacao = True
    else:
        local = None
        valor = 0
        indice = 0
        verificacao = False
    return verificacao, indice, valor, local

#verificar quantidade
def verificacao_quantidade(unidades, local):
    if unidades <= local:
        verificao = True
    else:
        verificao = False
    return verificao

#calcular o pagamento
def pagamento(preco, quantidade):
    valor_total_produto = preco * quantidade
    while True:
        print("[1]Dinheiro \n[2]Débito \n[3]Cartão de crédito ")    
        opcao = int(input("->"))
        if opcao in [1,2,3]:
            match opcao:
                case 1:
                    preco_final = valor_total_produto-(valor_total_produto*0.10)
                    desconto = "desconto de 10%"
                    break
                case 2:
                    preco_final = valor_total_produto-(valor_total_produto*0.10)
                    desconto = "desconto de 10%"
                    break
                case 3:
                    print("Deseja parcelar em quantas vezes: \n[1] A vista \n[2] x2 vezes \n[3] x3 vezes")
                    parcelas = int(input("->"))
                    match parcelas:
                        case 1:
                            preco_final = valor_total_produto
                            desconto = "sem juros ou desconto"
                            break
                        case 2:
                            preco_final = valor_total_produto+(valor_total_produto*0.05) 
                            desconto = f"juros de 5%, duas parcelas de R$ {preco_final/2:.2f}"
                            break
                        case 3:
                            preco_final = valor_total_produto+(valor_total_produto*0.10)
                            desconto = f"juros de 10%, três parcelas de R$ {preco_final/3:.2f}"
                            break
                        case _:
                            print("Opção inválida!!!")
                            preco_final = None
                            desconto = None
                case _:
                    print("Opção inválida!!!")
                    preco_final = None
                    desconto = None
        else:
            print("Opção inválida")
    sleep(0.5)
    os.system('cls')
    return preco_final, desconto

#confirmar pagamento
def confimar_pagamento():
    while True:
        sn = input("Confimar pagamento? [S/N]").strip().upper()
        if sn == "S":
            print("Pagamento confirmado!!!")
            return True
        elif sn == "N":
            print("Pagamento cancelado!!!")
            return False

        print("Opção inválida!!!")

relatorio_de_compras = []
def relatorio(nome_do_produto, valor_do_produto,quantidade_de_produto):
    listavazia = []
    if nome_do_produto in produto:
        listavazia.append(nome_do_produto)
        listavazia.append(valor_do_produto)
        listavazia.append(quantidade_de_produto)
        relatorio_de_compras.append(listavazia[:])
        listavazia.clear()

#atualização de estoque caso o cliente compre
def atualizar_estoque_cliente(indice, quantia):
    if quantidade[indice] > 0:
        novo_valor = quantidade[indice] - quantia
        quantidade[indice] = novo_valor

#Saída do sistema
def saida():
    print("Saindo...")
    sleep(1.5)
    exit()

def menu_adm():
    opcoes = int(input("Você deseja \n[1]Atualizar o estoque \n[2]Atualizar preço do produto \n[3]Relatório de compras \n[4]sair \n->"))
    match opcoes:
        case 1:
            atualizar_estoque_adm()
        case 2:
            atualizar_preco_adm()
        case 3:
            mostrar_relatorio()
        case 4:
            saida()
        case _:
            print("Escolha inválida!!!")

def atualizar_estoque_adm():
    exibir_estoque(produto, quantidade, preco)
    while True:
        mercadoria = input("Qual produto você quer atualizar o estoque: \n->").strip().capitalize()
        if mercadoria in produto:
            unidades = int(input("Quer atualizar o estoque para quanto: "))
            for mercad in produto:
                if mercadoria == mercad:
                    pos = produto.index(mercad)
                    if quantidade[pos] > 0:
                        novo_valor = unidades
                        quantidade[pos] = novo_valor
                    else:
                        pass
                    exibir_estoque(produto, quantidade, preco)
                    print("Novo estoque atualizado!!!")

            break
        else:
            print("Produto não encontrado!!!")
        

def atualizar_preco_adm():
    exibir_estoque(produto, quantidade, preco)
    while True:
        mercadoria = input("Qual produto você quer atualizar o preço: \n->").strip().capitalize()
        if mercadoria in produto:
            valor = float(input("Quer atualizar o preço para quanto: "))
            for mercad in produto:
                if mercadoria == mercad:
                    pos = produto.index(mercad)
                    print(pos, valor)
                    print("Certooooo!!!")
                    if quantidade[pos] > 0:
                        novo_valor = valor
                        preco[pos] = novo_valor
                    else:
                        pass
                    exibir_estoque(produto, quantidade, preco)
                    print("Novo preço atualizado!!!")

            break
        else:
            print("Produto não encontrado!!!")

def mostrar_relatorio():
    print(f"{"RELATÓRIO DE COMPRAS":.^40}")
    print(f"{"Produto":<10}", f"{"Quantidade":>15}" f"{"Valor":>15}")
    print("="*40)
    for p in (relatorio_de_compras):
        print(f'{f"{p[0]}":<10}', f"{f"{p[2]}":>10}" f'{f"R$ {p[1]:.2f}":>20}')
    totalpreco = totalunidades = 0
    for t in relatorio_de_compras:
        totalpreco += (t[1])
        totalunidades += (t[2])
    print("="*40)
    print(f"Produtos vendidos: {totalunidades}")
    print(f"Valor Total: R$ {totalpreco:.2f}")

while True:
    menu()