import random


#função para posicionar os navios na matriz de forma aleatória juntamente com a regra do projeto
def posicionarNavio(tab, qtdN):
  naviosposicionados = 0
  while naviosposicionados < qtdN:
    linha = random.randint(0, n - 1)
    coluna = random.randint(0, n - 1)
    # Verifica se a posição está vazia e não tem vizinhos ocupados
    if tab[linha][coluna] == ' ' and not temVizinhosOcupados(
        tab, linha, coluna):
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
    print()


#função para continuar jogando
def contJogo():
  continuar = input('Deseja continuar jogando?[S/N] ').upper()
  while jogada:
    if continuar == 'S':
      continue
    if continuar == 'N':
      break


#Para salvar o arquivo
def salvar_batalha(jogador, tabuleiro, acertos):
  batalha = open('batalha.txt','a')
  batalha.write('Jogador: '+ jogador + '\n')
  batalha.write('Acertos: '+ str(acertos) + '\n')
  batalha.write('     A     B     C     D     E     F     G     H   \n')
  for i in range(8):
    batalha.write('~' * 51 + '\n')
    batalha.write(alfa[i] + ' |  ')
    for l in tabuleiro[i]:
      batalha.write(l + '  |  ')
    batalha.write('\n')
  batalha.write('~' * 51 + '\n')
  batalha.write('\n' + '\n')

#Para ler o arquivo
def lerBatalha():
  batalhaLer = open('batalha.txt', 'r')
  return batalhaLer


#vetor com a localização de cada indice das linhas e colunas
alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

#ordem da matriz quadrada
n = 8

#vetor do jogador 1 (não aparece)
player1 = [None] * n
for i in range(n):
  player1[i] = [None] * n
for i in range(n):
  for j in range(n):
    player1[i][j] = ' '

#vetor do jogador 2 (não aparece)
player2 = [None] * n
for i in range(n):
  player2[i] = [None] * n
for i in range(n):
  for j in range(n):
    player2[i][j] = ' '

#matriz do jogador 1 (aparece)
viewPlayer1 = [None] * n
for i in range(n):
  viewPlayer1[i] = [None] * n

for i in range(n):
  for j in range(n):
    viewPlayer1[i][j] = ' '

#matriz do jogador 2 (aparece)
viewPlayer2 = [None] * n
for i in range(n):
  viewPlayer2[i] = [None] * n

for i in range(n):
  for j in range(n):
    viewPlayer2[i][j] = ' '

#decisão acerca do jogo
resposta = input('Deseja continuar o jogo salvo? [S/N] ').upper()

if resposta == 'N':
  #entrada da quantidade de navios nas matrizes
  qtdNavios = int(
      input('Digite quantos navios serão colocados no tabuleiro (máximo 6): '))
  #funções sendo chamadas
  posicionarNavio(player1, qtdNavios)
  posicionarNavio(player2, qtdNavios)

  #visualizar navios (para mostar em caso de teste)
  #imprimetabuleiro(player1)
  #imprimetabuleiro(player2)

  #programa para os tiros e para o funcionamento do jogo no geral

  jogada = 0
  acertos1 = 0
  acertos2 = 0

  while acertos1 < qtdNavios and acertos2 < qtdNavios:
    salvar_batalha('1', viewPlayer1, acertos1)  
    #chamando função que APENAS SALVA o tabuleiro do jogador 1
    salvar_batalha('2', viewPlayer2, acertos2)  
    #chamando função que APENAS SALVA o tabuleiro do jogador 2
    print()
    print('Tabuleiro Jogador 1')
    print(f'Acertos: {acertos1}')
    print()
    imprimetabuleiro(viewPlayer1)
    print('\n\n')
    print('Tabuleiro Jogador 2')
    print(f'Acertos: {acertos2}')
    print()
    imprimetabuleiro(viewPlayer2)
    if jogada % 2 == 0:
      print()
      linhaPalpite = input(
          'Jogador 1. Digite a linha da posição em que você deseja atirar do tabuleiro oponente: '
      ).upper()
      colunaPalpite = input(
          'Jogador 1. Digite a coluna da posição em que você deseja atirar do tabuleiro oponente: '
      ).upper()
      num_linha = alfa.index(linhaPalpite)
      num_coluna = alfa.index(colunaPalpite)
      if player2[num_linha][num_coluna] == 'N':
        viewPlayer2[num_linha][num_coluna] = 'F'
        print('FOGO!')
        print('Você acertou, tente mais uma vez!')
        acertos1 += 1
        contJogo()
        continue

      else:
        viewPlayer2[num_linha][num_coluna] = 'A'
        print('ÁGUA!')
        print('Você errou, agora é a vez do seu oponente!')
      #caso ele acerte ou erre, ADICIONE ao arquivo o tabuleiro
      #escolha acerca da continuação do jogo, enquanto ele está em andamento
      contJogo()
    else:
      print()
      linhaPalpite = input(
          'Jogador 2. Digite a linha da posição em que você deseja atirar do tabuleiro oponente: '
      ).upper()
      colunaPalpite = input(
          'Jogador 2. Digite a coluna da posição em que você deseja atirar do tabuleiro oponente: '
      ).upper()
      num_linha = alfa.index(linhaPalpite)
      num_coluna = alfa.index(colunaPalpite)
      if player1[num_linha][num_coluna] == 'N':
        viewPlayer1[num_linha][num_coluna] = 'F'
        print()
        print('FOGO!')
        print('Você acertou, tente mais uma vez!')
        acertos2 += 1
        contJogo()
        continue
      else:
        viewPlayer1[num_linha][num_coluna] = 'A'
        print()
        print('ÁGUA!')
        print('Você errou, agora é a vez do seu oponente!')
      contJogo()
    jogada += 1
    pontos1 = acertos1
    pontos2 = acertos2
    print(f'Pontos do Jogador 1: {pontos1}')
    print(f'Pontos do Jogador 2: {pontos2}')
