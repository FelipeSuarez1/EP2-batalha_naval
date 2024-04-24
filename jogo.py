import funcoes
import random
def cria_mapa(n):
    matriz = []
    lista1 = []
    igual = n
    for i in range(n):
        lista = lista1
        while igual > 0:
            lista1.append(' ')
            igual -= 1
        matriz.append(lista)
    return matriz

lines = [
    " _________________________________________",
    "|                                         |",
    "|   Bem-vindo ao INSPER - Batalha Naval   |",
    "|                                         |",
    " =======  XXXXXXXXXXXXXXXXXXXXX    ======="
]

for line in lines:
    print(line) # printando o bem vindo para o jogador

def game():
    lista_pais = ["Japão","França", "Rússia", "Austrália","Brasil"]
    pais_comp = random.choice(lista_pais)
    
    print("\n")
    print("\n Iniciando o jogo!")
    print("\n Computador está alocando os navios de guerra do país", pais_comp,'...')
    print("\n Computador já está em posição de batalha\n")

    print("1: Brasil \n 1 cruzador \n 2 torpedeiro \n 1 destroyer \n 1 couracado \n 1 porta-avioes\n")
    print("2: França \n 3 cruzador \n 1 porta-avioes \n 1 destroyer \n 1 submarino \n couracado\n")
    print("3: Austrália \n 1 couracado \n 3 cruzador \n 1 submarino \n 1 porta_avioes \n torpedeiro\n")
    print("4: Rússia \n 1 cruzador \n 1 porta-avioes \n 2 couracado \n 1 destroyer \n 1 submarino\n")
    print("5: Japão \n 2 torpedeiro \n 1 cruzador \n 2 destroyer \n couracado \n 1 submarino") 
    resp = int(input("Qual o número da nação da sua frota?"))
    if resp == 1:
        pais = "Brasil"
    elif resp == 2:
        pais = "França"
    elif resp == 3:
        pais = "Austrália"
    elif resp == 4:
        pais = "Rússia"
    elif resp == 5:
        pais = "Japão"
    
    print("Você escolheu a nação", pais)
    print("Agora é a sua vez de alocar seus navios de guerra!\n")
    mapa_tamanho = cria_mapa(10)
    colunas = "ABCDEFGHIJ"
    linhas_mapa = [1,2,3,4,5,6,7,8,9,10]
    print("COMPUTADOR"," ",'-',' ',pais_comp,'                                 ',"COMPUTADOR"," ",'-',' ',pais)
    print('  ' + '  '.join(colunas),'                         ','  ' + '  '.join(colunas))
    for linha in mapa_tamanho:
        print("  ".join(linha),'                         ',"  ".join(linha))
    print("  ","  ".join(colunas),'                         ',"  ".join(colunas))
    
    
game()
