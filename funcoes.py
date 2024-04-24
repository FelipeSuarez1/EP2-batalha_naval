import random
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