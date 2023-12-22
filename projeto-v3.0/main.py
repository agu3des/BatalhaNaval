from batalha import *
from player import *


Player = Player()
Batalha = Batalha()


#mostra os tabuleiros respectivos a cada jogador
viewPlayer1 = Player.viewPlayer()
viewPlayer2 = Player.viewPlayer()

#decisão acerca do jogo
lerBatalha = Batalha.lerBatalha()

#input dos nomes dos jogadores
nomePlayer1 = input('Digite o nome do jogador 1: ')
nomePlayer2 = input('Digite o nome do jogador 2: ')

#criação dos vetores
player1 = Player.vetorPlayer()
player2 = Player.vetorPlayer()

jogada = 0
acertosPlayer1 = 0
acertosPlayer2 = 0

#entrada da quantidade de navios nas matrizes
qtdNavios = int(
    input('Digite quantos navios serão colocados no tabuleiro (máximo 6): '))

if lerBatalha == False:
  #funções sendo chamadas
  Batalha.posicionarNavio(player1, qtdNavios)
  Batalha.posicionarNavio(player2, qtdNavios)


  while acertosPlayer1 < qtdNavios and acertosPlayer2 < qtdNavios:
    Batalha.salvarBatalha('1', viewPlayer1, acertosPlayer1)  
    #chamando função que APENAS SALVA o tabuleiro do jogador 1
    Batalha.salvarBatalha('2', viewPlayer2, acertosPlayer2)  
    #chamando função que APENAS SALVA o tabuleiro do jogador 2
    print()
    print(f'Tabuleiro Jogador {nomePlayer1}')
    print(f'Acertos: {acertosPlayer1}')
    print()
    Batalha.imprimetabuleiro(viewPlayer1)
    print('\n\n')
    print(f'Tabuleiro Jogador {nomePlayer2}')
    print(f'Acertos: {acertosPlayer2}')
    print()
    Batalha.imprimetabuleiro(viewPlayer2)
    if jogada % 2 == 0:
      print()
      linhaPalpite = input(
          'Jogador, digite a linha da posição em que você deseja atirar do tabuleiro oponente: '
      ).upper()
      colunaPalpite = input(
          'Jogador, digite a coluna da posição em que você deseja atirar do tabuleiro oponente: '
      ).upper()
      num_linha = Batalha.alfa.index(linhaPalpite)
      num_coluna = Batalha.alfa.index(colunaPalpite)
      if player2[num_linha][num_coluna] == 'N':
        viewPlayer2[num_linha][num_coluna] = 'F'
        print('FOGO!')
        print('Você acertou, tente mais uma vez!')
        acertosPlayer1 += 1
        Batalha.contJogo()
        continue

      else:
        viewPlayer2[num_linha][num_coluna] = 'A'
        print('ÁGUA!')
        print('Você errou, agora é a vez do seu oponente!')
      #caso ele acerte ou erre, ADICIONE ao arquivo o tabuleiro
      #escolha acerca da continuação do jogo, enquanto ele está em andamento
      Batalha.contJogo()
    else:
      print()
      linhaPalpite = input(
          'Jogador, digite a linha da posição em que você deseja atirar do tabuleiro oponente: '
      ).upper()
      colunaPalpite = input(
          'Jogador, digite a coluna da posição em que você deseja atirar do tabuleiro oponente: '
      ).upper()
      num_linha = Batalha.alfa.index(linhaPalpite)
      num_coluna = Batalha.alfa.index(colunaPalpite)
      if player1[num_linha][num_coluna] == 'N':
        viewPlayer1[num_linha][num_coluna] = 'F'
        print()
        print('FOGO!')
        print('Você acertou, tente mais uma vez!')
        acertosPlayer2 += 1
        Batalha.contJogo()
        continue
      else:
        viewPlayer1[num_linha][num_coluna] = 'A'
        print()
        print('ÁGUA!')
        print('Você errou, agora é a vez do seu oponente!')
      Batalha.contJogo()
    jogada += 1
    pontos1 = acertosPlayer1
    pontos2 = acertosPlayer2
    print(f'Pontos do Jogador 1: {pontos1}')
    print(f'Pontos do Jogador 2: {pontos2}')
else:
  Batalha.posicionarNavio(player1, qtdNavios)
  Batalha.posicionarNavio(player2, qtdNavios)
  Batalha.imprimetabuleiro(player1)
  Batalha.imprimetabuleiro(player2)
  jogada = 0
  acertos1 = valores[-4]
  acertos2 = acertosPlayer2

  while acertos1 < qtdNavios and acertos2 < qtdNavios:
    Batalha.salvarBatalha('1', viewPlayer1, acertos1)
    Batalha.salvarBatalha('2', viewPlayer2, acertos2)
    print()
    print('Tabuleiro Jogador 1')
    print(f'Acertos: {acertos1}')
    print()
    Batalha.imprimetabuleiro(viewPlayer1)
    print('\n\n')
    print('Tabuleiro Jogador 2')
    print(f'Acertos: {acertos2}')
    print()
    Batalha.imprimetabuleiro(viewPlayer2)
    if jogada % 2 == 0:
      print()
      linhaPalpite = input(
          'Jogador 1. Digite a linha da posição em que você deseja atirar do tabuleiro oponente: '
      ).upper()
      colunaPalpite = input(
          'Jogador 1. Digite a coluna da posição em que você deseja atirar do tabuleiro oponente: '
      ).upper()
      num_linha = Batalha.alfa.index(linhaPalpite)
      num_coluna = Batalha.alfa.index(colunaPalpite)
      if player2[num_linha][num_coluna] == 'N':
        viewPlayer2[num_linha][num_coluna] = 'F'
        print('FOGO!')
        print('Você acertou, tente mais uma vez!')
        acertos1 += 1
        Batalha.contJogo()
        continue
      else:
        viewPlayer2[num_linha][num_coluna] = 'A'
        print('ÁGUA!')
        print('Você errou, agora é a vez do seu oponente!')
      Batalha.contJogo()
    else:
      print()
      linhaPalpite = input(
          'Jogador 2. Digite a linha da posição em que você deseja atirar do tabuleiro oponente: '
      ).upper()
      colunaPalpite = input(
          'Jogador 2. Digite a coluna da posição em que você deseja atirar do tabuleiro oponente: '
      ).upper()
      num_linha = Batalha.alfa.index(linhaPalpite)
      num_coluna = Batalha.alfa.index(colunaPalpite)
      if player1[num_linha][num_coluna] == 'N':
        viewPlayer1[num_linha][num_coluna] = 'F'
        print()
        print('FOGO!')
        print('Você acertou, tente mais uma vez!')
        acertos2 += 1
        Batalha.contJogo()
        continue
      else:
        viewPlayer1[num_linha][num_coluna] = 'A'
        print()
        print('ÁGUA!')
        print('Você errou, agora é a vez do seu oponente!')
      Batalha.contJogo()
    jogada += 1
