import random

#EQUIPE 3 (GRUPO: ANANDA, ANA LETICIA, ANGELICA, FELIPE E LUAN - TURMA A)


#vetor com a localização de cada indice das linhas e colunas
alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

#ordem da matriz quadrada
n = 8

#vetor do jogador 1 (não aparece)
player1 = [None] * n
for i in range (n):
  player1[i] = [None] * n

for i in range (n):
  for j in range (n):
      player1[i][j] = ' '

#vetor do jogador 2 (não aparece)
player2 = [None] * n
for i in range (n):
  player2[i] = [None] * n

for i in range (n):
  for j in range (n):
      player2[i][j] = ' '

#matriz do jogador 1 (aparece)
viewPlayer1 = [None] * n
for i in range (n):
  viewPlayer1[i] = [None] * n

for i in range (n):
  for j in range (n):
      viewPlayer1[i][j] = ' '

#matriz do jogador 2 (aparece)
viewPlayer2 = [None] * n
for i in range (n):
  viewPlayer2[i] = [None] * n

for i in range (n):
  for j in range (n):
      viewPlayer2[i][j] = ' '

#entrada da quantidade de navios nas matrizes
qtdNavios = int(input('Digite quantos navios serão colocados no tabuleiro (máximo 6): '))
while qtdNavios > 6:
  qtdNavios = int(input('Digite uma quantidade de navios dentro do limite (entre 1 a 6): '))

#função para posicionar os navios na matriz de forma aleatória juntamente com a regra do projeto
def posicionarNavio(tab, qtdN):
    naviosposicionados = 0
    while naviosposicionados < qtdN:
        linha = random.randint(0, n - 1)
        coluna = random.randint(0, n - 1)
        # Verifica se a posição está vazia e não tem vizinhos ocupados
        if tab[linha][coluna] == ' ' and not temVizinhosOcupados(tab, linha, coluna):
            tab[linha][coluna] = 'N'
            naviosposicionados += 1

def temVizinhosOcupados(tab, linha, coluna):
    # Verifica as posições vizinhas e diagonais
    for i in range(linha - 1, linha + 2):
        for j in range(coluna - 1, coluna + 2):
            if i >= 0 and i < n and j >= 0 and j < n and tab[i][j] == 'N':
                return True
    return False



#função para imprimir o tabuleiro
def imprimetabuleiro(tab):
  for ialfa in range(n):
      print(f'    {alfa[ialfa]}', end=' ')
  print()
  for i in range(n):
    print('~' * 50)
    print(alfa[i], end=' |')
    for j in range(n):
        print(f''' {tab[i][j]:3}|''', end=' ')
    print( )

#Para salvar o arquivo
def salvar_batalha(nome, tabuleiro):
  arq = open(nome+'.txt','w')
  arq.write(nome+'\n')
  for i in range(8):
    arq.write('|')
    for l in tabuleiro[i]:
      arq.write(l + '|')
    arq.write('\n')

#funções sendo chamadas
posicionarNavio(player1,qtdNavios)
posicionarNavio(player2, qtdNavios)

#visualizar navios (para teste)
print()
print('Tabuleiro jogador 1 mostrando a frota: versão teste')
print()
imprimetabuleiro(player1)
print()
print('Tabuleiro jogador 2 mostrando a frota: versão teste')
print()
imprimetabuleiro(player2)

#programa para os tiros e para o funcionamento do jogo no geral

jogada = 0
acertos1 = 0
acertos2 = 0

while acertos1 < qtdNavios and  acertos2 < qtdNavios:
  salvar_batalha('tabuleiro jogador 1', viewPlayer1)#chamando função que APENAS SALVA o tabuleiro do jogador 1
  salvar_batalha('tabuleiro jogador 2', viewPlayer2)#chamando função que APENAS SALVA o tabuleiro do jogador 2
  print()
  print('Tabuleiro Jogador 1')
  print(f'Quantidade de acertos: {acertos1}')
  print()
  imprimetabuleiro(viewPlayer1)
  print('\n\n')
  print('Tabuleiro Jogador 2')
  print(f'Quantidade de acertos: {acertos2}')
  print()
  imprimetabuleiro(viewPlayer2)
  if jogada % 2 == 0:
    print()
    linhaPalpite = input('Jogador 1. Digite a linha da posição em que você deseja atirar do tabuleiro oponente: ').upper()
    colunaPalpite = input('Jogador 1. Digite a coluna da posição em que você deseja atirar do tabuleiro oponente: ').upper()
    num_linha = alfa.index(linhaPalpite)
    num_coluna = alfa.index(colunaPalpite)
    if player2[num_linha][num_coluna] == 'N':
      viewPlayer2[num_linha][num_coluna] = 'F'
      print()
      print('FOGO!')
      print('Você acertou, tente mais uma vez!')
      acertos1 += 1
      continue
    else:
      viewPlayer2[num_linha][num_coluna] = 'A'
      print()
      print('ÁGUA!')
      print('Você errou, agora é a vez do seu oponente!')
  else:
    print()
    linhaPalpite = input('Jogador 2. Digite a linha da posição em que você deseja atirar do tabuleiro oponente: ').upper()
    colunaPalpite = input('Jogador 2. Digite a coluna da posição em que você deseja atirar do tabuleiro oponente: ').upper()
    num_linha = alfa.index(linhaPalpite)
    num_coluna = alfa.index(colunaPalpite)
    if player1[num_linha][num_coluna] == 'N':
      viewPlayer1[num_linha][num_coluna] = 'F'
      print()
      print('FOGO!')
      print('Você acertou, tente mais uma vez!')
      acertos2 += 1
      continue
    else:
      viewPlayer1[num_linha][num_coluna] = 'A'
      print()
      print('ÁGUA!')
      print('Você errou, agora é a vez do seu oponente!')
  jogada += 1

print()
if acertos1 == qtdNavios:
  print('Parabéns jogador 1! Você afundou todos os navios do seu oponente! Suas habilidades nesse jogo são surpreendentes.')
if acertos2 == qtdNavios:
  print('Parabéns jogador 2! Você afundou todos os navios do seu oponente! Suas habilidades nesse jogo são surpreendentes.')