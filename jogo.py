import pygame
from pygame.locals import *
from sys import exit
from random import randint


pygame.init()

# criando tela
largura = 600
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('QUADRADIN')

# variaveis iniciais
cianos = vermelhos = verdes = 0
vivo = True
imortal = False
campeao = False
velocidade = 8
velocidade_vilao = 4
x_controle = 0
y_controle = 0
controlex_vilao = 0
controley_vilao = 0
lista_coletaveis = []
cor_tela = (0,0,0)
cor_gameover = (255,0,0)

relogio = pygame.time.Clock()
fonte = pygame.font.SysFont('arial', 25, bold=True, italic=True)
fonte2 = pygame.font.SysFont('arial', 18, bold=True, italic=False)
fonte_placar = pygame.font.SysFont('arial', 15, True, False)
fonte_vantagens = pygame.font.SysFont('arial', 22, bold=True, italic=False)
fonte_gameover = pygame.font.SysFont('franklingothicmedium', 50, bold=True, italic=False)



class Player:
    def __init__(self, cor, pos_x, pos_y):
        self.cor = cor
        self.pos_x = pos_x
        self.pos_y = pos_y

    def andar(self):
        global x_controle, y_controle
        if event.key == K_LEFT:
            x_controle = -velocidade
            y_controle = 0
        if event.key == K_RIGHT:
            x_controle = velocidade
            y_controle = 0
        if event.key == K_UP:
            x_controle = 0
            y_controle = -velocidade
        if event.key == K_DOWN:
            x_controle = 0
            y_controle = velocidade
        if player.pos_x > largura-20:
            player.pos_x = 0
        if player.pos_x < 0:
            player.pos_x = largura
        if player.pos_y > altura-20:
            player.pos_y = 0
        if player.pos_y < 0:
            player.pos_y = altura

    def colidiu(self, coletavel):
        global Coletaveis, cianos, vermelhos, verdes, velocidade, imortal, cor_tela, vivo
        if coletavel.centro_x -30 <   player.pos_x < coletavel.centro_x + 10:
            if coletavel.centro_y - 30 <  player. pos_y < coletavel.centro_y + 10:
                coletavel.centro_x = randint(0,largura-10)
                coletavel.centro_y = randint(51,altura-10)
                if coletavel == vermelho:
                    vermelhos += 1
                    velocidade += 3
                    if imortal == True:
                        imortal = False
                        cor_tela = (0, 0, 0)
                if coletavel == ciano:
                    cianos += 1
                    imortal = True
                    cor_tela = (255,255,255)
                if coletavel == verde:
                    verdes += 1
                    if velocidade > 3:
                        velocidade -= 3
                    else:
                        vivo = False
                    if imortal == True:
                        imortal = False
                        cor_tela = (0,0,0)
    def desenhar(self):
        pygame.draw.rect(tela, (0,0,255), (self.pos_x, self.pos_y, 25, 25))

class Coletaveis:
    def __init__(self, cor, centro_x, centro_y, raio):
        self.cor = cor
        self.centro_x = centro_x
        self.centro_y = centro_y
        self.raio = raio

    def desenhar_coletaveis(self):
        pygame.draw.circle(tela, self.cor, (self.centro_x, self.centro_y), self.raio)

class Vilao():
    def __init__(self, cor, pos_x, pos_y):
        self.cor = cor
        self.pos_x = pos_x
        self.pos_y = pos_y

    def desenhar_vilao(self):
        pygame.draw.rect(tela, self.cor, (self.pos_x, self.pos_y, 20, 20))

    def perseguir(self):
        global player, controlex_vilao, controley_vilao, vivo
        if self.pos_x < player.pos_x:
            controlex_vilao = velocidade_vilao

        if self.pos_x > player.pos_x:
            controlex_vilao = -velocidade_vilao

        if self.pos_y < player.pos_y:
            controley_vilao = velocidade_vilao
        if self.pos_y > player.pos_y:
            controley_vilao = -velocidade_vilao

        if player.pos_x - 20 < self.pos_x < player.pos_x + 25 and not imortal :
            if player.pos_y - 20 < self.pos_y < player.pos_y + 25:
                vivo = False

def reiniciar_jogo():
    global cianos, vermelhos, verdes, vivo, imoral, velocidade, velocidade_vilao, imortal, x_controle, y_controle
    global controlex_vilao, controley_vilao, lista_coletaveis, player, inimigo
    cianos = vermelhos = verdes = 0
    vivo = True
    imortal = False
    velocidade = 8
    velocidade_vilao = 4
    x_controle = 0
    y_controle = 0
    controlex_vilao = 0
    controley_vilao = 0
    player.pos_x = largura//2
    player.pos_y = altura//2
    inimigo.pos_x = largura-20
    inimigo.pos_y = altura-20
