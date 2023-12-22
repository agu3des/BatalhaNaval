import random
import os

class BatalhaException(Exception):
    """Classe de exceção lançada quando uma violação no acesso aos elementos
    do jogo, indicado pelo usuário, é identificada.
    """
    def __init__(self,msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
        embutir na exceção.
        """
        super().__init__(msg)


class Batalha():
    def __init__(self):
        """
        No construtor da classe jogo, criamos os atributos jogadores e removidos e instanciamos a lista e a pilha nos mesmos.
        """
        #vetor com a localização de cada indice das linhas e colunas
        self.alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        #ordem da matriz quadrada
        self.n = 8

    def temVizinhosOcupados(self,tab, linha, coluna):
    # Verifica as posições vizinhas e diagonais
        for i in range(linha - 1, linha + 2):
            for j in range(coluna - 1, coluna + 2):
                if i >= 0 and i < self.n and j >= 0 and j < self.n and tab[i][j] == 'N':
                    return True
        return False


    #função para posicionar os navios na matriz de forma aleatória juntamente com a regra do projeto
    def posicionarNavio(self,tab, qtdN):
        naviosposicionados = 0
        while naviosposicionados < qtdN:
            linha = random.randint(0, self.n - 1)
            coluna = random.randint(0, self.n - 1)
            # Verifica se a posição está vazia e não tem vizinhos ocupados
            if tab[linha][coluna] == ' ' and not self.temVizinhosOcupados(tab, linha, coluna):
                tab[linha][coluna] = 'N'
                naviosposicionados += 1
        return tab


    #função para imprimir o tabuleiro
    def imprimetabuleiro(self,tab):
        for self.ialfa in range(self.n):
            print(f'    {self.alfa[self.ialfa]}', end=' ')
        print()
        for i in range(self.n):
            print('~' * 50)
            print(self.alfa[i], end=' |')
            for j in range(self.n):
                    print(f''' {tab[i][j]:3}|''', end=' ')
            print()


    #função para continuar jogando
    def contJogo(self):
        continuar = input('Deseja continuar jogando?[S/N] ').upper()
        while True:
            if continuar == 'S':
                return continuar
            elif continuar == 'N':
                break
            else:
                raise BatalhaException(f'O caractere: {continuar} não é válido!')
            

    #Para salvar o arquivo
    def salvarBatalha(self, jogador, tabuleiro, acertos):
        with open('batalha.txt', 'a') as batalha:
            lista = []
            for i, linha in enumerate(tabuleiro):
                for j, item in enumerate(linha):
                    if item == 'A' or item == 'F': 
                        posicao = f'Linha: {i}, Coluna: {j}'
                        lista.append(f'Jogador: {jogador}, Acertos: {acertos}, Posicao: {posicao}, Item: {item}')
            batalha.write(str(lista) + '\n')


    #Para ler o arquivo
    def lerBatalha(self):
        puxarArquivo = input('Deseja carregar os dados do jogo através de um arquivo? (S)im/(N)ão: ').upper()
        if puxarArquivo != 'S' and puxarArquivo != 'N':
            raise BatalhaException(f'A resposta deve ser S ou N.')
        
        if puxarArquivo == 'S':
            if os.path.isfile('batalha.txt'):
                with open('batalha.txt', 'r') as batalha:
                    for linha in batalha:
                        # Separar os valores pela vírgula
                        valores = linha.strip().split(',')
                        print(valores)       
            else:
                raise BatalhaException(f'Arquivo não encontrado.')
            return True
        else:
            return False