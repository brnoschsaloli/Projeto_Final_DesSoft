import pygame

pygame.init()

window = pygame.display.set_mode((570, 600))
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

verde = pygame.image.load('assets/Images/carro verde2_rotacionada.png')
verde = pygame.transform.scale(verde, (120,150))

while jogo:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo = False

    window.fill((255, 255, 255))
    window.blit(rua, (0, 0))
    window.blit(carro, (225, 450))
    window.blit(carro2, (40, 0))
    window.blit(taxi, (190, 200))
    window.blit(verde, (400,50))
    pygame.display.update() 

pygame.quit()  