menu = True
while menu:
    tela.fill((0, 0, 0))

    mensagem = ('Seja Bem-Vindo(a) ao Nosso Jogo!')   # Mensagem de Bem-Vindo
    texto_formatado4 = fonte.render(mensagem, True, (255, 255, 0))
    tela.blit(texto_formatado4, (90, altura / 7))
    inicio = ('Pressione a BARRA DE ESPAÇO para iniciar')    # Iniciar Jogo
    texto_formatado3 = fonte.render(inicio, True, (255, 255, 255))
    tela.blit(texto_formatado3, (35, altura / 2.2))
    poderes_coletaveis = ('||||||  Efeitos  ||||||')  # Mostra as vantagens dos coletáveis
    texto_formatado8 = fonte_vantagens.render(poderes_coletaveis, True, (100, 100, 220))
    tela.blit(texto_formatado8, (15, altura / 1.3))
    pontuacao1 = ('Ciano: Invencível')
    texto_formatado5 = fonte2.render(pontuacao1, True, (0, 255, 255))
    tela.blit(texto_formatado5, (15, altura / 1.22))
    pontuacao2 = ('Verde: Perde Velocidade')
    texto_formatado6 = fonte2.render(pontuacao2, True, (0, 255, 0))
    tela.blit(texto_formatado6, (15, altura / 1.17))
    pontuacao3 = ('Vermelho: Ganha Velocidade')
    texto_formatado7 = fonte2.render(pontuacao3, True, (255, 0, 0))
    tela.blit(texto_formatado7, (15, altura / 1.13))


    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                menu = False

    pygame.display.update()

player = Player((0,0,255), largura//2, altura//2 )
inimigo = Vilao((255, 255, 0), largura-20, altura-20 )
vermelho = Coletaveis((255, 0, 0), randint(0, largura - 30), randint(0,altura - 30), 5)
ciano = Coletaveis((0, 255, 255), randint(0, largura - 30), randint(0,altura - 30), 5)
verde = Coletaveis((0, 255, 0), randint(0, largura - 30), randint(0,altura - 30), 5)
lista_coletaveis.append(ciano)
lista_coletaveis.append(vermelho)
lista_coletaveis.append(verde)

vivo = True
while True:
    while vivo:
        tela.fill((cor_tela))
        mensagem = (f'Cianos: {cianos}  |  Verde:{verdes}  |  Vermelhos:{vermelhos}')
        texto_formatado = fonte_placar.render(mensagem, True, (255, 255, 255), True)
        relogio.tick(30)
        player.desenhar()
        vermelho.desenhar_coletaveis()
        ciano.desenhar_coletaveis()
        verde.desenhar_coletaveis()
        inimigo.desenhar_vilao()

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                player.andar()
        for coletavel in lista_coletaveis:
            player.colidiu(coletavel)

        player.pos_x += x_controle
        player.pos_y += y_controle
        inimigo.pos_x += controlex_vilao
        inimigo.pos_y += controley_vilao

        if player.pos_x > largura:
            player.pos_x = 0
        if player.pos_y > altura:
            player.pos_y = 0
        if player.pos_x < 0:
            player.pos_x = 600
        if player.pos_y < 0:
            player.pos_y = 600
        inimigo.perseguir()
        tela.blit(fonte_placar.render(f'Cianos: ' + str(cianos) + ' |', True, 'aqua'), (20, 30))
        tela.blit(fonte_placar.render(f'Verdes: ' + str(verdes) + ' |', True, 'green'), (100, 30))
        tela.blit(fonte_placar.render(f'Vermelhos: ' + str(vermelhos) + ' |', True, 'red'), (180, 30))
        tela.blit(fonte_placar.render(f'Colete {10 - verdes} objetos verdes', True, 'green'), (400, 30))
        pygame.display.update()
        if verdes == 10:
            vivo = False
            campeao = True
            gameover = ('Você ganhou!!!')
            cor_gameover = (0,0,255)
    if not vivo:
        tela.fill((0, 0, 0))
        if not campeao:
            gameover = ('Game Over :(')
        reset = ('Pressione "BARRA DE ESPAÇO" para reiniciar')
        sair = ('Pressione "ESC" para sair')
        texto_formatado1 = fonte_gameover.render(gameover, True, cor_gameover, True)
        texto_formatado2 = fonte.render(reset, True, (255, 255, 255), True)
        texto_formatado3 = fonte2.render(sair, True, (0, 255, 0), True)


        tela.blit(texto_formatado1, (130, altura // 6))
        tela.blit(texto_formatado2, (20, altura // 2))
        tela.blit(texto_formatado3, (170, altura // 1.6))

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    reiniciar_jogo()
                    vivo = True
                if event.key == K_ESCAPE:
                    exit()
        pygame.display.update()
