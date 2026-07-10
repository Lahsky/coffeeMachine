from os import system, name
import time

def limpaTela():
    '''
    Função que limpa a tela do terminal.

    Esta função verifica qual o sistema operacional usado e limpa a tela do terminal com base nessa informação.
    '''
    if name == "nt":
        system("cls")
    else:
        system("clear")

def xicaraG():
    '''
    Função que imprime uma xícara de café.

    Está função imprime uma xícara de café com o nome da máquina de bebidas.
    '''
    print("              ഽ       ഽ       ഽ       ")
    print("               ഽ       ഽ       ഽ       ")
    print("              ഽ       ഽ       ഽ       ")
    print("               ഽ       ഽ       ഽ       ")
    print("       ╔═══════════════════════════════╗")
    print("   ╔═══║ ★                          ★  ║       ")
    print("  ╔╝   ║ ★                          ★  ║       ")
    print("  ║    ║ ★        STARCOFFEE        ★  ║       ")
    print("  ╚╗   ║ ★                          ★  ║       ")
    print("   ╚═══║ ★                          ★  ║       ")
    print("       ╚═╦═══════════════════════════╦═╝        ")
    print("     ╔═══╩═══════════════════════════╩═══╗")

def telaMsgSemAgua():
    '''
    Função que avisa que está sem água para bebidas.

    Esta função limpa a tela do terminal e imprime uma mensagem avisando que não tem mais água para bebidas.
    '''
    limpaTela()
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║                                             ║")
    print("║         Infelizmente a máquina está         ║")
    print("║            sem água para bebidas            ║")
    print("║                                             ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def telaMsgSemAguaM():
    '''
    Função que avisa que está sem água para bebidas médias.

    Esta função limpa a tela do terminal e imprime uma mensagem avisando que não tem mais água para bebidas de tamanho médio.
    '''
    limpaTela()
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║                                             ║")
    print("║         Infelizmente a máquina está         ║")
    print("║        sem água para bebidas médias         ║")
    print("║                                             ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def telaMsgSemAguaG():
    '''
    Função que avisa que está sem água para bebidas grandes.

    Esta função limpa a tela do terminal e imprime uma mensagem avisando que não tem mais água para bebidas de tamanho grande.
    '''
    limpaTela()
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║                                             ║")
    print("║         Infelizmente a máquina está         ║")
    print("║        sem água para bebidas grandes        ║")
    print("║                                             ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def telaMsgSemCopoP():
    '''
    Função que avisa que está sem copos para bebidas pequenas.

    Esta função limpa a tela do terminal, imprime uma mensagem avisando que está sem copos pequenos para as bebidas pequenas.
    '''
    limpaTela()
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║                                             ║")
    print("║         Infelizmente a máquina está         ║")
    print("║   sem copos para bebidas pequenas (50 mL)   ║")
    print("║                                             ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def telaMsgSemCopoM():
    '''
    Função que avisa que está sem copos para bebidas médias.

    Esta função limpa a tela do terminal, imprime uma mensagem avisando que está sem copos médios para as bebidas médias.
    '''
    limpaTela()
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║                                             ║")
    print("║         Infelizmente a máquina está         ║")
    print("║   sem copos para bebidas médias (100 mL)    ║")
    print("║                                             ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def telaMsgSemCopoG():
    '''
    Função que avisa que está sem copos para bebidas grandes.

    Esta função limpa a tela do terminal, imprime uma mensagem avisando que está sem copos grandes para as bebidas grandes.
    '''
    limpaTela()
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║                                             ║")
    print("║         Infelizmente a máquina está         ║")
    print("║   sem copos para bebidas grandes (150 mL)   ║")
    print("║                                             ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def telaProdIndisp(prodCliente):
    '''
    Função que avisa que um produto não está disponível.

    Esta função limpa a tela do terminal, recebe uma lista com o produto do cliente e imprime que ele não está disponível.

    Argumentos:
        prodCliente (list): Lista do produto do cliente.    
    '''
    limpaTela()
    if len(prodCliente[1]) % 2 == 0:
        passo1 = (42 - len(prodCliente[1])) // 2
        passo2 = passo1 + 1
    else:
        passo1 = (43 - len(prodCliente[1])) // 2
        passo2 = passo1
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║                                             ║")
    print("║                Infelizmente                 ║")
    print("║", " " * passo1,end="")
    print(prodCliente[1],end="")
    print(" " * passo2, "║")
    print("║       não está disponível no momento!       ║")
    print("║                                             ║")
    print("╚═════════════════════════════════════════════╝")
    print()
    time.sleep(3)

def telaConfimacao(prodCliente):
    '''
    Função para confimar o preparo da bebida.

    Esta função limpa a tela do terminal, recebe a lista com o produto do cliente e imprime uma mensagem de confimação se o cliente realmente deseja preparar esta bebida.

    Argumentos:
        prodCliente (list): Lista do produto do cliente.
    '''
    limpaTela()
    if len(prodCliente[1]) % 2 == 0:
        passo1 = (42 - len(prodCliente[1])) // 2
        passo2 = passo1
    else:
        passo1 = (42 - len(prodCliente[1])) // 2
        passo2 = passo1 + 1
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║   ★ ┅┅┅┅┅┅┅┅┅ Deseja preparar ┅┅┅┅┅┅┅┅┅ ★   ║")
    print("║                                             ║")
    print("║", " " * passo1,end="")
    print(f"{prodCliente[1]}?",end="")
    print(" " * passo2, "║")
    print("║                                             ║")
    print("║           1. Sim           0. Não           ║")
    print("║                                             ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def telaDinCliente(din):
    '''
    Função para exibir o dinheiro do cliente.

    Esta função limpa a tela do terminal, recebe a variável de dinheiro do cliente e imprime o valor na tela.

    Argumentos:
        din (float): váriavel contendo o valor que o cliente colocou na máquina.
    '''
    limpaTela()
    if verQuantNum(din) % 2 == 0:
        passo1 = (37 - verQuantNum(din)) // 2
        passo2 = passo1 + 1
    else:
        passo1 = (37 - verQuantNum(din)) // 2
        passo2 = passo1
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║   ★ ┅┅┅┅┅┅┅┅┅┅ Dinhero total ┅┅┅┅┅┅┅┅┅┅ ★   ║")
    print("║                                             ║")
    print("║", " " * passo1,end="")
    print(f"R$ {din:.2f}".replace(".",","),end="")
    print(" " * passo2, "║")
    print("║                                             ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def telaOutraBeb():
    '''
    Função que pergunta se quer uma nova bebida.

    Esta função limpa a tela do terminal e imprime se o cliente quer comprar uma outra bebida.
    '''
    limpaTela()
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║   ★ ┅┅┅┅┅┅┅┅┅┅ Outra bebida? ┅┅┅┅┅┅┅┅┅┅ ★   ║")
    print("║                                             ║")
    print("║           1. Sim           0. Não           ║")
    print("║                                             ║") 
    print("╚═════════════════════════════════════════════╝")
    print()

def telaFinalizar():
    '''
    Função que pergunta se quer finalizar.

    Esta função limpa a tela do terminal e imprime se o usuário quer finalizar o programa.
    '''
    limpaTela()
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║   ★ ┅┅┅┅┅┅┅┅ Deseja finalizar? ┅┅┅┅┅┅┅┅ ★   ║")
    print("║                                             ║")
    print("║           1. Sim           0. Não           ║")
    print("║                                             ║") 
    print("╚═════════════════════════════════════════════╝")
    print()

def telaPrefencia():
    '''
    Função que imprime uma mensagem de agradecimento.

    Esta função limpa a tela do terminal e imprime uma mensagem de agradecimento pela preferência.
    '''
    limpaTela()
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║                                             ║")
    print("║   ★ ┅┅┅┅ Agradecemos a preferência ┅┅┅┅ ★   ║")
    print("║                                             ║") 
    print("╚═════════════════════════════════════════════╝")
    print()
    time.sleep(2)

def telaInicial():
    '''
    Função que imprime o menu inicial.

    Esta função limpa a tela do terminal e imprime o menu inicial com as opções de bebida, configurações, 'quem somos' e finalizar.
    '''
    limpaTela()
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║   ★ ┅┅┅┅┅┅┅┅ Escolha uma opção ┅┅┅┅┅┅┅┅ ★   ║")
    print("║ 1. Bebidas                                  ║")            
    print("║ 2. Configurações                            ║")
    print("║ 3. Quem somos                               ║")
    print("║ 4. Finalizar                                ║")  
    print("╚═════════════════════════════════════════════╝")
    print()

def telaTamBeb():
    '''
    Função que imprime o menu com o tamanho das bebidas.

    Esta função limpa a tela do terminal e imprime o menu do tamanho das bebidas (pequeno, médio e grande).
    '''
    limpaTela()
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║   ★ ┅┅┅ Escolha o tamanho da bebida ┅┅┅ ★   ║")
    print("║ 1. Pequeno (P) ---------------------- 50 mL ║")
    print("║ 2. Médio (M) ----------------------- 100 mL ║")
    print("║ 3. Grande (G) ---------------------- 150 mL ║")
    print("║ 0. Voltar                                   ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def telaDescCafe():
    '''
    Função que imprime o menu com o tipo de preparo da bebida.

    Esta função limpa a tela do terminal e imprime o menu com os dois tipos de preparo da bebida (cafeinado e descafeinado).
    '''
    limpaTela()
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║   ★ ┅┅┅┅ Escolha o tipo de preparo ┅┅┅┅ ★   ║")
    print("║ 1. Descafeinado                             ║")
    print("║ 2. Cafeinado                                ║")
    print("║ 0. Voltar                                   ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def prepararBebida(prodCliente):
    '''
    Função que prepara a bebida do cliente.

    Esta função limpa a tela do terminal, recebe a lista com o produto do cliente, exibe uma mensagem que a bebida do cliente que está sendo preparada e outra que a bebida está pronta.

    Argumentos:
        prodCliente (list): Lista do produto do cliente.
    '''
    limpaTela()
    print("")
    print("")
    print("")
    print("               ഽ       ഽ       ഽ       ")
    print("       ╔═══════════════════════════════╗")
    print("   ╔═══║ ★                          ★  ║       ")
    print("  ╔╝   ║ ★                          ★  ║       ")
    print("  ║    ║ ★        STARCOFFEE        ★  ║       ")
    print("  ╚╗   ║ ★                          ★  ║       ")
    print("   ╚═══║ ★                          ★  ║       ")
    print("       ╚═══════════════════════════════╝        ")
    print()
    print()
    print(f"{prodCliente[1]} está sendo preparado.")
    time.sleep(1)
    limpaTela()
    print("")
    print("")
    print("              ഽ       ഽ       ഽ       ")
    print("               ഽ       ഽ       ഽ       ")
    print("       ╔═══════════════════════════════╗")
    print("   ╔═══║ ★                          ★  ║       ")
    print("  ╔╝   ║ ★                          ★  ║       ")
    print("  ║    ║ ★        STARCOFFEE        ★  ║       ")
    print("  ╚╗   ║ ★                          ★  ║       ")
    print("   ╚═══║ ★                          ★  ║       ")
    print("       ╚═══════════════════════════════╝        ")
    print()
    print()
    print(f"{prodCliente[1]} está sendo preparado..")
    time.sleep(1)
    limpaTela()
    print("")
    print("               ഽ       ഽ       ഽ       ")
    print("              ഽ       ഽ       ഽ       ")
    print("               ഽ       ഽ       ഽ       ")
    print("       ╔═══════════════════════════════╗")
    print("   ╔═══║ ★                          ★  ║       ")
    print("  ╔╝   ║ ★                          ★  ║       ")
    print("  ║    ║ ★        STARCOFFEE        ★  ║       ")
    print("  ╚╗   ║ ★                          ★  ║       ")
    print("   ╚═══║ ★                          ★  ║       ")
    print("       ╚═══════════════════════════════╝        ")
    print()
    print()
    print(f"{prodCliente[1]} está sendo preparado...")
    time.sleep(1)
    limpaTela()
    print("              ഽ       ഽ       ഽ       ")
    print("               ഽ       ഽ       ഽ       ")
    print("              ഽ       ഽ       ഽ       ")
    print("               ഽ       ഽ       ഽ       ")
    print("       ╔═══════════════════════════════╗")
    print("   ╔═══║ ★                          ★  ║       ")
    print("  ╔╝   ║ ★                          ★  ║       ")
    print("  ║    ║ ★        STARCOFFEE        ★  ║       ")
    print("  ╚╗   ║ ★                          ★  ║       ")
    print("   ╚═══║ ★                          ★  ║       ")
    print("       ╚═══════════════════════════════╝        ")
    print()
    print()
    print(f"Seu {prodCliente[1]} está pronto!")
    print()
    time.sleep(2)

def telaConfiguracoes():
    '''
    Função que imprime o menu configurações.

    Esta função limpa a tela do terminal e imprime o menu de configurações.
    '''
    limpaTela()
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║   ★ ┅┅┅┅┅┅┅┅┅┅ Configurações ┅┅┅┅┅┅┅┅┅┅ ★   ║")
    print("║ 1. Informações internas                     ║")
    print("║ 2. Informações dos produtos                 ║")
    print("║ 3. Reposição de insumos                     ║")
    print("║ 4. Reposição de notas e moedas              ║")
    print("║ 5. Sangria                                  ║")
    print("║ 0. Voltar                                   ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def telaInfInternas(agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente):
    '''
    Função que exibe as informações internas de insumos e faturamento da máquina .

    Esta função recebe diversas variáveis com a quantidade de cada insumo da máquina, além da diversas listas de produtos para calcular o faturamento.
    Ela limpa a tela do terminal e imprime a quantidade de cada insumo e o faturamento.

    Argumentos:
        agua (int): variável com a quantidade em mililitros de água.
        cafeSol (float): variável com a quantidade em gramas de café solúvel.
        cafeSolDesc (float): variável com a quantidade em gramas de café solúvel descafeinado.
        leitePo (float): variável com a quantidade em gramas de leite em pó.
        chocoPo (float): variável com a quantidade em gramas de chocolate em pó.
        canela (float): variável com a quantidade em gramas de canela.
        copoP (int): variável com a quantidade de copos de tamanho (P).
        copoM (int): variável com a quantidade de copos de tamanho (M).
        copoG (int): variável com a quantidade de copos de tamanho (G).
        prodEspresso (list): lista com as informções do produto 'Espresso'.
        prodCafePreto (list): lista com as informções do produto 'Café Preto'.
        prodLatte (list): lista com as informções do produto 'Latte'.
        prodCafeComLeite (list): lista com as informções do produto 'Café com Leite'.
        prodLeiteComCafe (list): lista com as informções do produto 'Leite com Café'.
        prodCappuccino (list): lista com as informções do produto 'Cappuccino'.
        prodMacchiato (list): lista com as informções do produto 'Macchiato'.
        prodMocha (list): lista com as informções do produto 'Mocha'.
        prodChocoQuente (list): lista com as informções do produto 'Chocolate Quente'.
        '''
    limpaTela()
    faturamento = calcFaturamento(prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente)
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║   ★ ┅┅┅┅┅┅ Informações internas: ┅┅┅┅┅┅ ★   ║")
    print(f"║ Água: {agua} mL", end="")
    print(" " * (34 - verQuantNum(agua)), "║")
    print(f"║ Café Solúvel: {cafeSol:.2f} g".replace(".", ","), end="")
    print(" " * (24 - verQuantNum(cafeSol)), "║")
    print(f"║ Café Solúvel Descafeinado: {cafeSolDesc:.2f} g".replace(".", ","), end="")
    print(" " * (11 - verQuantNum(cafeSolDesc)), "║")
    print(f"║ Leite em Pó: {leitePo:.2f} g".replace(".", ","), end="")
    print(" " * (25 - verQuantNum(leitePo)), "║")
    print(f"║ Chocolate em Pó: {chocoPo:.2f} g".replace(".", ","), end="")
    print(" " * (21 - verQuantNum(chocoPo)), "║")
    print(f"║ Canela: {canela:.2f} g".replace(".", ","), end="")
    print(" " * (30 - verQuantNum(canela)), "║")
    print(f"║ Copo (P) 80 mL: {copoP} unidade(s)", end="")
    print(" " * (16 - verQuantNum(copoP)), "║")
    print(f"║ Copo (M) 130 mL: {copoM} unidade(s)", end="")
    print(" " * (15 - verQuantNum(copoM)), "║")
    print(f"║ Copo (G) 180 mL: {copoG} unidade(s)", end="")
    print(" " * (15 - verQuantNum(copoG)), "║")
    print("║                                             ║")
    print(f"║ Faturamento: R$ {faturamento:.2f}".replace(".", ","),end="")
    print(" " * (24 - verQuantNum(faturamento)), "║")
    print("║                                             ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def telaReposicao(agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG):
    '''
    Função que exibe as informações internas de insumos da máquina .

    Esta função recebe diversas variáveis com a quantidade de cada insumo da máquina, limpa a tela do terminal e imprime a quantidade de cada insumo.

    Argumentos:
        agua (int): variável com a quantidade em mililitros de água.
        cafeSol (float): variável com a quantidade em gramas de café solúvel.
        cafeSolDesc (float): variável com a quantidade em gramas de café solúvel descafeinado.
        leitePo (float): variável com a quantidade em gramas de leite em pó.
        chocoPo (float): variável com a quantidade em gramas de chocolate em pó.
        canela (float): variável com a quantidade em gramas de canela.
        copoP (int): variável com a quantidade de copos de tamanho (P).
        copoM (int): variável com a quantidade de copos de tamanho (M).
        copoG (int): variável com a quantidade de copos de tamanho (G).
    '''
    limpaTela()
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║   ★ ┅┅┅┅┅┅┅┅┅┅┅┅ Reposição ┅┅┅┅┅┅┅┅┅┅┅┅ ★   ║")
    print(f"║ 1. Água: {agua} mL", end="")
    print(" " * (31 - verQuantNum(agua)), "║")
    print("║ 2. ", end="")
    print(f"Café Solúvel: {cafeSol:.2f} g".replace(".", ","), end="")
    print(" " * (21 - verQuantNum(cafeSol)), "║")
    print("║ 3. ", end="")
    print(f"Café Solúvel Descafeinado: {cafeSolDesc:.2f} g".replace(".", ","), end="")
    print(" " * (8 - verQuantNum(cafeSolDesc)), "║")
    print("║ 4. ", end="")
    print(f"Leite em Pó: {leitePo:.2f} g".replace(".", ","), end="")
    print(" " * (22 - verQuantNum(leitePo)), "║")
    print("║ 5. ", end="")
    print(f"Chocolate em Pó: {chocoPo:.2f} g".replace(".", ","), end="")
    print(" " * (18 - verQuantNum(chocoPo)), "║")
    print("║ 6. ", end="")
    print(f"Canela: {canela:.2f} g".replace(".", ","), end="")
    print(" " * (27 - verQuantNum(canela)), "║")
    print(f"║ 7. Copo (P) 80 mL: {copoP} unidade(s)", end="")
    print(" " * (13 - verQuantNum(copoP)), "║")
    print(f"║ 8. Copo (M) 130 mL: {copoM} unidade(s)", end="")
    print(" " * (12 - verQuantNum(copoM)), "║")
    print(f"║ 9. Copo (G) 180 mL: {copoG} unidade(s)", end="")
    print(" " * (12 - verQuantNum(copoG)), "║")
    print("║ 0. Voltar                                   ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def telaCaixa(listaVal, listaCaixa):
    '''
    Função que mostra valores do caixa da máquina

    Esta função recebe a lista de valores de notas e moedas, a lista com a quantidade de notas e moedas que tem no caixa e imprime os valores na tela do terminal. 

    Argumentos:
        listaVal (list): lista que contém os valores das notas e das moedas.
        listaCaixa (list): lista que contém a quantidade de notas e moedas no caixa da máquina.
    '''
    limpaTela()
    xicaraG()
    totalCaixa = 0
    for i in range(len(listaVal)):
        totalCaixa =  totalCaixa + listaCaixa[i] * listaVal[i]
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║   ★ ┅┅┅┅┅┅┅┅┅┅┅┅┅┅ Caixa ┅┅┅┅┅┅┅┅┅┅┅┅┅┅ ★   ║")
    print(f"║ 1.  R$ 100,00: {listaCaixa[0]} notas", " " * (21 - verQuantNum(listaCaixa[0])), "║")
    print(f"║ 2.  R$ 50,00:  {listaCaixa[1]} notas", " " * (21 - verQuantNum(listaCaixa[1])), "║")
    print(f"║ 3.  R$ 20,00:  {listaCaixa[2]} notas", " " * (21 - verQuantNum(listaCaixa[2])), "║" )
    print(f"║ 4.  R$ 10,00:  {listaCaixa[3]} notas", " " * (21 - verQuantNum(listaCaixa[3])), "║" )
    print(f"║ 5.  R$ 5,00:   {listaCaixa[4]} notas", " " * (21 - verQuantNum(listaCaixa[4])), "║" )
    print(f"║ 6.  R$ 2,00:   {listaCaixa[5]} notas", " " * (21 - verQuantNum(listaCaixa[5])), "║" )
    print(f"║ 7.  R$ 1,00:   {listaCaixa[6]} notas", " " * (21 - verQuantNum(listaCaixa[6])), "║" )
    print(f"║ 8.  R$ 0,50:   {listaCaixa[7]} moedas", " " * (20 - verQuantNum(listaCaixa[7])), "║" )
    print(f"║ 9.  R$ 0,25:   {listaCaixa[8]} moedas", " " * (20 - verQuantNum(listaCaixa[8])), "║" )
    print(f"║ 10. R$ 0,10:   {listaCaixa[9]} moedas", " " * (20 - verQuantNum(listaCaixa[9])), "║" )
    print(f"║ 11. R$ 0,05:   {listaCaixa[10]} moedas", " " * (20 - verQuantNum(listaCaixa[10])), "║" )
    print(f"║ 12. R$ 0,01:   {listaCaixa[11]} moedas", " " * (20 - verQuantNum(listaCaixa[11])), "║" )
    print("║ 0.  Voltar                                  ║")
    print("║                                             ║")
    print(f"║ Total: R$ {totalCaixa:.2f}".replace(".",","), end="")
    print(" " * (30 - verQuantNum(totalCaixa)), "║")
    print("╚═════════════════════════════════════════════╝")
    print()

def telaQuemSomos():
    '''
    Função que imprime missão, visão, valores e desenvolvedores da máquina de bebidas.

    Está função limpa a tela do terminal e imprime missão, visão, valores e desenvolvedores da máquina de bebidas.
    '''
    limpaTela()
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║     ★ Bem-vindo à Starcoffee Machine ★      ║")
    print("║                                             ║")
    print("║     Desenvolvemos máquinas inteligentes     ║")
    print("║      que oferecem exímia praticidade e      ║")
    print("║ qualidade no preparo de bebidas cotidianas. ║")
    print("║                                             ║")
    print("║   ★ ┅┅┅┅┅┅┅┅┅┅┅┅┅ Missão ┅┅┅┅┅┅┅┅┅┅┅┅┅ ★    ║")
    print("║                                             ║")
    print("║       Oferecer um sistema eficiente e       ║")
    print("║ intuitivo no preparo de cafés de qualidade, ║")
    print("║     criando uma experiência confortável     ║")
    print("║          entre o usuário e máquina.         ║")
    print("║                                             ║")
    print("║   ★ ┅┅┅┅┅┅┅┅┅┅┅┅┅┅ Visão ┅┅┅┅┅┅┅┅┅┅┅┅┅┅ ★   ║")
    print("║                                             ║")
    print("║ Visamos nos tornar referência na fabricação ║")
    print("║      de máquinas de bebida, expandindo      ║")
    print("║     o nicho para além do café e estando     ║")
    print("║   sempre presente nas pausas para o café.   ║")
    print("║                                             ║")
    print("║   ★ ┅┅┅┅┅┅┅┅┅┅┅┅┅ Valores ┅┅┅┅┅┅┅┅┅┅┅┅┅ ★   ║")
    print("║                                             ║")
    print("║                 Praticidade                 ║")
    print("║                 Organização                 ║")
    print("║                   Conforto                  ║")
    print("║                  Qualidade                  ║")
    print("║              Ética sustentável              ║")
    print("║          Compromisso com o cliente          ║")
    print("║                                             ║")
    print("║   ★ ┅┅┅┅┅┅┅┅┅ Desenvolvedores ┅┅┅┅┅┅┅┅┅ ★   ║")
    print("║                                             ║")
    print("║           ★ Leandro Alves Vieira            ║")
    print("║               ★ Mateus Fagian               ║")
    print("║      ★ Victor Ming Hur dos Santos Tsai      ║")
    print("║                                             ║")
    print("╚═════════════════════════════════════════════╝")
    print()
    input("Pressione qualquer tecla para voltar ")

def infEspresso():
    '''
    Função que exibe as informações do Espresso.

    Esta função imprime as informações do Espresso nos tamanhos (P), (M) e (G).
    '''
    limpaTela()
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║   ★ ┅┅┅┅┅┅┅┅┅┅┅┅ Espresso ┅┅┅┅┅┅┅┅┅┅┅┅ ★    ║")
    print("║                                             ║")
    print("║ Espresso (P)                                ║")
    print("║ Café solúvel: 2 g                           ║")
    print("║ Água: 50 mL                                 ║")
    print("║ Preço: R$ 3,50                              ║")
    print("║                                             ║")
    print("║ Espresso (M)                                ║")
    print("║ Café solúvel: 4 g                           ║")
    print("║ Água: 100 mL                                ║")
    print("║ Preço: R$ 4,90                              ║")
    print("║                                             ║")
    print("║ Espresso (G)                                ║")
    print("║ Café solúvel: 6 g                           ║")
    print("║ Água: 150 mL                                ║")
    print("║ Preço: R$ 5,60                              ║")
    print("║                                             ║")
    print("║     <-- Voltar (1) (0) (2) Avançar -->      ║")
    print("║                    Sair                     ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def infCafePreto():
    '''
    Função que exibe as informações do Café Preto.

    Esta função imprime as informações do Café Preto nos tamanhos (P), (M) e (G).
    '''
    limpaTela()
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║   ★ ┅┅┅┅┅┅┅┅┅┅┅ Café Preto ┅┅┅┅┅┅┅┅┅┅┅ ★    ║")
    print("║                                             ║")
    print("║ Café Preto (P)                              ║")
    print("║ Café solúvel: 0,75 g                        ║")
    print("║ Água: 50 mL                                 ║")
    print("║ Preço: R$ 2,50                              ║")
    print("║                                             ║")
    print("║ Café Preto (M)                              ║")
    print("║ Café solúvel: 1,50 g                        ║")
    print("║ Água: 100 mL                                ║")
    print("║ Preço: R$ 3,50                              ║")
    print("║                                             ║")
    print("║ Café Preto (G)                              ║")
    print("║ Café solúvel: 2,25 g                        ║")
    print("║ Água: 150 mL                                ║")
    print("║ Preço: R$ 4,00                              ║")
    print("║                                             ║")
    print("║     <-- Voltar (1) (0) (2) Avançar -->      ║")
    print("║                    Sair                     ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def infLatte():
    '''
    Função que exibe as informações do Latte.

    Esta função imprime as informações do Latte nos tamanhos (P), (M) e (G).
    '''
    limpaTela()
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║   ★ ┅┅┅┅┅┅┅┅┅┅┅┅┅┅ Latte ┅┅┅┅┅┅┅┅┅┅┅┅┅┅ ★   ║")
    print("║                                             ║")
    print("║ Latte (P)                                   ║")
    print("║ Café solúvel: 0,75 g                        ║")
    print("║ Leite em pó: 12 g                           ║")
    print("║ Água: 50 mL                                 ║")
    print("║ Preço: R$ 3,50                              ║")
    print("║                                             ║")
    print("║ Latte (M)                                   ║")
    print("║ Café solúvel: 1,50 g                        ║")
    print("║ Leite em pó: 24 g                           ║")
    print("║ Água: 100 mL                                ║")
    print("║ Preço: R$ 4,90                              ║")
    print("║                                             ║")
    print("║ Latte (G)                                   ║")
    print("║ Café solúvel: 2,25 g                        ║")
    print("║ Leite em pó: 36 g                           ║")
    print("║ Água: 150 mL                                ║")
    print("║ Preço: R$ 5,60                              ║")
    print("║                                             ║")
    print("║     <-- Voltar (1) (0) (2) Avançar -->      ║")
    print("║                    Sair                     ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def infCafeComLeite():
    '''
    Função que exibe as informações do Café com Leite.

    Esta função imprime as informações do Café com Leite nos tamanhos (P), (M) e (G).
    '''
    limpaTela()
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║   ★ ┅┅┅┅┅┅┅┅┅ Café com Leite ┅┅┅┅┅┅┅┅┅ ★    ║")
    print("║                                             ║")
    print("║ Café com Leite (P)                          ║")
    print("║ Café solúvel: 0,75 g                        ║")
    print("║ Leite em pó: 5 g                            ║")
    print("║ Água: 50 mL                                 ║")
    print("║ Preço: R$ 2,75                              ║")
    print("║                                             ║")
    print("║ Café com Leite (M)                          ║")
    print("║ Café solúvel: 1,50 g                        ║")
    print("║ Leite em pó: 10 g                           ║")
    print("║ Água: 100 mL                                ║")
    print("║ Preço: R$ 3,85                              ║")
    print("║                                             ║")
    print("║ Café com Leite (G)                          ║")
    print("║ Café solúvel: 2,25 g                        ║")
    print("║ Leite em pó: 15 g                           ║")
    print("║ Água: 150 mL                                ║")
    print("║ Preço: R$ 4,40                              ║")
    print("║                                             ║")
    print("║     <-- Voltar (1) (0) (2) Avançar -->      ║")
    print("║                    Sair                     ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def infLeiteComCafe():
    '''
    Função que exibe as informações do Leite com Café.

    Esta função imprime as informações do Leite com Café nos tamanhos (P), (M) e (G).
    '''
    limpaTela()
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║   ★ ┅┅┅┅┅┅┅┅┅ Leite com Café ┅┅┅┅┅┅┅┅┅ ★    ║")
    print("║                                             ║")
    print("║ Leite com Café (P)                          ║")
    print("║ Café solúvel: 0,75 g                        ║")
    print("║ Leite em pó: 10 g                           ║")
    print("║ Água: 50 mL                                 ║")
    print("║ Preço: R$ 3,00                              ║")
    print("║                                             ║")
    print("║ Leite com Café (M)                          ║")
    print("║ Café solúvel: 1,50 g                        ║")
    print("║ Leite em pó: 20 g                           ║")
    print("║ Água: 100 mL                                ║")
    print("║ Preço: R$ 4,20                              ║")
    print("║                                             ║")
    print("║ Leite com Café (G)                          ║")
    print("║ Café solúvel: 2,25 g                        ║")
    print("║ Leite em pó: 30 g                           ║")
    print("║ Água: 150 mL                                ║")
    print("║ Preço: R$ 4,80                              ║")
    print("║                                             ║")
    print("║     <-- Voltar (1) (0) (2) Avançar -->      ║")
    print("║                    Sair                     ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def infCappuccino():
    '''
    Função que exibe as informações do Cappuccino.

    Esta função imprime as informações do Cappuccino nos tamanhos (P), (M) e (G).
    '''
    limpaTela()
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║   ★ ┅┅┅┅┅┅┅┅┅┅┅ Cappuccino ┅┅┅┅┅┅┅┅┅┅┅ ★    ║")
    print("║                                             ║")
    print("║ Cappuccino (P)                              ║")
    print("║ Café solúvel: 2 g                           ║")
    print("║ Leite em pó: 10 g                           ║")
    print("║ Chocolate em pó: 2,50 g                     ║")
    print("║ Canela em pó: 0,15 g                        ║")
    print("║ Água: 50 mL                                 ║")
    print("║ Preço: R$ 4,00                              ║")
    print("║                                             ║")
    print("║ Cappuccino (M)                              ║")
    print("║ Café solúvel: 4 g                           ║")
    print("║ Leite em pó: 20 g                           ║")
    print("║ Chocolate em pó: 5 g                        ║")
    print("║ Canela em pó: 0,30 g                        ║")
    print("║ Água: 100 mL                                ║")
    print("║ Preço: R$ 5,60                              ║")
    print("║                                             ║")
    print("║ Cappuccino (G)                              ║")
    print("║ Café solúvel: 6 g                           ║")
    print("║ Leite em pó: 30 g                           ║")
    print("║ Chocolate em pó: 7,50 g                     ║")
    print("║ Canela em pó: 0,45 g                        ║")
    print("║ Água: 150 mL                                ║")
    print("║ Preço: R$ 6,40                              ║")
    print("║                                             ║")
    print("║     <-- Voltar (1) (0) (2) Avançar -->      ║")
    print("║                    Sair                     ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def infMacchiato():
    '''
    Função que exibe as informações do Macchiato.

    Esta função imprime as informações do Macchiato nos tamanhos (P), (M) e (G).
    '''
    limpaTela()
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║   ★ ┅┅┅┅┅┅┅┅┅┅┅┅ Macchiato ┅┅┅┅┅┅┅┅┅┅┅┅ ★   ║")
    print("║                                             ║")
    print("║ Macchiato (P)                               ║")
    print("║ Café solúvel: 3 g                           ║")
    print("║ Leite em pó: 7 g                            ║")
    print("║ Água: 50 mL                                 ║")
    print("║ Preço: R$ 4,50                              ║")
    print("║                                             ║")
    print("║ Macchiato (M)                               ║")
    print("║ Café solúvel: 6 g                           ║")
    print("║ Leite em pó: 14 g                           ║")
    print("║ Água: 100 mL                                ║")
    print("║ Preço: R$ 6,30                              ║")
    print("║                                             ║")
    print("║ Macchiato (G)                               ║")
    print("║ Café solúvel: 9 g                           ║")
    print("║ Leite em pó: 21 g                           ║")
    print("║ Água: 150 mL                                ║")
    print("║ Preço: R$ 7,20                              ║")
    print("║                                             ║")
    print("║     <-- Voltar (1) (0) (2) Avançar -->      ║")
    print("║                    Sair                     ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def infMocha():
    '''
    Função que exibe as informações do Mocha.

    Esta função imprime as informações do Mocha nos tamanhos (P), (M) e (G).
    '''
    limpaTela()
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║   ★ ┅┅┅┅┅┅┅┅┅┅┅┅┅┅ Mocha ┅┅┅┅┅┅┅┅┅┅┅┅┅┅ ★   ║")
    print("║                                             ║")
    print("║ Mocha (P)                                   ║")
    print("║ Café solúvel: 1 g                           ║")
    print("║ Leite em pó: 5 g                            ║")
    print("║ Chocolate em pó: 5 g                        ║")
    print("║ Água: 50 mL                                 ║")
    print("║ Preço: R$ 4,00                              ║")
    print("║                                             ║")
    print("║ Mocha (M)                                   ║")
    print("║ Café solúvel: 2 g                           ║")
    print("║ Leite em pó: 10 g                           ║")
    print("║ Chocolate em pó: 10 g                       ║")
    print("║ Água: 100 mL                                ║")
    print("║ Preço: R$ 5,60                              ║")
    print("║                                             ║")
    print("║ Mocha (G)                                   ║")
    print("║ Café solúvel: 3 g                           ║")
    print("║ Leite em pó: 15 g                           ║")
    print("║ Chocolate em pó: 15 g                       ║")
    print("║ Água: 150 mL                                ║")
    print("║ Preço: R$ 6,40                              ║")
    print("║                                             ║")
    print("║     <-- Voltar (1) (0) (2) Avançar -->      ║")
    print("║                    Sair                     ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def infChocoQuente():
    '''
    Função que exibe as informações do Chocolate Quente.

    Esta função imprime as informações do Chocolate Quente nos tamanhos (P), (M) e (G).
    '''
    limpaTela()
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║   ★ ┅┅┅┅┅┅┅┅ Chocolate Quente ┅┅┅┅┅┅┅┅ ★    ║")
    print("║                                             ║")
    print("║ Chocolate Quente (P)                        ║")
    print("║ Leite em pó: 8 g                            ║")
    print("║ Chocolate em pó: 5 g                        ║")
    print("║ Água: 50 mL                                 ║")
    print("║ Preço: R$ 3,75                              ║")
    print("║                                             ║")
    print("║ Chocolate Quente (M)                        ║")
    print("║ Leite em pó: 16 g                           ║")
    print("║ Chocolate em pó: 10 g                       ║")
    print("║ Água: 100 mL                                ║")
    print("║ Preço:  R$ 5,25                             ║")
    print("║                                             ║")
    print("║ Chocolate Quente (G)                        ║")
    print("║ Leite em pó: 24 g                           ║")
    print("║ Chocolate em pó: 15 g                       ║")
    print("║ Água: 150 mL                                ║")
    print("║ Preço: R$ 6,00                              ║")
    print("║                                             ║")
    print("║     <-- Voltar (1) (0) (2) Avançar -->      ║")
    print("║                    Sair                     ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def telaInfProd():
    '''
    Função que controla a exibição das impormações dos produtos.

    Esta função navega entre as informações dos produtos conforme o usuário digita se quer avançar, voltar ou sair.
    '''
    cont = 1
    while True:
        match cont:
            case 1:
                infEspresso()
            case 2:
                infCafePreto()
            case 3:
                infLatte()
            case 4:
                infCafeComLeite()
            case 5:
                infLeiteComCafe()
            case 6:
                infCappuccino()
            case 7:
                infMacchiato()
            case 8:
                infMocha()
            case 9:
                infChocoQuente()
        print("Deseja avaçar, voltar ou sair? ", end="")
        scroll = digitarIntPositivo()
        if scroll == 1:
            cont = cont - 1
        elif scroll == 2:
            cont = cont + 1
        elif scroll == 0:
            break
        else:
            print()
            print("Parâmetro inválido!")
            time.sleep(1)
        if cont == 0:
            cont = 9
        if cont == 10:
            cont = 1
                
def somarLista(a, b):
    '''
    Função que soma duas listas

    Esta função recebe duas listas, verifica o tamanho da primeira e soma termo a termo com a segunda

    Argumentos:
        a (list): A primeira lista que terá seus valores acrescidos
        b (list): A segunda lista que terá seus valores somados a primeira
    '''
    for i in range(len(a)):
        a[i] = a[i] + b[i]

def subtrairLista(a, b):
    '''
    Função que subtrai duas listas

    Esta função recebe duas listas, verifica o tamanho da primeira e subtrai termo a termo com a segunda

    Argumentos:
        a (list): A primeira lista que terá seus valores decrescidos
        b (list): A segunda lista que terá seus valores subtraidos a primeira
    '''
    for i in range(len(a)):
        a[i] = a[i] - b[i]

def digitarIntPositivo():
    '''
    Função que verifica o valor digitado e o retorna se for inteiro positivo

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
            print()
            print("Parâmetro inválido!")
            print()
    except:
        print()
        print("Parâmetro inválido!")
        print()

def verQuantNum(num):
    '''
    Função que verifica quantos algarismos tem no número.

    Esta função recebe uma várial numerica e vefica quantos digitos a compõe.

    Argumentos:
        num (float): número a ser verificados quantos digitos a compõe.

    Retorna:
        int: quantidade de digitos a compõe o número dado como argumento.
    '''
    if num // 10 < 1:
        return 1
    else:
        return 1 + verQuantNum(num // 10)

def somarDinheiro(din, listaVal, listaDinCliente):
    '''
    Função que recebe dinheiro do cliente.

    Esta função recebe duas listas, pergunta quantas notas ou moedas foram inseridas de cada valor correspondente as posições da primeira lista e armazena essa quantidade na segunda lista.
    Se o cliente já tiver colocado dinhero na máquina antes, este valor é acrescido a nova quantidade.

    Argumentos:
        din (float): dinheiro total do cliente
        listaVal (list): lista que contém os valores das notas e das moedas
        listaDinCliente (list): lista que armazenará a quantidade de dinheiro do cliente
    '''
    for i in range(12):
        telaDinCliente(din)
        while True:
            if i <= 5:
                print(f"Digite a quantidade de notas de R$ {listaVal[i]}: ",end="")
            else:
                print(f"Digite a quantidade de moedas de R$ {listaVal[i]}: ",end="")
            val = digitarIntPositivo()
            if val != None:
                if val >= 0:
                    listaDinCliente[i] = val
                    din = din + listaVal[i] * val
                    break
    print()

def dinCliente(listaVal, listaDinCliente):
    '''
    Função que calcula o dinheiro do cliente.

    Esta função recebe duas lista, a primeira com o valor de cada nota e moeda, a segunda com a quantidade que o cliente tem de cada um desses valores. 
    Depois multiplica termo a termo a primeira pela segunda e soma a uma variável com o total.

    Argumentos:
        listaVal (list): Lista que contém os valores das notas e das moedas.
        listaDinCliente (list): Lista com a quantidade de dinheiro do cliente.

    Retorna:
        float: A soma de todo dinheiro do cliente.
    '''
    din = 0
    for i in range(len(listaDinCliente)):
        din = din + listaDinCliente[i] * listaVal[i]
    return din

def verificarCaixa(troco, listaVal, listaCaixa, listaDinCliente):
    '''
    Função que verifica se tem dinheiro para troco no caixa da máquina.

    Esta função recebe o valor do troco que tem que dar para o cliente, a lista com os valores das notas e das moedas, a lista com a quantidade de notas e moedas no caixa da máquina e a lista com a quantidade de dinheiro do cliente
    Chama a função somarLista para colocar o dinheiro do cliente no caixa da empresa.
    Faz a verificação termo a termo da lista do caixa para dar o troco para o cliente.
    Volta a lista do caixa ao normal. E se tiver troco, retorna True, se não, retorna False.

    Argumentos:
        troco (float): valor a ser verificado se tem troco no caixa.
        listaVal (list): lista que contém os valores das notas e das moedas.
        listaCaixa (list): lista que contém a quantidade de notas e moedas no caixa da máquina.
        listaDinCliente (list): lista que contém a quantidade de dinheiro do cliente.

    Retorna:
        bool: True se tiver dinheiro no caixa, False se não tiver dinheiro no caixa.
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
    Função que dá o troco para o cliente.

    Esta função recebe a quantidade de troco que deve ser dado ao cliente, imprime esses valores, nota por nota e centavo por centavo.
    Retira a mesma quantidade de nota e moedas do caixa.

    Argumentos:
        troco (float): Valor que precisa dar de troco ao cliente.
        listaVal (list): Lista que contém os valores das notas e das moedas.
        listaCaixa (list): Lista que contém a quantidade de notas e moedas no caixa da máquina.
    '''
    i = 0
    troco = round(troco, 2)
    print()
    print("Acompanhe seu troco: ")
    while troco != 0:
        if i > 11:
            break
        elif listaCaixa[i] == 0 or (troco - listaVal[i]) < 0:
            i = i + 1
        else:
            print(f"R$ {listaVal[i]:.2f}".replace(".",","))
            troco = round(troco - listaVal[i], 2)
            listaCaixa[i] = listaCaixa[i] - 1
            time.sleep(0.1)
    time.sleep(3)

def verificaTam():
    '''
    Função que pergunta qual o tamanho da bebida do cliente.

    Esta função pergunta qual o tamanho da bebida do cliente e verifica se o valor é válido.

    Retorna:
        float: retorna um valor a ser multiplicado no preço da bebida conforme o tamanho ou 0 que fará voltar no menu.
    '''
    while True:
        tam = str(input("Qual o tamanho da sua bebida? "))
        if tam == "P" or tam == "p" or tam == "1" or tam == "50":
            return 1
        elif tam == "M" or tam == "m" or tam == "2" or tam == "100":
            return 1.4
        elif tam == "G" or tam == "g" or tam == "3" or tam == "150":
            return 1.6
        elif tam == "0":
            return 0
        else:
            print()
            print("Parámetro inválido!")
            print()

def verificaDesc():
    '''
    Função que pergunta se a bebida será descafeinada.

    Função que pergunta se a bebida será descafeinada e verifica se o valor digitado é válido.
    '''
    while True:
        desc = str(input("Gostaria da sua bebida descafeinada? "))
        if desc == "S" or desc == "s" or desc == "1" or desc == "D" or desc == "d":
            return 1
        elif desc == "N" or desc == "n" or desc == "2" or desc == "C" or desc == "c":
            return 0
        elif desc == "0":
            return 2
        else:
            print()
            print("Parâmetro inválido!")
            print()

def verificaDisp(tam, listaPosicao, statusProd, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente):
    '''
    Função que verifica se o produto está disponível.

    Esta função recebe o tamanho, a lista da posição, o status de disponibilidade e as listas dos produtos. Imprime na tela do termina qual produto está disponível e indisponível.

    Argumentos:
        tam (float): valor que representa o tamanho do produto.
        listaPosição (list): lista com a ordem que ficará organizado os produtos.
        statusProd (list): lista com o status de disponibilidade de cada produto.
        prodEspresso (list): lista com as informções do produto 'Espresso'.
        prodCafePreto (list): lista com as informções do produto 'Café Preto'.
        prodLatte (list): lista com as informções do produto 'Latte'.
        prodCafeComLeite (list): lista com as informções do produto 'Café com Leite'.
        prodLeiteComCafe (list): lista com as informções do produto 'Leite com Café'.
        prodCappuccino (list): lista com as informções do produto 'Cappuccino'.
        prodMacchiato (list): lista com as informções do produto 'Macchiato'.
        prodMocha (list): lista com as informções do produto 'Mocha'.
        prodChocoQuente (list): lista com as informções do produto 'Chocolate Quente'.
    '''
    limpaTela()
    xicaraG()
    print("╔════╩═══════════════════════════════════╩════╗")
    print("║   ★ ┅┅┅┅┅ Escolha uma das bebidas ┅┅┅┅┅ ★   ║")
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
    print()

def escolheProd(listaPosicao, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente):
    '''
    Função que pergunta qual o produto que o cliente deseja.

    Esta função pergunta qual o produto que o cliente deseja, verifica qual é de acordo com a posição e retorna a lista do produto ou 0 se não for escolhido nada.
    
    Argumentos:
        listaPosição (list): lista com a ordem que está organizado os produtos na tela de bebidas.
        prodEspresso (list): lista com as informções do produto 'Espresso'.
        prodCafePreto (list): lista com as informções do produto 'Café Preto'.
        prodLatte (list): lista com as informções do produto 'Latte'.
        prodCafeComLeite (list): lista com as informções do produto 'Café com Leite'.
        prodLeiteComCafe (list): lista com as informções do produto 'Leite com Café'.
        prodCappuccino (list): lista com as informções do produto 'Cappuccino'.
        prodMacchiato (list): lista com as informções do produto 'Macchiato'.
        prodMocha (list): lista com as informções do produto 'Mocha'.
        prodChocoQuente (list): lista com as informções do produto 'Chocolate Quente'.

    Retorna:
        list: lista do produto escolido pelo cliente.
        int: 0 se não for escolhido nenhum produto.
    '''
    cod = None
    while cod == None or cod < 0 or cod > 9:
        print("Digite o número da sua bebida: ", end="")
        cod = digitarIntPositivo()
        if cod != None:
            if cod < 0 or cod > 9:
                print()
                print("Parâmetro inválido!")
                print()
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

def vendaDoProduto(din, tam, desc, agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG, prodCliente, listaCaixa, listaDinCliente):
    '''
    Função que vende o produto.

    Esta função verifica o tipo de produto, tamanho e tipo de preparo, logo após debita esses valores do reservatório da máquina.

    Argumentos:
        din (float): soma total do dinheiro do cliente.
        tam (float): tamanho da bebida escolhida do cliente.
        desc (int): tipo de preparo da bebida (cafeinado ou descafeinado).
        agua (int): variável com a quantidade de água.
        cafeSol (float): variável com a quantidade de café solúvel.
        cafeSolDesc (float): variável com a quantidade de café solúvel descafeinado.
        leitePo (float): variável com a quantidade de leite em pó.
        chocoPo (float): variável com a quantidade de chocolate em pó.
        canela (float): variável com a quantidade de canela.
        copoP (int): variável com a quantidade de copos de tamanho (P).
        copoM (int): variável com a quantidade de copos de tamanho (M).
        copoG (int): variável com a quantidade de copos de tamanho (G).
        prodCliente (list): lista com o produto que o cliente escolheu.
        listaCaixa (list): lista com quantidade de notas e moedas do caixa.
        listaDinCliente (list): lista com a quantidade de notas e moedas do cliente.

    Retorna:
        tuple: Uma tupla com o seguintes valores:
            din (float): Dinheiro do cliente atualizado.
            agua (int): Água atualizada.
            cafeSol (float): Café solúvel atualizado.
            cafeSolDesc (float): Café solúvel descafeinado atualizado.
            leitePo (float): Leite em pó atualizado.
            chocoPo (float): Chocolate em pó atualizado.
            canela (float): Canela em pó atualizada.
            copoP (int): Número de copos (P) atualizado.
            copoM (int): Número de copos (M) atualizado.
            copoG (int): Número de copos (G) atualizado.
            listaDinCliente (list): Lista com a quantidade de notas e moedas do cliente zerado.
    '''
    if desc == 1:
        if tam == 1:
            cafeSolDesc = cafeSolDesc - prodCliente[4]
        elif tam == 1.4:
            cafeSolDesc = cafeSolDesc - prodCliente[4] * 2
        else:
            cafeSolDesc = cafeSolDesc - prodCliente[4] * 3
    else:
        if tam == 1:
            cafeSol = cafeSol - prodCliente[4]
        elif tam == 1.4:
            cafeSol = cafeSol - prodCliente[4] * 2
        else:
            cafeSol = cafeSol - prodCliente[4] * 3
    if tam == 1:
        copoP = copoP - 1
        agua = agua - 50
        leitePo = leitePo - prodCliente[5]
        chocoPo = chocoPo - prodCliente[6]
        canela = canela - prodCliente[7]
        prodCliente[8] = prodCliente[8] + 1
    elif tam == 1.4:
        copoM = copoM - 1
        agua = agua - 100
        leitePo = leitePo - prodCliente[5] * 2
        chocoPo = chocoPo - prodCliente[6] * 2
        canela = canela - prodCliente[7] * 2
        prodCliente[9] = prodCliente[9] + 1
    else:
        copoG = copoG - 1
        agua = agua - 150
        leitePo = leitePo - prodCliente[5] * 3
        chocoPo = chocoPo - prodCliente[6] * 3
        canela = canela - prodCliente[7] * 3
        prodCliente[10] = prodCliente[10] + 1
    din = din - prodCliente[2] * tam
    somarLista(listaCaixa, listaDinCliente)
    listaDinCliente = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    prepararBebida(prodCliente)
    return din, agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG, listaDinCliente
        
def organizaPosicao(listaPosicao, statusProd):
    '''
    Função que organiza a posição dos produtos.

    Esta função recebe a lista com a posição dos produtos e outra com o status deles, verifica qual está disponível e reorganiza a posição, colocando os indisponíveis por último.

    Argumentos:
        listaPosicao (list): Lista com a posição dos produtos.
        statusProd (list): Lista com o status de disponibilidade de cada produto.
    '''
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
    '''
    Função que verifica o status dos produtos.

    Esta função faz a verificação se o produto pode ser produzido a depender do tamanho e tipo de preparo da bebida, ajustando a lista de status com base nessas informações.

    Argumentos:
        tam (float): tamanho da bebida escolhida do cliente.
        desc (int): tipo de preparo da bebida (cafeinado ou descafeinado).
        statusProd (list): Lista com o status de disponibilidade de cada produto.
        cafeSol (float): variável com a quantidade de café solúvel.
        cafeSolDesc (float): variável com a quantidade de café solúvel descafeinado.
        leitePo (float): variável com a quantidade de leite em pó.
        chocoPo (float): variável com a quantidade de chocolate em pó.
        canela (float): variável com a quantidade de canela.
        prodEspresso (list): lista com as informções do produto 'Espresso'.
        prodCafePreto (list): lista com as informções do produto 'Café Preto'.
        prodLatte (list): lista com as informções do produto 'Latte'.
        prodCafeComLeite (list): lista com as informções do produto 'Café com Leite'.
        prodLeiteComCafe (list): lista com as informções do produto 'Leite com Café'.
        prodCappuccino (list): lista com as informções do produto 'Cappuccino'.
        prodMacchiato (list): lista com as informções do produto 'Macchiato'.
        prodMocha (list): lista com as informções do produto 'Mocha'.
        prodChocoQuente (list): lista com as informções do produto 'Chocolate Quente'.
    '''
    if tam == 1:
        mult = 1
    elif tam == 1.4:
        mult = 2
    else:
        mult = 3
    prodEspresso[3], prodCafePreto[3], prodLatte[3], prodCafeComLeite[3], prodLeiteComCafe[3], prodCappuccino[3], prodMacchiato[3], prodMocha[3], prodChocoQuente[3] = 1, 1, 1, 1, 1, 1, 1, 1, 1
    if desc == 1:
        if prodEspresso[4] * mult > cafeSolDesc:
            prodEspresso[3] = 0
        if prodCafePreto[4] * mult > cafeSolDesc:
            prodCafePreto[3] = 0
        if prodLatte[4] * mult > cafeSolDesc or prodLatte[5] * mult > leitePo:
            prodLatte[3] = 0
        if prodCafeComLeite[4] * mult > cafeSolDesc or prodCafeComLeite[5] * mult > leitePo:
            prodCafeComLeite[3] = 0
        if prodLeiteComCafe[4] * mult > cafeSolDesc or prodLeiteComCafe[5] * mult > leitePo:
            prodLeiteComCafe[3] = 0
        if prodCappuccino[4] * mult > cafeSolDesc or prodCappuccino[5] * mult > leitePo or prodCappuccino[6] * mult > chocoPo or prodCappuccino[7] * mult > canela:
            prodCappuccino[3] = 0
        if prodMacchiato[4] * mult > cafeSolDesc or prodMacchiato[5] * mult > leitePo:
            prodMacchiato[3] = 0
        if prodMocha[4] * mult > cafeSolDesc or prodMocha[5] * mult > leitePo or prodMocha[6] * mult > chocoPo:
            prodMocha[3] = 0
        if prodChocoQuente[4] * mult > cafeSolDesc or prodChocoQuente[5] * mult > leitePo or prodChocoQuente[6] * mult > chocoPo:
            prodChocoQuente[3] = 0
    else:
        if prodEspresso[4] * mult > cafeSol:
            prodEspresso[3] = 0
        if prodCafePreto[4] * mult > cafeSol:
            prodCafePreto[3] = 0
        if prodLatte[4] * mult > cafeSol or prodLatte[5] * mult > leitePo:
            prodLatte[3] = 0
        if prodCafeComLeite[4] * mult > cafeSol or prodCafeComLeite[5] * mult > leitePo:
            prodCafeComLeite[3] = 0
        if prodLeiteComCafe[4] * mult > cafeSol or prodLeiteComCafe[5] * mult > leitePo:
            prodLeiteComCafe[3] = 0
        if prodCappuccino[4] * mult > cafeSol or prodCappuccino[5] * mult > leitePo or prodCappuccino[6] * mult > chocoPo or prodCappuccino[7] * mult > canela:
            prodCappuccino[3] = 0
        if prodMacchiato[4] * mult > cafeSol or prodMacchiato[5] * mult > leitePo:
            prodMacchiato[3] = 0
        if prodMocha[4] * mult > cafeSol or prodMocha[5] * mult > leitePo or prodMocha[6] * mult > chocoPo:
            prodMocha[3] = 0
        if prodChocoQuente[4] * mult > cafeSol or prodChocoQuente[5] * mult > leitePo or prodChocoQuente[6] * mult > chocoPo:
            prodChocoQuente[3] = 0
    statusProd[0], statusProd[1], statusProd[2], statusProd[3], statusProd[4], statusProd[5], statusProd[6], statusProd[7], statusProd[8] = prodEspresso[3], prodCafePreto[3], prodLatte[3], prodCafeComLeite[3], prodLeiteComCafe[3], prodCappuccino[3], prodMacchiato[3], prodMocha[3], prodChocoQuente[3]

def calcFaturamento(prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente):
    '''
    Função que calcula o faturamento da máquina de bebidas.

    Esta função soma todas as bebidas vendidas e retorna quanto foi faturado.

    Argumentos:
        prodEspresso (list): lista com as informções do produto 'Espresso'.
        prodCafePreto (list): lista com as informções do produto 'Café Preto'.
        prodLatte (list): lista com as informções do produto 'Latte'.
        prodCafeComLeite (list): lista com as informções do produto 'Café com Leite'.
        prodLeiteComCafe (list): lista com as informções do produto 'Leite com Café'.
        prodCappuccino (list): lista com as informções do produto 'Cappuccino'.
        prodMacchiato (list): lista com as informções do produto 'Macchiato'.
        prodMocha (list): lista com as informções do produto 'Mocha'.
        prodChocoQuente (list): lista com as informções do produto 'Chocolate Quente'.

    Retorna:
        float: valor do faturamento.
    '''
    fat = 0
    fat = fat + prodEspresso[8] * prodEspresso[2] + prodEspresso[9] * prodEspresso[2] * 1.4 + prodEspresso[10] * prodEspresso[2] * 1.6
    fat = fat + prodCafePreto[8] * prodCafePreto[2] + prodCafePreto[9] * prodCafePreto[2] * 1.4 + prodCafePreto[10] * prodCafePreto[2] * 1.6
    fat = fat + prodLatte[8] * prodLatte[2] + prodLatte[9] * prodLatte[2] * 1.4 + prodLatte[10] * prodLatte[2] * 1.6
    fat = fat + prodCafeComLeite[8] * prodCafeComLeite[2] + prodCafeComLeite[9] * prodCafeComLeite[2] * 1.4 + prodCafeComLeite[10] * prodCafeComLeite[2] * 1.6
    fat = fat + prodLeiteComCafe[8] * prodLeiteComCafe[2] + prodLeiteComCafe[9] * prodLeiteComCafe[2] * 1.4 + prodLeiteComCafe[10] * prodLeiteComCafe[2] * 1.6
    fat = fat + prodCappuccino[8] * prodCappuccino[2] + prodCappuccino[9] * prodCappuccino[2] * 1.4 + prodCappuccino[10] * prodCappuccino[2] * 1.6
    fat = fat + prodMacchiato[8] * prodMacchiato[2] + prodMacchiato[9] * prodMacchiato[2] * 1.4 + prodMacchiato[10] * prodMacchiato[2] * 1.6
    fat = fat + prodMocha[8] * prodMocha[2] + prodMocha[9] * prodMocha[2] * 1.4 + prodMocha[10] * prodMocha[2] * 1.6
    fat = fat + prodChocoQuente[8] * prodChocoQuente[2] + prodChocoQuente[9] * prodChocoQuente[2] * 1.4 + prodChocoQuente[10] * prodChocoQuente[2] * 1.6
    return round(fat, 2)

def reposicaoInsumos(agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG):
    '''
    Função que repõe insumos da máquina de bebidas.

    Esta função permite que seja feita a reposição de insumos da máquina de bebidas.

    Argumentos:
        agua (int): variável com a quantidade de água.
        cafeSol (float): variável com a quantidade de café solúvel.
        cafeSolDesc (float): variável com a quantidade de café solúvel descafeinado.
        leitePo (float): variável com a quantidade de leite em pó.
        chocoPo (float): variável com a quantidade de chocolate em pó.
        canela (float): variável com a quantidade de canela.
        copoP (int): variável com a quantidade de copos de tamanho (P).
        copoM (int): variável com a quantidade de copos de tamanho (M).
        copoG (int): variável com a quantidade de copos de tamanho (G).

    Retorna:
        tuple: retorna uma tupla com os seguintes valores:
            agua (int): Quantidade de água atualizada.
            cafeSol (float): Quantidade de café solúvel atualizada.
            cafeSolDesc (float): Quantidade de café solúvel descafeinado atualizada.
            leitePo (float): Quantidade de leite em pó atualizada.
            chocoPo (float): Quantidade de chocolate em pó atualizada.
            canela (float): Quantidade de canela atualizada.
            copoP (int): Quantidade de copos de tamanho (P) atualizada.
            copoM (int): Quantidade de copos de tamanho (M) atualizada.
            copoG (int): Quantidade de copos de tamanho (G) atualizada.
    '''
    while True:
        telaReposicao(agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG)

        repor = str(input("Digite o número do item para a reposição: "))
        print()
        match repor:
            case "1":
                while True:
                    telaReposicao(agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG)
                    print("Digite a quantidade de água para adicionar (em mL): ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0:
                            agua += x
                            print()
                            print(f"{x}mL de água foram adicionados ao reservatório.")
                            time.sleep(1.5)
                            break 
                    time.sleep(1)
            case "2":
                while True:
                    telaReposicao(agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG)
                    print("Digite a quantidade de café solúvel para adicionar (em g): ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0:
                            cafeSol += x
                            print()
                            print(f"{x}g de café solúvel foram adicionados ao reservatório.")
                            time.sleep(1.5)
                            break 
                    time.sleep(1)
            case "3":
                while True:
                    telaReposicao(agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG)
                    print("Digite a quantidade de café solúvel (descafeinado) para adicionar (em g): ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0:
                            cafeSolDesc += x
                            print()
                            print(f"{x}g de café solúvel descafeinado foram adicionados ao reservatório.")
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "4":
                while True:
                    telaReposicao(agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG)
                    print("Digite a quantidade de leite em pó para adicionar (em g): ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0:
                            leitePo += x
                            print()
                            print(f"{x}g de leite em pó foram adicionados ao reservatório.")
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "5":
                while True:
                    telaReposicao(agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG)
                    print("Digite a quantidade de chocolate em pó para adicionar (em g): ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0:
                            chocoPo += x
                            print()
                            print(f"{x}g de chocolate em pó foram adicionados ao reservatório.")
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "6":
                while True:
                    telaReposicao(agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG)
                    print("Digite a quantidade de canela para adicionar (em g): ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0:
                            canela += x
                            print()
                            print(f"{x}g de canela foram adicionados ao reservatório.")
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "7":
                while True:
                    telaReposicao(agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG)
                    print("Digite a quantidade de copos (tamanho P) para adicionar: ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0:
                            copoP += x
                            print()
                            print(f"{x} copos P foram adicionados ao reservatório.")
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "8":
                while True:
                    telaReposicao(agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG)
                    print("Digite a quantidade de copos (tamanho M) para adicionar: ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0:
                            copoM += x
                            print()
                            print(f"{x} copos M foram adicionados ao reservatório.")
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "9":
                while True:
                    telaReposicao(agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG)
                    print("Digite a quantidade de copos (tamanho G) para adicionar: ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0:
                            copoG += x
                            print()
                            print(f"{x} copos G foram adicionados ao reservatório.")
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "0":
                return agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG
            case _:
                print("Parâmetro inválido!")
                time.sleep(1)

def reposicaoDin(listaVal, listaCaixa):
    '''
    Função que repõe dinheiro do caixa da máquina.

    Esta função repõe uma certa quantidade de notas e moedas definidas pelo usuário no caixa da máquina.

    Argumentos:
        listaVal (list): lista que contém os valores das notas e das moedas.
        listaCaixa (list): lista que contém a quantidade de notas e moedas no caixa da máquina.

    Retorna:
        listaCaixa (list): lista com as novas quantidades de notas e moedas do caixa da máquina.
    '''
    while True:
        telaCaixa(listaVal, listaCaixa)
        repor = str(input("Digite o número do item para a reposição: "))
        print()
        match repor:
            case "1":
                while True:
                    telaCaixa(listaVal, listaCaixa)
                    print("Digite a quantidade de notas de R$ 100,00: ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0 and listaCaixa[0] + x <= 100:
                            listaCaixa[0] = listaCaixa[0] + x
                            print()
                            print(f"{x} notas de R$ 100,00 foram adicionadas ao caixa.")
                            time.sleep(1.5)
                            break
                        elif listaCaixa[0] + x > 100:
                            print()
                            print("Quantidade de notas excede o limite do caixa interno!")
                            print()
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "2":
                while True:
                    telaCaixa(listaVal, listaCaixa)
                    print("Digite a quantidade de notas de R$ 50,00: ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0 and listaCaixa[1] + x <= 100:
                            listaCaixa[1] = listaCaixa[1] + x
                            print()
                            print(f"{x} notas de R$ 50,00 foram adicionadas ao caixa.")
                            time.sleep(1.5)
                            break
                        elif listaCaixa[1] + x > 100:
                            print()
                            print("Quantidade de notas excede o limite do caixa interno!")
                            print()
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "3":
                while True:
                    telaCaixa(listaVal, listaCaixa)
                    print("Digite a quantidade de notas de R$ 20,00: ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0 and listaCaixa[2] + x <= 100:
                            listaCaixa[2] = listaCaixa[2] + x
                            print()
                            print(f"{x} notas de R$ 20,00 foram adicionadas ao caixa.")
                            time.sleep(1.5)
                            break
                        elif listaCaixa[2] + x > 100:
                            print()
                            print("Quantidade de notas excede o limite do caixa interno!")
                            print()
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "4":
                while True:
                    telaCaixa(listaVal, listaCaixa)
                    print("Digite a quantidade de notas de R$ 10,00: ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0 and listaCaixa[3] + x <= 100:
                            listaCaixa[3] = listaCaixa[3] + x
                            print()
                            print(f"{x} notas de R$ 10,00 foram adicionadas ao caixa.")
                            time.sleep(1.5)
                            break
                        elif listaCaixa[3] + x > 100:
                            print()
                            print("Quantidade de notas excede o limite do caixa interno!")
                            print()
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "5":
                while True:
                    telaCaixa(listaVal, listaCaixa)
                    print("Digite a quantidade de notas de R$ 5,00: ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0 and listaCaixa[4] + x <= 100:
                            listaCaixa[4] = listaCaixa[4] + x
                            print()
                            print(f"{x} notas de R$ 5,00 foram adicionadas ao caixa.")
                            time.sleep(1.5)
                            break
                        elif listaCaixa[4] + x > 100:
                            print()
                            print("Quantidade de notas excede o limite do caixa interno!")
                            print()
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "6":
                while True:
                    telaCaixa(listaVal, listaCaixa)
                    print("Digite a quantidade de notas de R$ 2,00: ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0 and listaCaixa[5] + x <= 100:
                            listaCaixa[5] = listaCaixa[5] + x
                            print()
                            print(f"{x} notas de R$ 2,00 foram adicionadas ao caixa.")
                            time.sleep(1.5)
                            break
                        elif listaCaixa[5] + x > 100:
                            print()
                            print("Quantidade de notas excede o limite do caixa interno!")
                            print()
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "7":
                while True:
                    telaCaixa(listaVal, listaCaixa)
                    print("Digite a quantidade de moedas de R$ 1,00: ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0 and listaCaixa[6] + x <= 100:
                            listaCaixa[6] = listaCaixa[6] + x
                            print()
                            print(f"{x} moedas de R$ 1,00 foram adicionadas ao caixa.")
                            time.sleep(1.5)
                            break
                        elif listaCaixa[6] + x > 100:
                            print()
                            print("Quantidade de moedas excede o limite do caixa interno!")
                            print()
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "8":
                while True:
                    telaCaixa(listaVal, listaCaixa)
                    print("Digite a quantidade de moedas de R$ 0,50: ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0 and listaCaixa[7] + x <= 100:
                            listaCaixa[7] = listaCaixa[7] + x
                            print()
                            print(f"{x} moedas de R$ 0,50 foram adicionadas ao caixa.")
                            time.sleep(1.5)
                            break
                        elif listaCaixa[7] + x > 100:
                            print()
                            print("Quantidade de moedas excede o limite do caixa interno!")
                            print()
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "9":
                while True:
                    telaCaixa(listaVal, listaCaixa)
                    print("Digite a quantidade de moedas de R$ 0,25: ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0 and listaCaixa[8] + x <= 100:
                            listaCaixa[8] = listaCaixa[8] + x
                            print()
                            print(f"{x} moedas de R$ 0,25 foram adicionadas ao caixa.")
                            time.sleep(1.5)
                            break
                        elif listaCaixa[8] + x > 100:
                            print()
                            print("Quantidade de moedas excede o limite do caixa interno!")
                            print()
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "10":
                while True:
                    telaCaixa(listaVal, listaCaixa)
                    print("Digite a quantidade de moedas de R$ 0,10: ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0 and listaCaixa[9] + x <= 100:
                            listaCaixa[9] = listaCaixa[9] + x
                            print()
                            print(f"{x} moedas de R$ 0,10 foram adicionadas ao caixa.")
                            time.sleep(1.5)
                            break
                        elif listaCaixa[9] + x > 100:
                            print()
                            print("Quantidade de moedas excede o limite do caixa interno!")
                            print()
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "11":
                while True:
                    telaCaixa(listaVal, listaCaixa)
                    print("Digite a quantidade de moedas de R$ 0,05: ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0 and listaCaixa[10] + x <= 100:
                            listaCaixa[10] = listaCaixa[10] + x
                            print()
                            print(f"{x} moedas de R$ 0,05 foram adicionadas ao caixa.")
                            time.sleep(1.5)
                            break
                        elif listaCaixa[10] + x > 100:
                            print()
                            print("Quantidade de moedas excede o limite do caixa interno!")
                            print()
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "12":
                while True:
                    telaCaixa(listaVal, listaCaixa)
                    print("Digite a quantidade de moedas de R$ 0,01: ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0 and listaCaixa[11] + x <= 100:
                            listaCaixa[11] = listaCaixa[11] + x
                            print()
                            print(f"{x} moedas de R$ 0,01 foram adicionadas ao caixa.")
                            time.sleep(1.5)
                            break
                        elif listaCaixa[11] + x > 100:
                            print()
                            print("Quantidade de moedas excede o limite do caixa interno!")
                            print()
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "0":
                return listaCaixa
            case _:
                print("Parâmetro inválido!")
                time.sleep(1)

def sangria(listaVal, listaCaixa):
    '''
    Função que retira dinheiro do caixa da máquina.

    Esta função retira uma certa quantidade de notas e moedas definidas pelo usuário do caixa da máquina.

    Argumentos:
        listaVal (list): lista que contém os valores das notas e das moedas.
        listaCaixa (list): lista que contém a quantidade de notas e moedas no caixa da máquina.

    Retorna:
        listaCaixa (list): lista com as novas quantidade de notas e moedas do caixa da máquina
    '''
    while True:
        telaCaixa(listaVal, listaCaixa)
        retirar = str(input("Digite o número do item para a retirada da sangria: "))
        print()
        match retirar:
            case "1":
                while True:
                    telaCaixa(listaVal, listaCaixa)
                    print("Digite a quantidade a ser retirada de notas de R$ 100,00: ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0 and listaCaixa[0] - x >= 0:
                            listaCaixa[0] = listaCaixa[0] - x
                            print()
                            print(f"{x} notas de R$ 100,00 foram retiradas ao caixa.")
                            time.sleep(1.5)
                            break
                        elif listaCaixa[0] - x < 0:
                            print()
                            print("Quantidade de notas fica abaixo do mínimo do caixa interno!")
                            print()
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "2":
                while True:
                    telaCaixa(listaVal, listaCaixa)
                    print("Digite a quantidade a ser retirada de notas de R$ 50,00: ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0 and listaCaixa[1] - x >= 0:
                            listaCaixa[1] = listaCaixa[1] - x
                            print()
                            print(f"{x} notas de R$ 50,00 foram retiradas ao caixa.")
                            time.sleep(1.5)
                            break
                        elif listaCaixa[1] - x < 0:
                            print()
                            print("Quantidade de notas fica abaixo do mínimo do caixa interno!")
                            print()
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "3":
                while True:
                    telaCaixa(listaVal, listaCaixa)
                    print("Digite a quantidade a ser retirada de notas de R$ 20,00: ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0 and listaCaixa[2] - x >= 0:
                            listaCaixa[2] = listaCaixa[2] - x
                            print()
                            print(f"{x} notas de R$ 20,00 foram retiradas ao caixa.")
                            time.sleep(1.5)
                            break
                        elif listaCaixa[2] - x < 0:
                            print()
                            print("Quantidade de notas fica abaixo do mínimo do caixa interno!")
                            print()
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "4":
                while True:
                    telaCaixa(listaVal, listaCaixa)
                    print("Digite a quantidade a ser retirada de notas de R$ 10,00: ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0 and listaCaixa[3] - x >= 0:
                            listaCaixa[3] = listaCaixa[3] - x
                            print()
                            print(f"{x} notas de R$ 10,00 foram retiradas ao caixa.")
                            time.sleep(1.5)
                            break
                        elif listaCaixa[3] - x < 0:
                            print()
                            print("Quantidade de notas fica abaixo do mínimo do caixa interno!")
                            print()
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "5":
                while True:
                    telaCaixa(listaVal, listaCaixa)
                    print("Digite a quantidade a ser retirada de notas de R$ 5,00: ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0 and listaCaixa[4] - x >= 0:
                            listaCaixa[4] = listaCaixa[4] - x
                            print()
                            print(f"{x} notas de R$ 5,00 foram retiradas ao caixa.")
                            time.sleep(1.5)
                            break
                        elif listaCaixa[4] - x < 0:
                            print()
                            print("Quantidade de notas fica abaixo do mínimo do caixa interno!")
                            print()
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "6":
                while True:
                    telaCaixa(listaVal, listaCaixa)
                    print("Digite a quantidade a ser retirada de notas de R$ 2,00: ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0 and listaCaixa[5] - x >= 0:
                            listaCaixa[5] = listaCaixa[5] - x
                            print()
                            print(f"{x} notas de R$ 2,00 foram retiradas ao caixa.")
                            time.sleep(1.5)
                            break
                        elif listaCaixa[5] - x < 0:
                            print()
                            print("Quantidade de notas fica abaixo do mínimo do caixa interno!")
                            print()
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "7":
                while True:
                    telaCaixa(listaVal, listaCaixa)
                    print("Digite a quantidade a ser retirada de moedas de R$ 1,00: ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0 and listaCaixa[6] - x >= 0:
                            listaCaixa[6] = listaCaixa[6] - x
                            print()
                            print(f"{x} moedas de R$ 1,00 foram retiradas ao caixa.")
                            time.sleep(1.5)
                            break
                        elif listaCaixa[6] - x < 0:
                            print()
                            print("Quantidade de moedas fica abaixo do mínimo do caixa interno!")
                            print()
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "8":
                while True:
                    telaCaixa(listaVal, listaCaixa)
                    print("Digite a quantidade a ser retirada de moedas de R$ 0,50: ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0 and listaCaixa[7] - x >= 0:
                            listaCaixa[7] = listaCaixa[7] - x
                            print()
                            print(f"{x} moedas de R$ 0,50 foram retiradas ao caixa.")
                            time.sleep(1.5)
                            break
                        elif listaCaixa[7] - x < 0:
                            print()
                            print("Quantidade de moedas fica abaixo do mínimo do caixa interno!")
                            print()
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "9":
                while True:
                    telaCaixa(listaVal, listaCaixa)
                    print("Digite a quantidade a ser retirada de moedas de R$ 0,25: ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0 and listaCaixa[8] - x >= 0:
                            listaCaixa[8] = listaCaixa[8] - x
                            print()
                            print(f"{x} moedas de R$ 0,25 foram retiradas ao caixa.")
                            time.sleep(1.5)
                            break
                        elif listaCaixa[8] - x < 0:
                            print()
                            print("Quantidade de moedas fica abaixo do mínimo do caixa interno!")
                            print()
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "10":
                while True:
                    telaCaixa(listaVal, listaCaixa)
                    print("Digite a quantidade a ser retirada de moedas de R$ 0,10: ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0 and listaCaixa[9] - x >= 0:
                            listaCaixa[9] = listaCaixa[9] - x
                            print()
                            print(f"{x} moedas de R$ 0,10 foram retiradas ao caixa.")
                            time.sleep(1.5)
                            break
                        elif listaCaixa[9] - x < 0:
                            print()
                            print("Quantidade de moedas fica abaixo do mínimo do caixa interno!")
                            print()
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "11":
                while True:
                    telaCaixa(listaVal, listaCaixa)
                    print("Digite a quantidade a ser retirada de moedas de R$ 0,05: ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0 and listaCaixa[10] - x >= 0:
                            listaCaixa[10] = listaCaixa[10] - x
                            print()
                            print(f"{x} moedas de R$ 0,05 foram retiradas ao caixa.")
                            time.sleep(1.5)
                            break
                        elif listaCaixa[10] - x < 0:
                            print()
                            print("Quantidade de moedas fica abaixo do mínimo do caixa interno!")
                            print()
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "12":
                while True:
                    telaCaixa(listaVal, listaCaixa)
                    print("Digite a quantidade a ser retirada de moedas de R$ 0,01: ", end="")
                    x = digitarIntPositivo()
                    if x != None:
                        if x >= 0 and listaCaixa[11] - x >= 0:
                            listaCaixa[11] = listaCaixa[11] - x
                            print()
                            print(f"{x} moedas de R$ 0,01 foram retiradas ao caixa.")
                            time.sleep(1.5)
                            break
                        elif listaCaixa[11] - x < 0:
                            print()
                            print("Quantidade de moedas fica abaixo do mínimo do caixa interno!")
                            print()
                            time.sleep(1.5)
                            break
                    time.sleep(1)
            case "0":
                return listaCaixa
            case _:
                print("Parâmetro inválido!")
                time.sleep(1)

def venda(din, agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente, listaVal, listaCaixa, listaDinCliente, listaPosicao, statusProd):
    '''
    Função que faz a venda da bebida.

    Esta função controla as telas dos menus que aparecem quando o cliente está comprando a bebida, verifica o valor digitado e redireciona para as respectivas funções.

    Argumentos:
        din (float): váriavel com o valor que o cliente colocou na máquina.
        agua (int): variável com a quantidade de água.
        cafeSol (float): variável com a quantidade de café solúvel.
        cafeSolDesc (float): variável com a quantidade de café solúvel descafeinado.
        leitePo (float): variável com a quantidade de leite em pó.
        chocoPo (float): variável com a quantidade de chocolate em pó.
        canela (float): variável com a quantidade de canela.
        copoP (int): variável com a quantidade de copos de tamanho (P).
        copoM (int): variável com a quantidade de copos de tamanho (M).
        copoG (int): variável com a quantidade de copos de tamanho (G).
        prodEspresso (list): lista com as informções do produto 'Espresso'.
        prodCafePreto (list): lista com as informções do produto 'Café Preto'.
        prodLatte (list): lista com as informções do produto 'Latte'.
        prodCafeComLeite (list): lista com as informções do produto 'Café com Leite'.
        prodLeiteComCafe (list): lista com as informções do produto 'Leite com Café'.
        prodCappuccino (list): lista com as informções do produto 'Cappuccino'.
        prodMacchiato (list): lista com as informções do produto 'Macchiato'.
        prodMocha (list): lista com as informções do produto 'Mocha'.
        prodChocoQuente (list): lista com as informções do produto 'Chocolate Quente'.
        listaVal (list): lista que contém os valores das notas e das moedas.
        listaCaixa (list): lista que contém a quantidade de notas e moedas no caixa da máquina.
        listaDinCliente (list): lista que contém a quantidade de dinheiro do cliente.
        listaPosição (list): lista com a ordem dos produtos.
        statusProd (list): Lista com o status de disponibilidade de cada produto.

    Retorna:
        tuple: Retorna uma tupla com os seguintes valores:
            agua (int): Quantidade de água atualizada.
            cafeSol (float): Quantidade de café solúvel atualizada.
            cafeSolDesc (float): Quantidade de café solúvel descafeinado atualizada.
            leitePo (float): Quantidade de leite em pó atualizada.
            chocoPo (float): Quantidade de chocolate em pó atualizada.
            canela (float): Quantidade de canela atualizada.
            copoP (int): Quantidade de copos de tamanho (P) atualizada.
            copoM (int): Quantidade de copos de tamanho (M) atualizada.
            copoG (int): Quantidade de copos de tamanho (G) atualizada.
            prodEspresso (list): lista com as informções do produto 'Espresso' atualizadas.
            prodCafePreto (list): lista com as informções do produto 'Café Preto' atualizadas.
            prodLatte (list): lista com as informções do produto 'Latte' atualizadas.
            prodCafeComLeite (list): lista com as informções do produto 'Café com Leite' atualizadas.
            prodLeiteComCafe (list): lista com as informções do produto 'Leite com Café' atualizadas.
            prodCappuccino (list): lista com as informções do produto 'Cappuccino' atualizadas.
            prodMacchiato (list): lista com as informções do produto 'Macchiato' atualizadas.
            prodMocha (list): lista com as informções do produto 'Mocha' atualizadas.
            prodChocoQuente (list): lista com as informções do produto 'Chocolate Quente' atualizadas.
            listaCaixa (list): lista que contém a quantidade de notas e moedas no caixa da máquina atualizadas.
            listaDinCliente (list): lista que contém a quantidade de dinheiro do cliente atualizado.
    '''
    while True:
        if agua < 50:
            telaMsgSemAgua()
            time.sleep(3)
            if din > 0:
                print("Agradecemos pela preferência!")
                darTroco(din, listaVal, listaCaixa)
            somarLista(listaCaixa, listaDinCliente)
            listaDinCliente = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            return agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente, listaCaixa, listaDinCliente
        #else:
        res = ""
        while True:
            telaTamBeb()
            if res == "S" or res == "s" or res == "1":
                break
            tam = verificaTam()
            if tam == 0:
                if din > 0:
                    print("Agradecemos pela preferência!")
                    darTroco(din, listaVal, listaCaixa)
                somarLista(listaCaixa, listaDinCliente)
                listaDinCliente = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                return agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente, listaCaixa, listaDinCliente
            if tam == 1 and copoP <= 0:
                telaMsgSemCopoP()
                time.sleep(3)
                break
            if tam == 1.4:
                if copoM <= 0:
                    telaMsgSemCopoM()
                    time.sleep(3)
                    break
                if agua < 100:
                    telaMsgSemAguaM()
                    time.sleep(3)
                    break
            if tam == 1.6:
                if copoG <= 0:
                    telaMsgSemCopoG()
                    time.sleep(3)
                    break
                if agua < 150:
                    telaMsgSemAguaG()
                    time.sleep(3)
                    break
            while True:
                telaDescCafe()
                if res == "S" or res == "s" or res == "1":
                    break
                desc = verificaDesc()
                if desc == 2:
                    break
                while True:
                    verificaStatus(tam, desc, statusProd, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente)
                    organizaPosicao(listaPosicao, statusProd)
                    verificaDisp(tam, listaPosicao, statusProd, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente)
                    prodCliente = escolheProd(listaPosicao, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente)
                    if prodCliente == 0:
                        break
                    while prodCliente == 0 or prodCliente[3] == 0:
                        if prodCliente == 0:
                            break
                        telaProdIndisp(prodCliente)
                        verificaDisp(tam, listaPosicao, statusProd, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente)
                        prodCliente = escolheProd(listaPosicao, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente)
                    if prodCliente == 0:
                        break
                    telaConfimacao(prodCliente)
                    res = str(input(f"Deseja preparar {prodCliente[1]}? "))
                    while True:
                        if res == "S" or res == "s" or res == "1":
                            break
                        elif res == "N" or res == "n" or res == "0":
                            break
                        else:
                            print()
                            print("Parâmetro inválido!")
                            print()
                            res = str(input(f"Deseja preparar {prodCliente[1]}? "))
                    if res == "S" or res == "s" or res == "1":
                        if din < prodCliente[2] * tam:
                            print("Insira o dinheiro na máquina")
                            somarDinheiro(din, listaVal, listaDinCliente)
                            din = din + dinCliente(listaVal, listaDinCliente)
                        temTroco = verificarCaixa(din - prodCliente[2] * tam, listaVal, listaCaixa, listaDinCliente)
                        if din >= prodCliente[2] * tam and temTroco == True:
                            din, agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG, listaDinCliente = vendaDoProduto(din, tam, desc, agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG, prodCliente, listaCaixa, listaDinCliente)
                            telaOutraBeb()
                            res = str(input(f"Restam R$ {din:.2f}! Deseja comprar outra bebida? ".replace(".",",")))
                            while True:
                                if res == "S" or res == "s" or res == "1":
                                    break
                                elif res == "N" or res == "n" or res == "0":
                                    break
                                else:
                                    print()
                                    print("Parâmetro inválido!")
                                    print()
                                    res = str(input(f"Restam R$ {din:.2f}! Deseja comprar outra bebida? ".replace(".",",")))
                            if res == "S" or res == "s" or res == "1":
                                break
                        elif din < prodCliente[2] * tam:
                            print("Dinheiro insuficiente!")
                            time.sleep(1)
                        elif temTroco == False:
                            print("Infelizmente a máquina está sem troco para a quantia fornecida.")
                            time.sleep(2)
                        telaPrefencia()
                        print("Agradecemos pela preferência!")
                        somarLista(listaCaixa, listaDinCliente)
                        listaDinCliente = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                        if din <= 0:
                            print("Você não possui troco.")
                        else:
                            darTroco(din, listaVal, listaCaixa)
                        return agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente, listaCaixa, listaDinCliente


def main():
    '''
    Função que controla os menus da máquina de bebidas.

    Esta função controla quais as telas que aparecem para o usuário a depender do valor escolhido pelo mesmo.
    '''
    limpaTela()

    listaVal = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
    listaCaixa = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    listaDinCliente = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    listaPosicao = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    statusProd = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Produtos
    # ProdLista = [ID, nome, preco, status, cafeSoluvel, leitePo, chocoPo, canela, vendas P, vendas M, vendas G]
    prodEspresso = [1, "Café Espresso", 3.5, 1, 2, 0, 0, 0, 0, 0, 0]
    prodCafePreto = [2, "Café Preto", 2.5, 1, 0.75, 0, 0, 0, 0, 0, 0]
    prodLatte = [3, "Latte", 3.5, 1, 0.75, 12, 0, 0, 0, 0, 0]
    prodCafeComLeite = [4, "Café com Leite", 2.75, 1, 0.75, 5, 0, 0, 0, 0, 0]
    prodLeiteComCafe = [5, "Leite com Café", 3, 1, 0.75, 10, 0, 0, 0, 0, 0]
    prodCappuccino = [6, "Cappuccino", 4, 1, 2, 10, 2.5, 0.15, 0, 0, 0]
    prodMacchiato = [7, "Macchiato", 4.5, 1, 3, 7, 0, 0, 0, 0, 0]
    prodMocha = [8, "Mocha", 4, 1, 1, 5, 5, 0, 0, 0, 0]
    prodChocoQuente = [9, "Chocolate Quente", 3.75, 1, 0, 8, 5, 0, 0, 0, 0]

    faturamento = 0
    din = 0
    agua = 300
    cafeSol = 1000
    cafeSolDesc = 1000
    leitePo = 1000
    chocoPo = 1000
    canela = 100
    copoP = 100 # copo de 80ml
    copoM = 100 # copo de 130ml
    copoG = 100 # copo de 180ml

    while True:
        telaInicial()
        menu = str(input("Escolha uma opção: "))
        match menu:
            case "1":
                agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente, listaCaixa, listaDinCliente = venda(din, agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente, listaVal, listaCaixa, listaDinCliente, listaPosicao, statusProd)
            case "2":
                while True:
                    telaConfiguracoes()
                    menuConf = str(input("Escolha uma opção: "))
                    match menuConf:
                        case "1":
                            telaInfInternas(agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente)
                            input(" Pressione qualquer tecla para sair ")
                        case "2":
                            telaInfProd()
                        case "3":
                            agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG = reposicaoInsumos(agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG)
                        case "4":
                            listaCaixa = reposicaoDin(listaVal, listaCaixa)
                        case "5":
                            listaCaixa = sangria(listaVal, listaCaixa)
                        case "0":
                            break
                        case _:
                            print()
                            print("Parâmetro inválido! ")
                            time.sleep(1)

            case "3":
                telaQuemSomos()
            case "4":
                while True:
                    telaFinalizar()
                    sair = str(input("Deseja finalizar o programa? "))
                    if sair == "S" or sair == "s" or sair == "1":
                        telaPrefencia()                        
                        telaInfInternas(agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente)
                        input(" Pressione qualquer tecla para sair ")
                        return None
                    elif sair == "N" or sair == "n" or sair == "0":
                        break
                    else:
                        print()
                        print("Parâmetro inválido!")
                        time.sleep(1)
            case _:
                print()
                print("Parâmetro inválido!")
                time.sleep(1)
main()