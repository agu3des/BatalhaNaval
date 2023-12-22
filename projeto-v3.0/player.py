class PlayerException(Exception):
    """Classe de exceção lançada quando uma violação no acesso aos elementos
    do player, indicado pelo usuário, é identificada.
    """
    def __init__(self,msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
        embutir na exceção.
        """
        super().__init__(msg)


class Player():
    def __init__(self):
        """
        No construtor da classe jogo, criamos os atributos jogadores e removidos e instanciamos a lista e a pilha nos mesmos.
        """
        #ordem da matriz quadrada
        self.n = 8


    #vetor do jogador
    def vetorPlayer(self):
        player = [[' ' for _ in range(self.n)] for _ in range(self.n)]
        return player


    #matriz de visualização do player
    def viewPlayer(self):
        viewPlayer = [[' ' for _ in range(self.n)] for _ in range(self.n)]
        return viewPlayer