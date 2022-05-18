import pygame

pygame.init()

window = pygame.display.set_mode((570, 600))
pygame.display.set_caption('Rápidos e muito bravos')

jogo = True

image = pygame.image.load('assets/Images/rua2.png').convert()
image = pygame.transform.scale(image, (570, 870))

while jogo:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo = False

    window.fill((255, 255, 255))
    window.blit(image, (0, 0))
    pygame.display.update() 

pygame.quit()  