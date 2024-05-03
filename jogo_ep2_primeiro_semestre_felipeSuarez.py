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

def posicao_suporta(mapa,blocos,lin,col,ori):
    if ori == 'h':
        if col + blocos > len(mapa[lin]):
            return False

        for i in range(blocos):
            if mapa[lin][col + i] != ' ':
                return False

    if ori == 'v':
        if lin + blocos > len(mapa):
            return False
        for i in range(blocos):
            if mapa[lin + i][col] != ' ':
                return False
    return True
def aloca_navios(mapa, blocos):
    tam = len(mapa)
    for tamanho_navio in blocos:
        colocado = False
        while not colocado:
            linha = random.randint(0, tam - 1)
            coluna = random.randint(0, tam - 1)
            orientacao = random.choice(['h', 'v'])
            if posicao_suporta(mapa, tamanho_navio, linha, coluna, orientacao):
                for i in range(tamanho_navio):
                    if orientacao == 'h':
                        mapa[linha][coluna + i] = 'N'
                    else:
                        mapa[linha + i][coluna] = 'N'
                colocado = True
    return mapa

def foi_derrotado(matriz):
    for listas in matriz:
        for l in listas:
            if l == 'N':
                return False
    return True

def cria_visual(n):
    lista = []

    for i in range(n):
        l = ['   ']*n
        lista.append(l)
    return lista

CORES = {
    'reset': '\u001b[0m',
    'red': '\u001b[31m',
    'black': '\u001b[30m',
    'green': '\u001b[32m',
    'yellow': '\u001b[33m',
    'blue': '\u001b[34m',
    'magenta': '\u001b[35m',
    'cyan': '\u001b[36m',
    'white': '\u001b[37m'
}

CONFIGURACAO = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}

PAISES =  {
    'Brasil': {
        'cruzador': 1,
        'torpedeiro': 2,
        'destroyer': 1,
        'couracado': 1,
        'porta-avioes': 1
    }, 
    'França': {
        'cruzador': 3, 
        'porta-avioes': 1, 
        'destroyer': 1, 
        'submarino': 1, 
        'couracado': 1
    },
    'Austrália': {
        'couracado': 1,
        'cruzador': 3, 
        'submarino': 1,
        'porta-avioes': 1, 
        'torpedeiro': 1
    },
    'Rússia': {
        'cruzador': 1,
        'porta-avioes': 1,
        'couracado': 2,
        'destroyer': 1,
        'submarino': 1
    },
    'Japão': {
        'torpedeiro': 2,
        'cruzador': 1,
        'destroyer': 2,
        'couracado': 1,
        'submarino': 1
    }
}

ori = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
ori_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

mapa = cria_mapa(10)
paises = ['Brasil','França','Austrália','Rússia','Japão']
p = ['1','2','3','4','5']
paiscom = random.choice(paises)
navios_pc = []
for navio in PAISES[paiscom]:
    for i in range(PAISES[paiscom][navio]):
        navios_pc.append(CONFIGURACAO[navio])
mapa_pc = aloca_navios(mapa,navios_pc)

tela_primaria = ''' ===================================== 
|                                     |
| Bem-vindo ao INSPER - Batalha Naval |
|                                     |
 =======   xxxxxxxxxxxxxxxxx   ======= '''

mensagem_inicio = f'Iniciando o jogo!\n\nComputador está alocando os navios de guerra do país {paiscom}...\nComputador já está em posição de batalha!'

config = '''
1: Brasil
   1 cruzador
   2 torpedeiro
   1 destroyer
   1 couracado
   1 porta-avioes

2: França
   3 cruzador
   1 porta-avioes
   1 destroyer
   1 submarino
   1 couracado

3: Austrália
   1 couracado
   3 cruzador
   1 submarino
   1 porta-avioes
   1 torpedeiro

4: Rússia
   1 cruzador
   1 porta-avioes
   2 couracado
   1 destroyer
   1 submarino

5: Japão
   2 torpedeiro
   1 cruzador
   2 destroyer
   1 couracado
   1 submarino
'''

print(f'{tela_primaria}\n\n{mensagem_inicio}\n{config}')

jogador = input('Qual o número da nação da sua frota? ')
while jogador not in p:
    print('Opção inválida')
    jogador = input('Qual o número da nação da sua frota? ')
print(f'Você escolheu a nação {paises[int(jogador)-1]}!\nAgora é sua vez de alocar seus navios de guerra!')
paisjog = paises[int(jogador)-1]


x = '▓▓▓'

computador_visual = cria_visual(10)
jogador_visual = cria_visual(10)
mapa_jogador = cria_mapa(10)

