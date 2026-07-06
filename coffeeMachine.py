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

def xicaraG():
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

def telaMsgSemAgua():
    limpaTela()
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
    print("║                                             ║")
    print("║         Infelizmente a máquina está         ║")
    print("║            sem água para bebidas            ║")
    print("║                                             ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def telaMsgSemAguaM():
    limpaTela()
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
    print("║                                             ║")
    print("║         Infelizmente a máquina está         ║")
    print("║        sem água para bebidas médias         ║")
    print("║                                             ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def telaMsgSemAguaG():
    limpaTela()
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
    print("║                                             ║")
    print("║         Infelizmente a máquina está         ║")
    print("║        sem água para bebidas grandes        ║")
    print("║                                             ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def telaMsgSemCopoP():
    limpaTela()
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
    print("║                                             ║")
    print("║         Infelizmente a máquina está         ║")
    print("║   sem copos para bebidas pequenas (50 mL)   ║")
    print("║                                             ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def telaMsgSemCopoM():
    limpaTela()
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
    print("║                                             ║")
    print("║         Infelizmente a máquina está         ║")
    print("║   sem copos para bebidas médias (100 mL)    ║")
    print("║                                             ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def telaMsgSemCopoG():
    limpaTela()
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
    print("║                                             ║")
    print("║         Infelizmente a máquina está         ║")
    print("║   sem copos para bebidas grandes (150 mL)   ║")
    print("║                                             ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def telaProdIndisp(prodCliente):
    limpaTela()
    if len(prodCliente[1]) % 2 == 0:
        passo1 = (42 - len(prodCliente[1])) // 2
        passo2 = passo1 + 1
    else:
        passo1 = (43 - len(prodCliente[1])) // 2
        passo2 = passo1
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
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
    limpaTela()
    if len(prodCliente[1]) % 2 == 0:
        passo1 = (42 - len(prodCliente[1])) // 2
        passo2 = passo1
    else:
        passo1 = (42 - len(prodCliente[1])) // 2
        passo2 = passo1 + 1
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
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
    limpaTela()
    if verQuantNum(din) % 2 == 0:
        passo1 = (37 - verQuantNum(din)) // 2
        passo2 = passo1 + 1
    else:
        passo1 = (37 - verQuantNum(din)) // 2
        passo2 = passo1
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
    print("║   ★ ┅┅┅┅┅┅┅┅┅┅ Dinhero Total ┅┅┅┅┅┅┅┅┅┅ ★   ║")
    print("║                                             ║")
    print("║", " " * passo1,end="")
    print(f"R$ {din:.2f}".replace(".",","),end="")
    print(" " * passo2, "║")
    print("║                                             ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def telaOutraBeb():
    limpaTela()
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
    print("║   ★ ┅┅┅┅┅┅┅┅┅┅ Outra bebida? ┅┅┅┅┅┅┅┅┅┅ ★   ║")
    print("║                                             ║")
    print("║           1. Sim           0. Não           ║")
    print("║                                             ║") 
    print("╚═════════════════════════════════════════════╝")
    print()

def telaFinalizar():
    limpaTela()
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
    print("║   ★ ┅┅┅┅┅┅┅┅ Deseja Finalizar? ┅┅┅┅┅┅┅┅ ★   ║")
    print("║                                             ║")
    print("║           1. Sim           0. Não           ║")
    print("║                                             ║") 
    print("╚═════════════════════════════════════════════╝")
    print()

def telaPrefencia():
    limpaTela()
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
    print("║                                             ║")
    print("║   ★ ┅┅┅┅ Agradecemos a Preferência ┅┅┅┅ ★   ║")
    print("║                                             ║") 
    print("╚═════════════════════════════════════════════╝")
    print()
    time.sleep(2)

def telaInicial():
    limpaTela()
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
    print("║   ★ ┅┅┅┅┅┅┅┅ Escolha uma opção ┅┅┅┅┅┅┅┅ ★   ║")
    print("║ 1. Bebidas                                  ║")            
    print("║ 2. Configurações                            ║")
    print("║ 3. Quem somos                               ║")
    print("║ 4. Finalizar                                ║")  
    print("╚═════════════════════════════════════════════╝")
    print()

def telaTamBeb():
    limpaTela()
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
    print("║   ★ ┅┅┅ Escolha o tamanho da bebida ┅┅┅ ★   ║")
    print("║ 1. Pequeno (P) ---------------------- 50 mL ║")
    print("║ 2. Médio (M) ----------------------- 100 mL ║")
    print("║ 3. Grande (G) ---------------------- 150 mL ║")
    print("║ 0. Voltar                                   ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def telaDescCafe():
    limpaTela()
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
    print("║   ★ ┅┅┅┅ Escolha o tipo de preparo ┅┅┅┅ ★   ║")
    print("║ 1. Descafeinado                             ║")
    print("║ 2. Cafeinado                                ║")
    print("║ 0. Voltar                                   ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def prepararBebida(prodCliente):
    '''
    Função que prepara a bebida do cliente

    Esta função exibe uma mensagem que a bebida do cliente que está sendo preparada e outra que a bebida está pronta
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
    limpaTela()
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
    print("║   ★ ┅┅┅┅┅┅┅┅┅┅ Configurações ┅┅┅┅┅┅┅┅┅┅ ★   ║")
    print("║ 1. Informações internas                     ║")
    print("║ 2. Informações dos produtos                 ║")
    print("║ 3. Reposição                                ║")
    print("║ 0. Voltar                                   ║")
    print("╚═════════════════════════════════════════════╝")
    print()

def telaInfInternas(agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente):
    limpaTela()
    faturamento = calcFaturamento(prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente)
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
    print("║   ★ ┅┅┅┅┅┅ Informações Internas: ┅┅┅┅┅┅ ★   ║")
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
    limpaTela()
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
    print("║   ★ ┅┅┅┅┅┅ Informações Internas: ┅┅┅┅┅┅ ★   ║")
    print(f"║ 1. Água: {agua} mL", end="")
    print(" " * (31 - verQuantNum(agua)), "║")
    print(f"║ 2. Café Solúvel: {cafeSol:.2f} g".replace(".", ","), end="")
    print(" " * (21 - verQuantNum(cafeSol)), "║")
    print(f"║ 3. Café Solúvel Descafeinado: {cafeSolDesc:.2f} g".replace(".", ","), end="")
    print(" " * (8 - verQuantNum(cafeSolDesc)), "║")
    print(f"║ 4. Leite em Pó: {leitePo:.2f} g".replace(".", ","), end="")
    print(" " * (22 - verQuantNum(leitePo)), "║")
    print(f"║ 5. Chocolate em Pó: {chocoPo:.2f} g".replace(".", ","), end="")
    print(" " * (18 - verQuantNum(chocoPo)), "║")
    print(f"║ 6. Canela: {canela:.2f} g".replace(".", ","), end="")
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

""" def telaQuemSomos():
    limpaTela()
    print("                       ★ Bem-vindo à Starcoffee Machine! ★")
    print("                                           ☕")
    print("                   Desenvolvemos máquinas inteligentes que oferecem")
    print("            exímia praticidade e qualidade no preparo de bebidas cotidianas.")
    print("        ")
    print("★ ════════════════════════════════════ Missão ═════════════════════════════════════ ★")
    print("")
    print("  ☕ Oferecer um sistema eficiente e intuitivo no preparo de cafés de qualidade,")
    print("   criando uma experiência confortável entre o usuário e máquina.")
    print("")
    print("★ ═════════════════════════════════════ Visão ═════════════════════════════════════ ★")
    print("")
    print("  ☕ Visamos nos tornar referência na fabricação de máquinas de bebida, expandindo")
    print("   o nicho para além do café e estando sempre presente nas pausas para o café.")
    print("")
    print("★ ════════════════════════════════════ Valores ════════════════════════════════════ ★")
    print("")
    print("  ☕ Praticidade;   ☕ Conforto;   ☕ Compromisso com o cliente;")
    print("  ☕ Organização;   ☕ Qualidade;  ☕ Ética sustentável.")
    print("")
    print("★ ════════════════════════════════ Desenvolvedores ════════════════════════════════ ★")
    print("")
    print("  ★ Leandro Alves Vieira")
    print("  ★ Mateus Fagian")
    print("  ★ Victor Ming Hur dos Santos Tsai")
    print()
    input("Pressione qualquer tecla para sair ") """

def telaQuemSomos():
    limpaTela()
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
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
    print("║               ☕ Praticidade                ║")
    print("║               ☕ Organização                ║")
    print("║                 ☕ Conforto                 ║")
    print("║                ☕ Qualidade                 ║")
    print("║            ☕ Ética sustentável             ║")
    print("║        ☕ Compromisso com o cliente         ║")
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
    Função que exibe as informações do espresso

    Esta função imprime as informações do espresso nos tamanhos (P), (M) e (G)
    '''
    limpaTela()
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
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
    Função que exibe as informações do café preto

    Esta função imprime as informações do café preto nos tamanhos (P), (M) e (G)
    '''
    limpaTela()
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
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
    Função que exibe as informações do latte

    Esta função imprime as informações do latte nos tamanhos (P), (M) e (G)
    '''
    limpaTela()
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
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
    Função que exibe as informações do café com leite

    Esta função imprime as informações do café com leite nos tamanhos (P), (M) e (G)
    '''
    limpaTela()
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
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
    Função que exibe as informações do leite com café

    Esta função imprime as informações do leite com café nos tamanhos (P), (M) e (G)
    '''
    limpaTela()
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
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
    Função que exibe as informações do cappuccino

    Esta função imprime as informações do cappuccino nos tamanhos (P), (M) e (G)
    '''
    limpaTela()
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
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
    Função que exibe as informações do macchiato

    Esta função imprime as informações do macchiato nos tamanhos (P), (M) e (G)
    '''
    limpaTela()
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
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
    Função que exibe as informações do mocha

    Esta função imprime as informações do mocha nos tamanhos (P), (M) e (G)
    '''
    limpaTela()
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
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
    Função que exibe as informações do chocolate quente

    Esta função imprime as informações do chocolate quente nos tamanhos (P), (M) e (G)
    '''
    limpaTela()
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
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
            print()
            print("Parâmetro inválido!")
            print()
    except:
        print()
        print("Parâmetro inválido")
        print()

def verQuantNum(num):
    if num // 10 < 1:
        return 1
    else:
        return 1 + verQuantNum(num // 10)

def somarDinheiro(din, listaVal, listaDinCliente):
    '''
    Função que recebe dinheiro do cliente

    Esta função recebe duas listas, pergunta quantas notas ou moedas foram inseridas de cada valor correspondente as posições da primeira lista e armazena essa quantidade na segunda lista. 
    Chama função digitarIntPositivo para verificar se o número é um inteiro positivo
    
    Argumentos:
        listaVal (lista): Lista que contém os valores das notas e das moedas
        listaDinCliente (lista): Lista que armazenará a quantidade de dinheiro do cliente
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
    time.sleep(3)

def verificaTam():
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
            print("Parâmetro inválido")
            print()

def verificaDisp(tam, listaPosicao, statusProd, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente):
    limpaTela()
    xicaraG()
    print("╔════════╩═══════════════════════════╩════════╗")
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
    print("Digite o número da sua bebida: ", end="")
    cod = digitarIntPositivo()
    while cod == None or cod < 0 or cod > 9:
        print("Digite o número da sua bebida: ", end="")
        cod = digitarIntPositivo()
        if cod == None or cod < 0 or cod > 9:
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
        case _:
            print()
            print("Parâmetro inválido!")
            print()

def compraProd(tam, desc, prodCliente, agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela):
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
        agua = agua - 50
        leitePo = leitePo - prodCliente[5]
        chocoPo = chocoPo - prodCliente[6]
        canela = canela - prodCliente[7]
    elif tam == 1.4:
        agua = agua - 100
        leitePo = leitePo - prodCliente[5] * 2
        chocoPo = chocoPo - prodCliente[6] * 2
        canela = canela - prodCliente[7] * 2
    else:
        agua = agua - 150
        leitePo = leitePo - prodCliente[5] * 3
        chocoPo = chocoPo - prodCliente[6] * 3
        canela = canela - prodCliente[7] * 3
    return agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela 

def vendaDoProduto(din, tam, desc, agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG, prodCliente, listaCaixa, listaDinCliente):
    if tam == 1:
        copoP = copoP - 1
        prodCliente[8] = prodCliente[8] + 1
    elif tam == 1.4:
        copoM = copoM - 1
        prodCliente[9] = prodCliente[9] + 1
    else:
        copoG = copoG - 1
        prodCliente[10] = prodCliente[10] + 1
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

def reposicao(agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG):
    while True:
        telaReposicao(agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG)

        repor = str(input("Digite o número do item para a reposição: "))
        print()
        match repor:
            case "1":
                print("Digite a quantidade de água para adicionar (em mL): ", end="")
                x = digitarIntPositivo()
                agua += x
                print()
                print(f"{x}mL de água foram adicionados ao reservatório.")
                time.sleep(1) 
            case "2":
                print("Digite a quantidade de café solúvel para adicionar (em g): ", end="")
                x = digitarIntPositivo()
                cafeSol += x
                print()
                print(f"{x}g de café solúvel foram adicionados ao reservatório.")
                time.sleep(1)
            case "3":
                print("Digite a quantidade de café solúvel (descafeinado) para adicionar (em g): ", end="")
                x = digitarIntPositivo()
                cafeSolDesc += x
                print()
                print(f"{x}g de café solúvel descafeinado foram adicionados ao reservatório.")
                time.sleep(1)
            case "4":
                print("Digite a quantidade de leite em pó para adicionar (em g): ", end="")
                x = digitarIntPositivo()
                leitePo += x
                print()
                print(f"{x}g de leite em pó foram adicionados ao reservatório.")
                time.sleep(1)
            case "5":
                print("Digite a quantidade de chocolate em pó para adicionar (em g): ", end="")
                x = digitarIntPositivo()
                chocoPo += x
                print()
                print(f"{x}g de chocolate em pó foram adicionados ao reservatório.")
                time.sleep(1)
            case "6":
                print("Digite a quantidade de canela para adicionar (em g): ", end="")
                x = digitarIntPositivo()
                canela += x
                print()
                print(f"{x}g de canela foram adicionados ao reservatório.")
                time.sleep(1)
            case "7":
                print("Digite a quantidade de copos (tamanho P) para adicionar: ", end="")
                x = digitarIntPositivo()
                copoP += x
                print()
                print(f"{x}g de canela foram adicionados ao reservatório.")
                time.sleep(1)
            case "8":
                print("Digite a quantidade de copos (tamanho M) para adicionar: ", end="")
                x = digitarIntPositivo()
                copoM += x
                print()
                print(f"{x}g de canela foram adicionados ao reservatório.")
                time.sleep(1)
            case "9":
                print("Digite a quantidade de copos (tamanho G) para adicionar: ", end="")
                x = digitarIntPositivo()
                copoG += x
                print()
                print(f"{x}g de canela foram adicionados ao reservatório.")
                time.sleep(1)
            case "0":
                return agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG
            case _:
                print("Parâmetro inválido!")
                time.sleep(1)

def venda(din, agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG, prodEspresso, prodCafePreto, prodLatte, prodCafeComLeite, prodLeiteComCafe, prodCappuccino, prodMacchiato, prodMocha, prodChocoQuente, listaVal, listaCaixa, listaDinCliente, listaPosicao, statusProd):
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
                    res = str(input(f"Deseja preparar {prodCliente[1]}? S/N: "))
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
                                    print("Parâmetro inválido")
                                    print()
                                    res = str(input(f"Restam R$ {din:.2f}! Deseja comprar outra bebida? ".replace(".",",")))
                            if res == "S" or res == "s" or res == "1":
                                break
                        elif din < prodCliente[2] * tam:
                            print("Dinheiro insuficiente!")
                            time.sleep(1)
                        elif temTroco == False:
                            print("Infelizmente a máquina está sem troco para a quantia fornecida.")
                            time.sleep(1)
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

    #telaQuemSomos()
    #time.sleep(1000)

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
                            agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG = reposicao(agua, cafeSol, cafeSolDesc, leitePo, chocoPo, canela, copoP, copoM, copoG)
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