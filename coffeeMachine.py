from os import system, name
import time

def limpaTela():
    '''
    Função que limpa a tela do terminal

    Esta função verifica qual o sistema operacional usado e limpa a tela do terminal com base nessa informação
    '''
    if name == "nt":
        system("cls")
    else:
        system("clear")

def somarLista(a, b):
    '''
    Função que soma duas listas

    Esta função recebe duas listas, verifica o tamanho da primeira e soma termo a termo com a segunda

    Argumentos:
        a (lista): A primeira lista que terá seus valores acrescidos
        b (lista): A segunda lista que terá seus valores somados a primeira
    '''
    for i in range(len(a)):
        a[i] = a[i] + b[i]

def subtrairLista(a, b):
    '''
    Função que subtrai duas listas

    Esta função recebe duas listas, verifica o tamanho da primeira e subtrai termo a termo com a segunda

    Argumentos:
        a (lista): A primeira lista que terá seus valores decrescidos
        b (lista): A segunda lista que terá seus valores subtraidos a primeira
    '''
    for i in range(len(a)):
        a[i] = a[i] - b[i]

def digitarIntPositivo():
    '''
    Função que verifica o valor digitado e retorna se for inteiro positivo

    Esta função verifica se o valor digitado é um inteiro positivo, se não for, exibe uma mensagem, se for, retorna o valor

    Retorna:
        int: val (se o valor for inteiro positivo)
        None: se o valor não for inteiro positivo
    '''
    try:
        val = int(input())
        if val >= 0:
            return val
        else:
            print("Parâmetro inválido!")
    except:
        print("Parâmetro inválido!")

def prepararBebida():
    '''
    Função que prepara a bebida do cliente

    Esta função exibe uma mensagem que a bebida do cliente que está sendo preparada e outra que a bebida está pronta
    '''
    print("Sua bebida está sendo preparada")
    for i in range(3):
        time.sleep(1)
        print(".")
    time.sleep(1)
    print("Sua bebida está pronta!")

def somarDinheiro(listaVal, listaDinCliente):
    '''
    Função que recebe dinheiro do cliente

    Esta função recebe duas listas, pergunta quantas notas ou moedas foram inseridas de cada valor correspondente as posições da primeira lista e armazena essa quantidade na segunda lista. 
    Chama função digitarIntPositivo para verificar se o número é um inteiro positivo
    
    Argumentos:
        listaVal (lista): Lista que contém os valores das notas e das moedas
        listaDinCliente (lista): Lista que armazenará a quantidade de dinheiro do cliente
    '''
    for i in range(12):
        while True:
            if i <= 5:
                print(f"Digite a quantidade de notas de R$ {listaVal[i]}: ",end="")
            else:
                print(f"Digite a quantidade de moedas de R$ {listaVal[i]}: ",end="")
            val = digitarIntPositivo()
            if val != None:
                if val >= 0:
                    listaDinCliente[i] = val
                    break

def dinCliente(listaVal, listaDinCliente):
    '''
    Função que calcula o dinheiro do cliente

    Esta função recebe duas lista, a primeira com o valor de cada nota e moeda, a segunda com a quantidade que o cliente tem de cada um desses valores. 
    Depois multiplica termo a termo a primeira pela segunda e soma a uma variável com o total

    Argumentos:
        listaVal (lista): Lista que contém os valores das notas e das moedas
        listaDinCliente (lista): Lista com a quantidade de dinheiro do cliente

    Retorna:
        float: A soma de todo dinheiro do cliente
    '''
    din = 0
    for i in range(len(listaDinCliente)):
        din = din + listaDinCliente[i] * listaVal[i]
    return din

def verificarCaixa(troco, listaVal, listaCaixa, listaDinCliente):
    '''
    Função que verifica se tem dinheiro para troco no caixa da máquina

    Esta função recebe o valor do troco que tem que dar para o cliente e mais 3 listas.
    Chama a função somarLista para colocar o dinheiro do cliente no caixa da empresa.
    Faz a verificação termo a termo da lista do caixa para dar o troco para o cliente.
    Volta a lista do caixa ao normal. E se tiver troco, retorna True, se não, retorna False

    Argumentos:
        troco (float): Valor a ser verificado se tem troco no caixa
        listaVal (lista): Lista que contém os valores das notas e das moedas
        listaCaixa (lista): Lista que contém a quantidade de notas e moedas no caixa da máquina
        listaDinCliente (lista): Lista que contém a quantidade de dinheiro do cliente

    Retorna:
        bool: True se tiver dinheiro no caixa, False se não tiver dinheiro no caixa
    '''
    somarLista(listaCaixa, listaDinCliente)
    listaAux = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    while troco != 0:
        if i >= 12:
            somarLista(listaCaixa, listaAux)
            subtrairLista(listaCaixa, listaDinCliente)
            return False
        elif listaCaixa[i] == 0 or (troco - listaVal[i]) < 0:
            i = i + 1
        else:
            troco = round(troco - listaVal[i], 2)
            listaCaixa[i] = listaCaixa[i] - 1
            listaAux[i] = listaAux[i] + 1
    somarLista(listaCaixa, listaAux)
    subtrairLista(listaCaixa, listaDinCliente)
    return True

def darTroco(troco, listaVal, listaCaixa):
    '''
    Função que dá o troco pra o cliente

    Esta função recebe a quantidade de troco que deve ser dado ao cliente, imprime esses valores, nota por nota e centavo por centavo.
    Retira a mesma quantidade de nota e moedas do caixa

    Argumentos:
        troco (float): Valor que precisa dar de troco ao cliente
        listaVal (lista): Lista que contém os valores das notas e das moedas
        listaCaixa (lista): Lista que contém a quantidade de notas e moedas no caixa da máquina
    '''
    i = 0
    print("Acompanhe seu troco: ")
    while troco != 0:
        if i > 11:
            break
        elif listaCaixa[i] == 0 or (troco - listaVal[i]) < 0:
            i = i + 1
        else:
            print(f"R$ {listaVal[i]}")
            troco = round(troco - listaVal[i], 2)
            listaCaixa[i] = listaCaixa[i] - 1

def vendaDoProduto(din, valorProd, listaVal, listaCaixa, listaDinCliente):
    if din >= valorProd and verificarCaixa(din - valorProd, listaVal, listaCaixa, listaDinCliente) == True:
        din = din - valorProd
        somarLista(listaCaixa, listaDinCliente)
        listaDinCliente = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        prepararBebida()
        
        res = input(f"Restam R$ {din}. Deseja comprar outra bebida? S/N: ")
        if res == "S" or res == "s":
            print()
            vendaDoProduto(din, valorProd, listaVal, listaCaixa, listaDinCliente)
            # Função que levará para os produtos
        elif din > 0:
            darTroco(din, listaVal, listaCaixa)
        else:
            print("Você não possui troco")
            print("Volte sempre!")
    else:
        print("Dinheiro insuficiente!")
        if din > 0:
            darTroco(din, listaVal, listaCaixa)
        else:
            print("Você não possui troco")
            print("Volte sempre!")
        
def venda(din, valorProd, listaVal, listaCaixa, listaDinCliente):
    somarDinheiro(listaVal, listaDinCliente)
    din = din + dinCliente(listaVal, listaDinCliente)
    vendaDoProduto(din, valorProd, listaVal, listaCaixa, listaDinCliente)
    
def main():
    limpaTela()


    listaVal = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
    listaCaixa = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    listaDinCliente = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    din = 0
    valorProd = 2.5

    
    # venda(din, valorProd, listaVal, listaCaixa, listaDinCliente)

main()