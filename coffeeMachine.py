from os import system, name
import time

def limpaTela():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def somarLista(a, b):
    for i in range(len(a)):
        a[i] = a[i] + b[i]

def subtrairLista(a, b):
    for i in range(len(a)):
        a[i] = a[i] - b[i]

def digitarIntPositivo():
    try:
        val = int(input())
        if val >= 0:
            return val
        else:
            print("Parâmetro inválido!")
    except:
        print("Parâmetro inválido!")

def prepararBebida():
    print("Sua bebida está sendo preparada")
    for i in range(3):
        time.sleep(1)
        print(".")
    time.sleep(1)
    print("Sua bebida está pronta!")

def somarDinheiro(listaVal, listaDinCliente):
    din = 0
    for i in range(12):
        while True:
            if i <= 5:
                print(f"Digite quantas notas de R$ {listaVal[i]}: ",end="")
            else:
                print(f"Digite quantas moedas de R$ {listaVal[i]}: ",end="")
            val = digitarIntPositivo()
            if val != None:
                if val >= 0:
                    listaDinCliente[i] = val
                    break

def dinCliente(listaVal, listaDinCliente):
    din = 0
    for i in range(len(listaDinCliente)):
        din = din + listaDinCliente[i] * listaVal[i]
    return din

def verificarCaixa(troco, listaVal, listaDin, listaDinCliente):
    somarLista(listaDin, listaDinCliente)
    listaAux = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    while troco != 0:
        if i > 11:
            somarLista(listaDin, listaAux)
            return 0
        elif listaDin[i] == 0 or (troco - listaVal[i]) < 0:
            i = i + 1
        else:
            troco = round(troco - listaVal[i], 2)
            listaDin[i] = listaDin[i] - 1
            listaAux[i] = listaAux[i] + 1
    somarLista(listaDin, listaAux)
    subtrairLista(listaDin, listaDinCliente)
    return 1

def darTroco(troco, listaVal, listaDin, listaDinCliente):
    i = 0
    print("Acompanhe seu troco: ")
    while troco != 0:
        if i > 11:
            break
        elif listaDin[i] == 0 or (troco - listaVal[i]) < 0:
            i = i + 1
        else:
            print(f"R$ {listaVal[i]}")
            troco = round(troco - listaVal[i], 2)
            listaDin[i] = listaDin[i] - 1

def vendaDoProduto(din, valorProd, listaVal, listaDin, listaDinCliente):
    if din >= valorProd and verificarCaixa(din - valorProd, listaVal, listaDin, listaDinCliente) == 1:
        din = din - valorProd
        somarLista(listaDin, listaDinCliente)
        listaDinCliente = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        prepararBebida()
        
        res = input(f"Restam R$ {din}. Deseja comprar outra bebida? S/N: ")
        if res == "S" or res == "s":
            print()
            vendaDoProduto(din, valorProd, listaVal, listaDin, listaDinCliente)
            # Função que levará para os produtos
        elif din > 0:
            darTroco(din, listaVal, listaDin, listaDinCliente)
        else:
            print("Você não possui troco")
            print("Volte sempre!")
    else:
        print("Dinheiro insuficiente!")
        if din > 0:
            darTroco(din, listaVal, listaDin, listaDinCliente)
        else:
            print("Você não possui troco")
            print("Volte sempre!")
        
def venda(din, valorProd, listaVal, listaDin, listaDinCliente):
    somarDinheiro(listaVal, listaDinCliente)
    din = din + dinCliente(listaVal, listaDinCliente)
    vendaDoProduto(din, valorProd, listaVal, listaDin, listaDinCliente)
    
def main():
    limpaTela()


    listaVal = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
    listaDin = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    listaDinCliente = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    din = 0
    valorProd = 2.5


    venda(din, valorProd, listaVal, listaDin, listaDinCliente)

main()