alocar = []
for navio in PAISES[paisjog]:
    for i in range(PAISES[paisjog][navio]):
        alocar.append(navio)



for i in range(len(alocar)):


    tela = [f'''  COMPUTADOR - {paiscom}                   JOGADOR - {paisjog}
     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J ''']
    for i in range(9):
        tela.append(f'  {i+1} {computador_visual[i][0]}{computador_visual[i][1]}{computador_visual[i][2]}{computador_visual[i][3]}{computador_visual[i][4]}{computador_visual[i][5]}{computador_visual[i][6]}{computador_visual[i][7]}{computador_visual[i][8]}{computador_visual[i][9]} {i+1}    {i+1} {jogador_visual[i][0]}{jogador_visual[i][1]}{jogador_visual[i][2]}{jogador_visual[i][3]}{jogador_visual[i][4]}{jogador_visual[i][5]}{jogador_visual[i][6]}{jogador_visual[i][7]}{jogador_visual[i][8]}{jogador_visual[i][9]} {i+1}')
    i+=1
    tela.append(f' 10 {computador_visual[i][0]}{computador_visual[i][1]}{computador_visual[i][2]}{computador_visual[i][3]}{computador_visual[i][4]}{computador_visual[i][5]}{computador_visual[i][6]}{computador_visual[i][7]}{computador_visual[i][8]}{computador_visual[i][9]} 10  10 {jogador_visual[i][0]}{jogador_visual[i][1]}{jogador_visual[i][2]}{jogador_visual[i][3]}{jogador_visual[i][4]}{jogador_visual[i][5]}{jogador_visual[i][6]}{jogador_visual[i][7]}{jogador_visual[i][8]}{jogador_visual[i][9]} 10')
    tela.append('     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J')
    for a in tela:
        print(a)
  

    blocos = CONFIGURACAO[alocar[0]]
    print(f'Alocar: {alocar[0]} ({blocos} blocos)')
    del alocar[0]
    

    posicao = False

    while posicao == False:
        se = False

        while se == False:
            letra = input('Informe a letra:')
            letra = letra.upper()
            if letra not in ori:
                print('Letra inválida')
            else:
                se = True
        
        se = False
        while se == False:
            linha = input('Informe a linha: ')
            if linha not in ori_num:
                print('Linha inválida')
            else:
                se = True

        se = False
        while se == False:
            orientacao = input('Informe a orientação [v/h]: ')
            orientacao.lower()
            if orientacao != 'v' and orientacao != 'h':
                print('Orientação inválida')
            else:
                se = True

        l = int(linha)-1
        c = ori[letra]
        posicao = posicao_suporta(mapa_jogador,blocos,l,c,orientacao)
        if posicao == False:
            print(f'Não foi possivel alocar o navio em {letra}{linha} {orientacao}')
          
            tela = [f'''  COMPUTADOR - {paiscom}                   JOGADOR - {paisjog}
     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J ''']
            for i in range(9):
                tela.append(f'  {i+1} {computador_visual[i][0]}{computador_visual[i][1]}{computador_visual[i][2]}{computador_visual[i][3]}{computador_visual[i][4]}{computador_visual[i][5]}{computador_visual[i][6]}{computador_visual[i][7]}{computador_visual[i][8]}{computador_visual[i][9]} {i+1}    {i+1} {jogador_visual[i][0]}{jogador_visual[i][1]}{jogador_visual[i][2]}{jogador_visual[i][3]}{jogador_visual[i][4]}{jogador_visual[i][5]}{jogador_visual[i][6]}{jogador_visual[i][7]}{jogador_visual[i][8]}{jogador_visual[i][9]} {i+1}')
            i+=1
            tela.append(f' 10 {computador_visual[i][0]}{computador_visual[i][1]}{computador_visual[i][2]}{computador_visual[i][3]}{computador_visual[i][4]}{computador_visual[i][5]}{computador_visual[i][6]}{computador_visual[i][7]}{computador_visual[i][8]}{computador_visual[i][9]} 10  10 {jogador_visual[i][0]}{jogador_visual[i][1]}{jogador_visual[i][2]}{jogador_visual[i][3]}{jogador_visual[i][4]}{jogador_visual[i][5]}{jogador_visual[i][6]}{jogador_visual[i][7]}{jogador_visual[i][8]}{jogador_visual[i][9]} 10')
            tela.append('     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J')
            for a in tela:
                print(a)
        
                

    print('Foi posicionado!')

    for i in range(blocos):
        if orientacao == 'v':
            mapa_jogador[l+i][c] = 'N'
            jogador_visual[l+i][c] = f'\u001b[32m{x}\u001b[0m'
        elif orientacao == 'h':
            mapa_jogador[l][c+i] = 'N'
            jogador_visual[l][c+i] = f'\u001b[32m{x}\u001b[0m'


