import pygame
import random

pygame.init()

LARGURA = 600
ALTURA = 600
LARGURA_CARRO = 70
ALTURA_CARRO = 120
LARGURA_PICAPE = 70
ALTURA_PICAPE = 120
LARGURA_TAXI = 70
ALTURA_TAXI = 120
LARGURA_VERDE = 70
ALTURA_VERDE = 120 
GAME = False
LARGURA_ROSA = 70
ALTURA_ROSA = 120
LARGURA_VAN = 80
ALTURA_VAN = 130 
LARGURA_CAMINHÃO = 100
ALTURA_CAMINHÃO = 300
LARGURA_POLÍCIA = 70
ALTURA_POLÍCIA = 120 

lista_score = []

high_score = 0

window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Rápidos e muito bravos')

start = True
imagem = pygame.image.load('assets/Images/tela_inicio.png').convert()
imagem = pygame.transform.scale(imagem, (LARGURA, ALTURA))

while start:
        window.blit(imagem, (0, 0))
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                jogo = False
                GAME = True
                start = False

            if event.type == pygame.KEYUP:
                GAME = True
                start = False
                
        pygame.display.update()
     

while GAME:
    #carrega som
    pygame.mixer.music.load('assets/sounds/transito.mp3')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.load('assets/sounds/drift.mp3')
    pygame.mixer.music.set_volume(0.6)

    batida_sound = pygame.mixer.Sound('assets/sounds/batida.mp3')

    jogo = True

    carro_img = pygame.image.load('assets/Images/carro mustang.png')
    carro_img = pygame.transform.scale(carro_img, (LARGURA_CARRO,ALTURA_CARRO))

    van_img = pygame.image.load('assets/Images/van.png')
    van_img = pygame.transform.scale(van_img, (LARGURA_VAN,ALTURA_VAN))

    carro_rosa_img = pygame.image.load('assets/Images/carro_rosa.png')
    carro_rosa_img = pygame.transform.scale(carro_rosa_img, (LARGURA_ROSA,ALTURA_ROSA))

    polícia_img = pygame.image.load('assets/Images/polícia.png')
    polícia_img = pygame.transform.scale(polícia_img, (LARGURA_POLÍCIA,ALTURA_POLÍCIA))

    caminhão_img = pygame.image.load('assets/Images/caminhão.png')
    caminhão_img = pygame.transform.scale(caminhão_img, (LARGURA_CAMINHÃO,ALTURA_CAMINHÃO))

    picape_img = pygame.image.load('assets/Images/picape2_rotacionada.png')
    picape_img = pygame.transform.scale(picape_img, (LARGURA_PICAPE,ALTURA_PICAPE))

    taxi_img = pygame.image.load('assets/Images/taxi_rotacionado.png')
    taxi_img = pygame.transform.scale(taxi_img, (LARGURA_TAXI,ALTURA_TAXI))

    verde_img = pygame.image.load('assets/Images/carro verde2_rotacionada.png')
    verde_img = pygame.transform.scale(verde_img, (LARGURA_VERDE,ALTURA_VERDE))

    rua_img = pygame.image.load('assets/Images/rua2.png').convert()
    rua_img = pygame.transform.scale(rua_img, (600, 870))

    rua2_img = pygame.image.load('assets/Images/frame2.png').convert()
    rua2_img = pygame.transform.scale(rua2_img, (600, 870))

    rua3_img = pygame.image.load('assets/Images/frame3.png').convert()
    rua3_img = pygame.transform.scale(rua3_img, (600, 870))

    rua4_img = pygame.image.load('assets/Images/frame4.png').convert()
    rua4_img = pygame.transform.scale(rua4_img, (600, 870))

    rua5_img = pygame.image.load('assets/Images/frame5.png').convert()
    rua5_img = pygame.transform.scale(rua5_img, (600, 870))

    rua6_img = pygame.image.load('assets/Images/frame6.png').convert()
    rua6_img = pygame.transform.scale(rua6_img, (600, 870))

    rua7_img = pygame.image.load('assets/Images/frame7.png').convert()
    rua7_img = pygame.transform.scale(rua7_img, (600, 870))

    rua8_img = pygame.image.load('assets/Images/frame8.png').convert()
    rua8_img = pygame.transform.scale(rua8_img, (600, 870))

    rua9_img = pygame.image.load('assets/Images/frame9.png').convert()
    rua9_img = pygame.transform.scale(rua9_img, (600, 870))

    rua10_img = pygame.image.load('assets/Images/frame10.png').convert()
    rua10_img = pygame.transform.scale(rua10_img, (600, 870))

    Pontuação = pygame.font.Font('assets/Fonte/PressStart2P.ttf', 28)

    lista_ruas = [rua_img,rua2_img,rua3_img,rua4_img,rua5_img,rua6_img,rua7_img,rua8_img,rua9_img,rua10_img]

    i = len(lista_ruas)-1

    score = 0

    class Carro(pygame.sprite.Sprite):
        def __init__(self, img):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.centerx = LARGURA / 2
            self.rect.bottom = ALTURA - 10
            self.speedx = 0
            self.speedy = 0

        def update(self):
            # Atualização da posição da nave
            self.rect.x += self.speedx
            self.rect.y += self.speedy

            # Mantem dentro da tela
            if self.rect.right > LARGURA:
                self.rect.right = LARGURA
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.y < 0:
                self.rect.y = 0
            if self.rect.y>ALTURA -ALTURA_CARRO:
                self.rect.y = ALTURA - ALTURA_CARRO
    class Picape(pygame.sprite.Sprite):
        def __init__(self, img):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = (40)
            self.rect.y = (-200)
            self.speedx = (0)
            self.speedy = (5)

        def update(self):
            # Atualizando a posição do meteoro
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            # Se o meteoro passar do final da tela, volta para cima e sorteia
            # novas posições e velocidades
            if self.rect.top > ALTURA:
                self.rect.x = (random.randint((0),(LARGURA-LARGURA_PICAPE)))
                self.rect.y = (-220)
                self.speedx = (0)
                self.speedy = (5)
                
    class Taxi(pygame.sprite.Sprite):
        def __init__(self, img):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = (190)
            self.rect.y = (-130)
            self.speedx = (0)
            self.speedy = (5)
        def update(self):
            # Atualizando a posição do meteoro
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            # Se o meteoro passar do final da tela, volta para cima e sorteia
            # novas posições e velocidades
            if self.rect.top > ALTURA:
                self.rect.x = (random.randint((0),(LARGURA-LARGURA_TAXI)))
                self.rect.y = (-130)
                self.speedx = (0)
                self.speedy = (5)

    class Carro_verde(pygame.sprite.Sprite):
        def __init__(self, img):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = (400)
            self.rect.y = (-500)
            self.speedx = (0)
            self.speedy = (5)

        def update(self):
            # Atualizando a posição do meteoro
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            # Se o meteoro passar do final da tela, volta para cima e sorteia
            # novas posições e velocidades
            if self.rect.top > ALTURA:
                self.rect.x = (random.randint((0),(LARGURA-LARGURA_VERDE)))
                self.rect.y = (-700)
                self.speedx = (0)
                self.speedy = (5)
    class Carro_rosa(pygame.sprite.Sprite):
        def __init__(self, img):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = (400)
            self.rect.y = (-300)
            self.speedx = (0)
            self.speedy = (5)

        def update(self):
            # Atualizando a posição do meteoro
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            # Se o meteoro passar do final da tela, volta para cima e sorteia
            # novas posições e velocidades
            if self.rect.top > ALTURA:
                self.rect.x = (random.randint((0),(LARGURA-LARGURA_ROSA)))
                self.rect.y = (-800)
                self.speedx = (0)
                self.speedy = (5)
    class Van(pygame.sprite.Sprite):
        def __init__(self, img):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = (400)
            self.rect.y = (-600)
            self.speedx = (0)
            self.speedy = (5)

        def update(self):
            # Atualizando a posição do meteoro
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            # Se o meteoro passar do final da tela, volta para cima e sorteia
            # novas posições e velocidades
            if self.rect.top > ALTURA:
                self.rect.x = (random.randint((0),(LARGURA-LARGURA_VAN)))
                self.rect.y = (-600)
                self.speedx = (0)
                self.speedy = (5)
    class Polícia(pygame.sprite.Sprite):
        def __init__(self, img):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = (400)
            self.rect.y = (-1000)
            self.speedx = (0)
            self.speedy = (5)

        def update(self):
            # Atualizando a posição do meteoro
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            # Se o meteoro passar do final da tela, volta para cima e sorteia
            # novas posições e velocidades
            if self.rect.top > ALTURA:
                self.rect.x = (random.randint((0),(LARGURA-LARGURA_POLÍCIA)))
                self.rect.y = (-1000)
                self.speedx = (0)
                self.speedy = (5)
    class Caminhão(pygame.sprite.Sprite):
        def __init__(self, img):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = (400)
            self.rect.y = (-1000)
            self.speedx = (0)
            self.speedy = (5)

        def update(self):
            # Atualizando a posição do meteoro
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            # Se o meteoro passar do final da tela, volta para cima e sorteia
            # novas posições e velocidades
            if self.rect.top > ALTURA:
                self.rect.x = (random.randint((0),(LARGURA-LARGURA_CAMINHÃO)))
                self.rect.y = (-800)
                self.speedx = (0)
                self.speedy = (5)
    jogadô = Carro(carro_img)
    clock = pygame.time.Clock()
    FPS = 60
    all_sprites = pygame.sprite.Group()
    carros = pygame.sprite.Group()
    for i in range(1):
        picape = Picape(picape_img)
        taxi = Taxi(taxi_img)
        carro_verde = Carro_verde(verde_img)
        carro_rosa = Carro_rosa(carro_rosa_img)
        van = Van(van_img)
        polícia = Polícia(polícia_img)
        caminhão = Caminhão(caminhão_img)
        all_sprites.add(jogadô,carro_verde,taxi,picape,caminhão,polícia,carro_rosa,van)
        carros.add(taxi,picape,carro_verde,caminhão,carro_rosa,polícia,van)

    pygame.mixer.music.play(loops=-1)
    while jogo:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    jogadô.speedx -= 7
                if event.key == pygame.K_RIGHT:
                    jogadô.speedx += 7
                if event.key == pygame.K_UP:
                    jogadô.speedy -= 4
                if event.key == pygame.K_DOWN:
                    jogadô.speedy += 4
                if event.key == pygame.K_a:
                    jogadô.speedx -= 7
                if event.key == pygame.K_d:
                    jogadô.speedx += 7
                if event.key == pygame.K_w:
                    jogadô.speedy -= 4
                if event.key == pygame.K_s:
                    jogadô.speedy += 4
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    jogadô.speedx += 7
                if event.key == pygame.K_RIGHT:
                    jogadô.speedx -= 7
                if event.key == pygame.K_UP:
                    jogadô.speedy += 4
                if event.key == pygame.K_DOWN:
                    jogadô.speedy -= 4
                if event.key == pygame.K_a:
                    jogadô.speedx += 7
                if event.key == pygame.K_d:
                    jogadô.speedx -= 7
                if event.key == pygame.K_w:
                    jogadô.speedy += 4
                if event.key == pygame.K_s:
                    jogadô.speedy -= 4
                    
            if event.type == pygame.QUIT:
                jogo = False

        all_sprites.update()
        window.fill((255, 255, 255))
        window.blit(lista_ruas[i], (0, 0))
        all_sprites.draw(window)

        if score < 1000:
            text_surface = Pontuação.render("{:08d}".format(score), True, (255, 255, 0))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (LARGURA / 2,  10)
            window.blit(text_surface, text_rect)

        elif score >= 1000 and score < 2000:
            text_surface = Pontuação.render("{:08d}".format(score), True, (30, 144, 255))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (LARGURA / 2,  10)
            window.blit(text_surface, text_rect)
        
        elif score >= 2000 and score < 3000:
            text_surface = Pontuação.render("{:08d}".format(score), True, (0, 250, 154))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (LARGURA / 2,  10)
            window.blit(text_surface, text_rect)

        elif score >= 3000 and score < 4000:
            text_surface = Pontuação.render("{:08d}".format(score), True, (128, 0,128))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (LARGURA / 2,  10)
            window.blit(text_surface, text_rect)
        
        elif score >= 4000 and score < 5000:
            text_surface = Pontuação.render("{:08d}".format(score), True, (255,20,147))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (LARGURA / 2,  10)
            window.blit(text_surface, text_rect)
        
        elif score >= 5000:
            text_surface = Pontuação.render("{:08d}".format(score), True, (255, 0, 0))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (LARGURA / 2,  10)
            window.blit(text_surface, text_rect)

        score += 1
        pygame.display.update() 
        i -= 1
        if i < 0:
            i = len(lista_ruas)-1
        hits = pygame.sprite.spritecollide(jogadô, carros, True)
        
        if len(hits)>0:
            tela_final = pygame.image.load('assets/Images/tela_final.png').convert()
            batida_sound.play()
            pygame.mixer.music.set_volume(0.1)
            end = True
            GAME = False
            jogo = False
            lista_score.append(score)
            for pontos in lista_score:
                if pontos >= high_score:
                    high_score = pontos

            while end:
                window.blit(tela_final, (0, 0))
                text_surface = Pontuação.render("{:08d}".format(high_score), True, 	(255,255,255))
                text_rect = text_surface.get_rect()
                text_rect.midtop = (450,480)
                window.blit(text_surface, text_rect)
                text_surface = Pontuação.render("high_score:", True, 	(255,255,255))
                text_rect = text_surface.get_rect()
                text_rect.midtop = (190,480)
                window.blit(text_surface, text_rect)
                for event in pygame.event.get():
                # Verifica se foi fechado.
                    if event.type == pygame.QUIT:
                        end = False

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_SPACE:
                            GAME = True
                            end = False
                
                pygame.display.update()
            
        if event.type == pygame.QUIT:
            jogo = False
            GAME = False
pygame.quit() 