import os
from time import sleep

#Menu
def menu():
    print("="*30)
    print(f'{"Bem-Vindo ao Menu inicial":^30}')
    print("="*30)
    sleep(1)
    user = usuario()
    os.system('cls')
    if user == "Administrador":
        pass
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
            pass

#Área de compra para o cliente
def compra():
        while True:
            exibir_estoque(produto, quantidade, preco)
            mercadoria = input("Digite o nome do produto que deseja: \n->").capitalize()
            disponivel, quantia, valor = verificacao_produto(mercadoria)
            if disponivel == True:
                break
            else:
                print("Produto não encontrado! Tente novamente")
                sleep(1)
                os.system("cls")
                continue
        while True:
            unidades = int(input("Quantas unidades você quer? \n->"))
            uni = verificacao_quantidade(unidades, quantia)
            if uni == True:
                break
            else:
                print("Quantia inválida!")

        sleep(1)
        os.system('cls')
        print(f"O valor do produto é R$ {valor}")
        preco_final, desconto = pagamento(valor, unidades)
        print(f"O valor final ficou com {desconto} R$ {preco_final:.2f}")
        

#verificar se tem
def verificacao_produto(produto):
    mercadorias = estoque()[0]
    if produto in mercadorias:
        local = estoque()[0].index(produto)
        indice = estoque()[1][local]
        preco = estoque()[2][local]
        verificacao = True
    else:
        preco = 0
        indice = 0
        verificacao = False
    return verificacao, indice, preco

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
                case 2:
                    preco_final = valor_total_produto-(valor_total_produto*0.10)
                    desconto = "desconto de 10%"
                case 3:
                    preco_final = valor_total_produto
                    pass
            break
        else:
            print("Opção inválida")
    sn = ""
    while sn not in "SN":
        sn = input("Confimar pagamento? [S/N]").upper()
        if sn == "S":
            break
        if sn == "N":
            pass
    return preco_final, desconto

compra()