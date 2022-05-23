import pygame

pygame.init()
LARGURA = 570
ALTURA = 600
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Rápidos e muito bravos')

jogo = True

rua = pygame.image.load('assets/Images/rua2.png').convert()
rua = pygame.transform.scale(rua, (570, 870))

carro = pygame.image.load('assets/Images/carro mustang.png')
carro = pygame.transform.scale(carro, (120,150))

carro2 = pygame.image.load('assets/Images/picape2_rotacionada.png')
carro2 = pygame.transform.scale(carro2, (140,160))

taxi = pygame.image.load('assets/Images/taxi_rotacionado.png')
taxi = pygame.transform.scale(taxi, (120,150))

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

jogadô = Carro(carro)
clock = pygame.time.Clock()
FPS = 60
all_sprites = pygame.sprite.Group()
all_sprites.add(jogadô)
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

    window.fill((255, 255, 255))
    window.blit(rua, (0, 0))
    window.blit(carro, (225, 450))
    window.blit(carro2, (40, 0))
    window.blit(taxi, (190, 200))
    pygame.display.update() 

pygame.quit() 