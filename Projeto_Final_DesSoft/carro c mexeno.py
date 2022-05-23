import pygame
import random
pygame.init()
LARGURA = 570
ALTURA = 600
LARGURA_CARRO = 120
ALTURA_CARRO = 150
LARGURA_PICAPE = 140
ALTURA_PICAPE = 160
LARGURA_TAXI = 120
ALTURA_TAXI = 160
ALTURA_VERDE = 160
LARGURA_VERDE = 120

window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Rápidos e muito bravos')

jogo = True

rua_img = pygame.image.load('assets/Images/rua2.png').convert()
rua_img = pygame.transform.scale(rua_img, (570, 870))

carro_img = pygame.image.load('assets/Images/carro mustang.png')
carro_img = pygame.transform.scale(carro_img, (LARGURA_CARRO,ALTURA_CARRO))

picape_img = pygame.image.load('assets/Images/picape2_rotacionada.png')
picape_img = pygame.transform.scale(picape_img, (LARGURA_PICAPE,ALTURA_PICAPE))

taxi_img = pygame.image.load('assets/Images/taxi_rotacionado.png')
taxi_img = pygame.transform.scale(taxi_img, (LARGURA_TAXI,ALTURA_TAXI))

verde_img = pygame.image.load('assets/Images/carro verde2_rotacionada.png')
verde_img = pygame.transform.scale(verde_img, (LARGURA_VERDE,ALTURA_VERDE))

class Carro(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = LARGURA / 2
        self.rect.bottom = ALTURA - 10
        self.speedx = 0

    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0
class Picape(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = (40)
        self.rect.y = (-100)
        self.speedx = (0)
        self.speedy = (5)

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > ALTURA:
            self.rect.x = (40)
            self.rect.y = (-100)
            self.speedx = (0)
            self.speedy = (5)
class Taxi(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = (190)
        self.rect.y = (-100)
        self.speedx = (0)
        self.speedy = (5)

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > ALTURA:
            self.rect.x = (190)
            self.rect.y = (-100)
            self.speedx = (0)
            self.speedy = (5)
class Carro_verde(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = (400)
        self.rect.y = (-150)
        self.speedx = (0)
        self.speedy = (7)

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > ALTURA:
            self.rect.x = (400)
            self.rect.y = (-150)
            self.speedx = (0)
            self.speedy = (7)
jogadô = Carro(carro_img)
clock = pygame.time.Clock()
FPS = 60
all_sprites = pygame.sprite.Group()
all_sprites.add(jogadô)
for i in range(1):
    picape = Picape(picape_img)
    all_sprites.add(picape)
    taxi = Taxi(taxi_img)
    all_sprites.add(taxi)
    carro_verde = Carro_verde(verde_img)
    all_sprites.add(carro_verde)
while jogo:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                jogadô.speedx -= 4
            if event.key == pygame.K_RIGHT:
                jogadô.speedx += 4
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                jogadô.speedx += 4
            if event.key == pygame.K_RIGHT:
                jogadô.speedx -= 4
                
        if event.type == pygame.QUIT:
            jogo = False
    all_sprites.update()
    window.fill((255, 255, 255))
    window.blit(rua_img, (0, 0))
    all_sprites.draw(window)
    pygame.display.update() 

pygame.quit() 