print('Iniciando batalha naval!')


vitoria_pc = False
vitoria_jogador = False


restart = 's'
while restart == 's':
    while vitoria_jogador == False and vitoria_pc == False:
   
        tela = [f'''  COMPUTADOR - {paiscom}                   JOGADOR - {paisjog}
     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J ''']
        for i in range(9):
            tela.append(f'  {i+1} {computador_visual[i][0]}{computador_visual[i][1]}{computador_visual[i][2]}{computador_visual[i][3]}{computador_visual[i][4]}{computador_visual[i][5]}{computador_visual[i][6]}{computador_visual[i][7]}{computador_visual[i][8]}{computador_visual[i][9]} {i+1}    {i+1} {jogador_visual[i][0]}{jogador_visual[i][1]}{jogador_visual[i][2]}{jogador_visual[i][3]}{jogador_visual[i][4]}{jogador_visual[i][5]}{jogador_visual[i][6]}{jogador_visual[i][7]}{jogador_visual[i][8]}{jogador_visual[i][9]} {i+1}')
        i+=1
        tela.append(f' 10 {computador_visual[i][0]}{computador_visual[i][1]}{computador_visual[i][2]}{computador_visual[i][3]}{computador_visual[i][4]}{computador_visual[i][5]}{computador_visual[i][6]}{computador_visual[i][7]}{computador_visual[i][8]}{computador_visual[i][9]} 10  10 {jogador_visual[i][0]}{jogador_visual[i][1]}{jogador_visual[i][2]}{jogador_visual[i][3]}{jogador_visual[i][4]}{jogador_visual[i][5]}{jogador_visual[i][6]}{jogador_visual[i][7]}{jogador_visual[i][8]}{jogador_visual[i][9]} 10')
        tela.append('     A  B  C  D  E  F  G  H  I  J          A  B  C  D  E  F  G  H  I  J')
        for a in tela:
            print(a)
    
        print('Cordenadas do seu disparo')

      
        posi = False
        while posi == False:
            c = False
            while c == False:
                letra = input('Informe a letra: ')
                letra = letra.upper()
                if letra not in ori:
                    print('Letra inválida')
                else:
                    c = True
            
            c = False
            while c == False:
                linha = input('Informe a linha: ')
                if linha not in ori_num:
                    print('Linha inválida')
                else:
                    c = True

            l = int(linha)-1
            c = ori[letra]
            if mapa_pc[l][c] != 'B' and mapa_pc[l][c] != 'A':
                posi = True
            else:
                print(f'Posição {letra}{linha} já Bombardeada!')
        if mapa_pc[l][c] == 'N':
            mapa_pc[l][c] = 'B'
            computador_visual[l][c] = f'\u001b[31m{x}\u001b[0m'
        else:
            mapa_pc[l][c] = 'A'
            computador_visual[l][c] = f'\u001b[34m{x}\u001b[0m'
        letra1 = letra
        linha1 = linha

        pos = False
        while pos == False:
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)
            if mapa_jogador[linha][coluna] == ' ' or mapa_jogador[linha][coluna] == 'N':
                pos = True
                if mapa_jogador[linha][coluna] == 'N':
                    mapa_jogador[linha][coluna] = 'B'
                    jogador_visual[linha][coluna] = f'\u001b[31m{x}\u001b[0m'
                elif mapa_jogador[linha][coluna] == ' ':
                    mapa_jogador[linha][coluna] = 'A'
                    jogador_visual[linha][coluna] = f'\u001b[34m{x}\u001b[0m'
            


        ori1 = {}
        for k,v in ori.items():
            ori1[v+1] = k

        
        if mapa_jogador[linha][coluna] == 'A':
            jog = 'Água, AZAR!'
        elif mapa_jogador[linha][coluna] == 'B':
            jog = 'BOOMMM!'
        
        if mapa_pc[l][c] == 'A':
            pc = 'Água, AZAR!'
        elif mapa_pc[l][c] == 'B':
            pc = 'BOOMMM!'


        print(f'Jogador -> {letra1}{linha1}    {pc}\nComputador -> {ori1[coluna+1]}{linha+1}    {jog}')

        vitoria_jogador = foi_derrotado(mapa_pc)
        vitoria_pc = foi_derrotado(mapa_jogador)

        if vitoria_jogador == True:
            print('Você venceu!')
        elif vitoria_pc == True:
            print('Você perdeu!')

    restart = (input('Jogar novamente? [s/n] ')).lower()
    vitoria_pc = False
    vitoria_jogador = False
print('\n\nAté a proxima!')