else:
  lerBatalha()
  posicionarNavio(player1, qtdNavios)
  posicionarNavio(player2, qtdNavios)
  imprimetabuleiro(player1)
  imprimetabuleiro(player2)
  jogada = 0
  acertos1 = pontos1
  acertos2 = pontos2

  while acertos1 < qtdNavios and acertos2 < qtdNavios:
    salvar_batalha('1', viewPlayer1, acertos1)
    salvar_batalha('2', viewPlayer2, acertos2)
    print()
    print('Tabuleiro Jogador 1')
    print(f'Acertos: {acertos1}')
    print()
    imprimetabuleiro(viewPlayer1)
    print('\n\n')
    print('Tabuleiro Jogador 2')
    print(f'Acertos: {acertos2}')
    print()
    imprimetabuleiro(viewPlayer2)
    if jogada % 2 == 0:
      print()
      linhaPalpite = input(
          'Jogador 1. Digite a linha da posição em que você deseja atirar do tabuleiro oponente: '
      ).upper()
      colunaPalpite = input(
          'Jogador 1. Digite a coluna da posição em que você deseja atirar do tabuleiro oponente: '
      ).upper()
      num_linha = alfa.index(linhaPalpite)
      num_coluna = alfa.index(colunaPalpite)
      if player2[num_linha][num_coluna] == 'N':
        viewPlayer2[num_linha][num_coluna] = 'F'
        print('FOGO!')
        print('Você acertou, tente mais uma vez!')
        acertos1 += 1
        contJogo()
        continue
      else:
        viewPlayer2[num_linha][num_coluna] = 'A'
        print('ÁGUA!')
        print('Você errou, agora é a vez do seu oponente!')
      contJogo()
    else:
      print()
      linhaPalpite = input(
          'Jogador 2. Digite a linha da posição em que você deseja atirar do tabuleiro oponente: '
      ).upper()
      colunaPalpite = input(
          'Jogador 2. Digite a coluna da posição em que você deseja atirar do tabuleiro oponente: '
      ).upper()
      num_linha = alfa.index(linhaPalpite)
      num_coluna = alfa.index(colunaPalpite)
      if player1[num_linha][num_coluna] == 'N':
        viewPlayer1[num_linha][num_coluna] = 'F'
        print()
        print('FOGO!')
        print('Você acertou, tente mais uma vez!')
        acertos2 += 1
        contJogo()
        continue
      else:
        viewPlayer1[num_linha][num_coluna] = 'A'
        print()
        print('ÁGUA!')
        print('Você errou, agora é a vez do seu oponente!')
      contJogo()
    jogada += 1