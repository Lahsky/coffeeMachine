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

def prepararBebida(prodCliente):
    '''
    Função que prepara a bebida do cliente

    Esta função exibe uma mensagem que a bebida do cliente que está sendo preparada e outra que a bebida está pronta
    '''
    prodCliente[4] = prodCliente[4] + 1
    print("Sua bebida está sendo preparada")
    for i in range(3):
        time.sleep(1)
        print(".")
    time.sleep(1)
    print(f"Seu {prodCliente[1]} está pronto!")
    print()

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
    print()

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
    Função que dá o troco para o cliente

    Esta função recebe a quantidade de troco que deve ser dado ao cliente, imprime esses valores, nota por nota e centavo por centavo.
    Retira a mesma quantidade de nota e moedas do caixa

    Argumentos:
        troco (float): Valor que precisa dar de troco ao cliente
        listaVal (lista): Lista que contém os valores das notas e das moedas
        listaCaixa (lista): Lista que contém a quantidade de notas e moedas no caixa da máquina
    '''
    i = 0
    print()
    print("Acompanhe seu troco: ")
    while troco != 0:
        if i > 11:
            break
        elif listaCaixa[i] == 0 or (troco - listaVal[i]) < 0:
            i = i + 1
        else:
            print(f"R$ {listaVal[i]:.2f}")
            troco = round(troco - listaVal[i], 2)
            listaCaixa[i] = listaCaixa[i] - 1
            time.sleep(0.1)

def verificaTam():
    while True:
        tam = input("Digite o tamanho da sua bebida P / M / G: ")
        if tam == "P" or tam == "p":
            return 1
        elif tam == "M" or tam == "m":
            return 1.4
        elif tam == "G" or tam == "g":
            return 1.6
        elif tam == 0 or tam == "0":
            return 0
        else:
            print("Parámetro inválido!")

def verificaDesc():
    while True:
        desc = input("Gostaria da sua bebida descafeinada? S / N: ")
        if desc == "S" or desc == "s":
            return 1
        elif desc == "N" or desc == "n":
            return 0
        elif desc == 0 or desc == "0":
            return 2
        else:
            print("Parâmetro inválido")

def verificaDisp(tam, listaPosicao, statusProd, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente):
    #print("            ╔═════════════════════╗")
    #print("        ╔═══╣     BEM-VINDO À     ║")
    #print("        ╚═══╣   NOME DA EMPRESA   ║")
    #print("            ╚══╦═══════════════╦══╝")
    print("╔══════════════╩═══════════════╩══════════════╗")
    for i in range(len(listaPosicao)):
        match listaPosicao[i]:
            case 1:
                print(f"║ {i + 1}. {prodEspresso[1]}", end="")
                pos = 0
                lista = prodEspresso
            case 2:
                print(f"║ {i + 1}. {prodCafePreto[1]}", end="")
                pos = 1
                lista = prodCafePreto                
            case 3:
                print(f"║ {i + 1}. {prodLatte[1]}", end="")
                pos = 2
                lista = prodLatte 
            case 4:
                print(f"║ {i + 1}. {prodCafeComLeite[1]}", end="")
                pos = 3
                lista = prodCafeComLeite
            case 5:
                print(f"║ {i + 1}. {prodLeiteComCafe[1]}", end="")
                pos = 4
                lista = prodLeiteComCafe
            case 6:
                print(f"║ {i + 1}. {prodCappuccino[1]}", end="")
                pos = 5
                lista = prodCappuccino
            case 7:
                print(f"║ {i + 1}. {prodMacchiato[1]}", end="")
                pos = 6
                lista = prodMacchiato
            case 8:
                print(f"║ {i + 1}. {prodMocha[1]}", end="")
                pos = 7
                lista = prodMocha
            case 9:
                print(f"║ {i + 1}. {prodChocoQuente[1]}", end="")
                pos = 8
                lista = prodChocoQuente

        preco = f"{lista[2]*tam:.2f}".replace(".", ",")
        passo = len(lista[1])       
        if statusProd[pos] == 1:
            print(" ", "-" * (30 - passo),end="")
            print(f" R$ {preco} ║")
        else:
            passo = passo + 5
            print(" ", "-" * (30 - passo),end="")
            print(" Indisponível ║")
    print("║ 0. Voltar                                   ║")
    print("╚═════════════════════════════════════════════╝")

def escolheProd(listaPosicao, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente):
    print("Digite o número da sua bebida: ", end="")
    cod = digitarIntPositivo()
    while cod == None or cod < 0 or cod > 9:
        print("Digite o número da sua bebida: ", end="")
        cod = digitarIntPositivo()
    if cod == 0:
        return 0
    match listaPosicao[cod - 1]:
        case 1:
            return prodEspresso
        case 2:
            return prodCafePreto
        case 3:
            return prodLatte
        case 4:
            return prodCafeComLeite
        case 5:
            return prodLeiteComCafe
        case 6:
            return prodCappuccino
        case 7:
            return prodMacchiato
        case 8:
            return prodMocha
        case 9:
            return prodChocoQuente

def compraProd(tam, desc, prodCliente, agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela):
    if desc == 1:
        if tam == 1:
            cafeSolDesc = cafeSolDesc - prodCliente[5]
        elif tam == 1.4:
            cafeSolDesc = cafeSolDesc - prodCliente[5] * 2
        else:
            cafeSolDesc = cafeSolDesc - prodCliente[5] * 3
    else:
        if tam == 1:
            cafeSol = cafeSol - prodCliente[5]
        elif tam == 1.4:
            cafeSol = cafeSol - prodCliente[5] * 2
        else:
            cafeSol = cafeSol - prodCliente[5] * 3
    if tam == 1:
        agua = agua - 50
        leitePo = leitePo - prodCliente[6]
        chocoPo = chocoPo - prodCliente[7]
        canela = canela - prodCliente[8]
    elif tam == 1.4:
        agua = agua - 100
        leitePo = leitePo - prodCliente[6] * 2
        chocoPo = chocoPo - prodCliente[7] * 2
        canela = canela - prodCliente[8] * 2
    else:
        agua = agua - 150
        leitePo = leitePo - prodCliente[6] * 3
        chocoPo = chocoPo - prodCliente[7] * 3
        canela = canela - prodCliente[8] * 3
    return agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela 

def vendaDoProduto(din, tam, desc, agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG, prodCliente, listaCaixa, listaDinCliente):
    if tam == 1:
        copoP = copoP - 1
    elif tam == 1.4:
        copoM = copoM - 1
    else:
        copoG = copoG - 1
    din = din - prodCliente[2] * tam
    somarLista(listaCaixa, listaDinCliente)
    listaDinCliente = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    prepararBebida(prodCliente)
    agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela = compraProd(tam, desc, prodCliente, agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela)
    return din, agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG, listaDinCliente
        
def organizaPosicao(listaPosicao, statusProd):
    disp = 0
    indis = len(listaPosicao) - 1
    for i in range(len(listaPosicao)):
        if statusProd[i] == 1:
            listaPosicao[disp] = i + 1
            disp = disp + 1
        else:
            listaPosicao[indis] = i + 1
            indis = indis - 1
        
def verificaStatus(tam, desc, statusProd, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente):
    if tam == 1:
        mult = 1
    elif tam == 1.4:
        mult = 2
    else:
        mult = 3
    prodEspresso[3], prodCafePreto[3], prodLatte[3], prodCafeComLeite[3], prodLeiteComCafe[3], prodCappuccino[3], prodMacchiato[3], prodMocha[3], prodChocoQuente[3] = 1, 1, 1, 1, 1, 1, 1, 1, 1
    if desc == 1:
        if prodEspresso[5] * mult > cafeSolDesc:
            prodEspresso[3] = 0
        if prodCafePreto[5] * mult > cafeSolDesc:
            prodCafePreto[3] = 0
        if prodLatte[5] * mult > cafeSolDesc or prodLatte[6] * mult > leitePo:
            prodLatte[3] = 0
        if prodCafeComLeite[5] * mult > cafeSolDesc or prodCafeComLeite[6] * mult > leitePo:
            prodCafeComLeite[3] = 0
        if prodLeiteComCafe[5] * mult > cafeSolDesc or prodLeiteComCafe[6] * mult > leitePo:
            prodLeiteComCafe[3] = 0
        if prodCappuccino[5] * mult > cafeSolDesc or prodCappuccino[6] * mult > leitePo or prodCappuccino[7] * mult > chocoPo or prodCappuccino[8] * mult > canela:
            prodCappuccino[3] = 0
        if prodMacchiato[5] * mult > cafeSolDesc or prodMacchiato[6] * mult > leitePo:
            prodMacchiato[3] = 0
        if prodMocha[5] * mult > cafeSolDesc or prodMocha[6] * mult > leitePo or prodMocha[7] * mult > chocoPo:
            prodMocha[3] = 0
        if prodChocoQuente[5] * mult > cafeSolDesc or prodChocoQuente[6] * mult > leitePo or prodChocoQuente[7] * mult > chocoPo:
            prodChocoQuente[3] = 0
    else:
        if prodEspresso[5] * mult > cafeSol:
            prodEspresso[3] = 0
        if prodCafePreto[5] * mult > cafeSol:
            prodCafePreto[3] = 0
        if prodLatte[5] * mult > cafeSol or prodLatte[6] * mult > leitePo:
            prodLatte[3] = 0
        if prodCafeComLeite[5] * mult > cafeSol or prodCafeComLeite[6] * mult > leitePo:
            prodCafeComLeite[3] = 0
        if prodLeiteComCafe[5] * mult > cafeSol or prodLeiteComCafe[6] * mult > leitePo:
            prodLeiteComCafe[3] = 0
        if prodCappuccino[5] * mult > cafeSol or prodCappuccino[6] * mult > leitePo or prodCappuccino[7] * mult > chocoPo or prodCappuccino[8] * mult > canela:
            prodCappuccino[3] = 0
        if prodMacchiato[5] * mult > cafeSol or prodMacchiato[6] * mult > leitePo:
            prodMacchiato[3] = 0
        if prodMocha[5] * mult > cafeSol or prodMocha[6] * mult > leitePo or prodMocha[7] * mult > chocoPo:
            prodMocha[3] = 0
        if prodChocoQuente[5] * mult > cafeSol or prodChocoQuente[6] * mult > leitePo or prodChocoQuente[7] * mult > chocoPo:
            prodChocoQuente[3] = 0
    statusProd[0], statusProd[1], statusProd[2], statusProd[3], statusProd[4], statusProd[5], statusProd[6], statusProd[7], statusProd[8], = prodEspresso[3], prodCafePreto[3], prodLatte[3], prodCafeComLeite[3], prodLeiteComCafe[3], prodCappuccino[3], prodMacchiato[3], prodMocha[3], prodChocoQuente[3]
            
def venda(din, agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente, listaVal, listaCaixa, listaDinCliente, listaPosicao, statusProd):
    while True:
        if agua < 50:
            print("A máquina está sem água para bebidas")
            break
        else:
            # def venda(muitasCoisas):
            # def telaTamBeb():
            while True:
                res = ""
                tam = verificaTam()
                if tam == 0:
                    # funçãoVoltar()
                    print("Blá")
                    break
                if tam == 1 and copoP < 1:
                    # funçãoVoltar()
                    print("Infelizmente a máquina está sem copos para bebidas pequenas (50ml)")
                    break
                elif tam == 1.4 and copoM < 1:
                    # funçãoVoltar()
                    print("Infelizmente a máquina está sem copos para bebidas médias (100ml)")
                    break
                elif tam == 1.6 and copoG < 1:
                    # funçãoVoltar()
                    print("Infelizmente a máquina está sem copos para bebidas grandes (150ml)")
                    break
                else:
                    while True:
                        if res == "S" or res == "s":
                            break
                        desc = verificaDesc()
                        if desc == 2:
                            # funçãoVoltar()
                            print("Blá")
                            break
                        else:
                            while True:
                                verificaStatus(tam, desc, statusProd, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente)
                                organizaPosicao(listaPosicao, statusProd)
                                verificaDisp(tam, listaPosicao, statusProd, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente)
                                prodCliente = escolheProd(listaPosicao, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente)
                                print(prodCliente)
                                if prodCliente == 0:
                                    # funçãoVoltar()
                                    print("Blá")
                                    break
                                else:
                                    #while True:
                                        while prodCliente == 0 or prodCliente[3] == 0:
                                            if prodCliente == 0:
                                                # funçãoVoltar()
                                                print("Blá")
                                                break
                                            print(f"Infelizmente {prodCliente[1]} está indisponível!")
                                            print("Escolha uma nova bebida.")
                                            prodCliente = escolheProd(listaPosicao, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente)
                                        if prodCliente == 0:
                                            break
                                        resp = input(f"Deseja preparar {prodCliente[1]}? S / N: ")
                                        while True:
                                            if resp == "S" or resp == "s":
                                                break
                                            elif resp == "N" or resp == "n" or resp == 0:
                                                break
                                            else:
                                                print("Parâmetro inválido!")
                                                resp = input(f"Deseja preparar {prodCliente[1]}? S / N: ")
                                        if resp == "S" or resp == "s":
                                            if din < prodCliente[2] * tam:
                                                print("Insira o dinheiro na máquina")
                                                somarDinheiro(listaVal, listaDinCliente)
                                                din = din + dinCliente(listaVal, listaDinCliente)
                                            temTroco = verificarCaixa(din - prodCliente[2] * tam, listaVal, listaCaixa, listaDinCliente)
                                            if din >= prodCliente[2] * tam and temTroco == True:
                                                din, agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG, listaDinCliente = vendaDoProduto(din, tam, desc, agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG, prodCliente, listaCaixa, listaDinCliente)

                                                res = input(f"Restam R$ {din:.2f}. Deseja comprar outra bebida? S/N: ")
                                                if res == "S" or res == "s":
                                                    break
                                                elif din > 0:
                                                    darTroco(din, listaVal, listaCaixa)
                                                    print()
                                                    print("Agradecemos pela preferencia!")
                                                    time.sleep(3)
                                                    return agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente, listaCaixa, listaDinCliente
                                                else:
                                                    print("Você não possui troco")
                                                    print("Volte sempre!")
                                            elif din < prodCliente[2] * tam:
                                                print("Dinheiro insuficiente!")
                                                time.sleep(1)
                                                if din > 0:
                                                    somarLista(listaCaixa, listaDinCliente)
                                                    listaDinCliente = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                                                    darTroco(din, listaVal, listaCaixa)
                                                    return agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente, listaCaixa, listaDinCliente
                                                else:
                                                    # Verificar aqui
                                                    print("Você não possui troco")
                                                    print("Volte sempre!")
                                            elif temTroco == False:
                                                print("Infelizmente a máquina está sem troco para a quantia fornecida.")
                                                time.sleep(1)
                                                somarLista(listaCaixa, listaDinCliente)
                                                listaDinCliente = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                                                darTroco(din, listaVal, listaCaixa)
                                                return agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente, listaCaixa, listaDinCliente
                                            
# Verificar quando retorna os valores, 

def main():
    limpaTela()

    listaVal = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
    listaCaixa = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    listaDinCliente = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    listaPosicao = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    statusProd = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Produtos
    # ProdLista = [ID, nome, preco, status, vendas, cafeSoluvel, leitePo, chocoPo, canela]
    prodEspresso = [1, "Café Espresso", 3.5, 1, 0, 2, 0, 0, 0]
    prodCafePreto = [2, "Café Preto", 2.5, 1, 0, 0.75, 0, 0, 0]
    prodLatte = [3, "Latte", 3.5, 1, 0, 0.75, 12, 0, 0]
    prodCafeComLeite = [4, "Café com Leite", 2.75, 1, 0, 0.75, 5, 0, 0]
    prodLeiteComCafe = [5, "Leite com Café", 3, 1, 0, 0.75, 10, 0, 0]
    prodCappuccino = [6, "Cappuccino", 4, 1, 0, 2, 10, 2.5, 0.15]
    prodMacchiato = [7, "Macchiato", 4.5, 1, 0, 3, 7, 0, 0]
    prodMocha = [8, "Mocha", 4, 1, 0, 1, 5, 5, 0]
    prodChocoQuente = [9, "Chocolate Quente", 3.75, 1, 0, 0, 8, 5, 0]

    din = 0
    agua = 1000
    cafeSol = 1000
    cafeSolDesc = 1000
    leitePo = 1000
    chocoPo = 1000
    canela = 100
    copoP = 100 # copo de 80ml
    copoM = 100 # copo de 130ml
    copoG = 100 # copo de 180ml
    while True:
        agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente, listaCaixa, listaDinCliente  = venda(din, agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente, listaVal, listaCaixa, listaDinCliente, listaPosicao, statusProd)
        print()
        print(f"Dinheiro: {din}")
        print(f"Água: {agua}")
        print(f"Café Solúvel: {cafeSol}")
        print(f"Café Solúvel Descafeinado: {cafeSolDesc}")
        print(f"Leite em Pó: {leitePo}")
        print(f"Chocolate em Pó: {chocoPo}")
        print(f"Copo (P) 50 ml:  {copoP}")
        print(f"Copo (M) 100 ml: {copoM}")
        print(f"Copo (G) 150 ml: {copoG}")
        print(f"Espresso:       {prodEspresso}")
        print(f"Café Preto:     {prodCafePreto}")
        print(f"Latte:          {prodLatte}")
        print(f"Café com Leite: {prodCafeComLeite}")
        print(f"Leite com Café: {prodLeiteComCafe}")
        print(f"Cappuccino:     {prodCappuccino}")
        print(f"Macchiato:      {prodMacchiato}")
        print(f"Mocha:          {prodMocha}")
        print(f"ChocoQuente:    {prodChocoQuente}")
        print(listaCaixa)
        print(listaDinCliente)
    

main()
    
""" def infEspresso():
    print("Café Espresso (P): R$ 3,50")
    print("2g de café sóluvel")
    print("50ml de água")
    print()
    print("Café Espresso (M): R$ 5,25")
    print("4g de café sóluvel")
    print("100ml de água")
    print()
    print("Café Espresso (G): R$ 5,95")
    print("6g de café sóluvel")
    print("150ml de água")
    print() """