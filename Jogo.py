import pygame

pygame.init()

window = pygame.display.set_mode((600, 750))
pygame.display.set_caption('Rápidos e muito bravos')

jogo = True

while jogo:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo = False

    window.fill((255, 255, 255))

    pygame.display.update() 

pygame.quit()  