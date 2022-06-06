#importa bibliotecas necessárias
import pygame
import random

#inicia módulos importados do pygame
pygame.init()

#Define parâmetros
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

#cria janela do jogo
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Rápidos e muito bravos')

start = True
#cria tela inicial
imagem = pygame.image.load('assets/Images/tela_inicio.png').convert()
imagem = pygame.transform.scale(imagem, (LARGURA, ALTURA))

#coloca música de intro
intro = pygame.mixer.Sound('assets/sounds/musica_inicio.mp3')
intro.set_volume(0.5)
intro.play()

#Definindo fontes
Pontuação = pygame.font.Font('assets/Fonte/PressStart2P.ttf', 28)
aviso = pygame.font.Font('assets/Fonte/PressStart2P.ttf', 18)
instruções = pygame.font.Font('assets/Fonte/PressStart2P.ttf', 20)
instruções2 = pygame.font.Font('assets/Fonte/PressStart2P.ttf', 15)

#programação da tela de início
while start:
        window.blit(imagem, (0, 0))
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                jogo = False
                GAME = True
                start = False
            #inicia o jogo
            if event.type == pygame.KEYUP:
                controles = True
                start = False
                
        #atualiza a tela
        pygame.display.update()

while controles:
    #Desenha as informações na tela
    window.fill((0,0,0))
    text_surface = Pontuação.render('Controles', True, 	(255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (300,5)
    window.blit(text_surface, text_rect)
    text_surface = instruções.render("Movimentação", True, 	(255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (300,60)
    window.blit(text_surface, text_rect)
    text_surface = instruções.render("Cima", True, 	(255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (300,150)
    window.blit(text_surface, text_rect)
    text_surface = instruções2.render("W ou ↑", True, 	(255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (305,190)
    window.blit(text_surface, text_rect)
    text_surface = instruções.render("Direita", True, 	(255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (500,250)
    window.blit(text_surface, text_rect)
    text_surface = instruções2.render("D ou →", True, 	(255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (500,290)
    window.blit(text_surface, text_rect)
    text_surface = instruções.render("Esquerda", True, 	(255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (100,250)
    window.blit(text_surface, text_rect)
    text_surface = instruções2.render("E ou ←", True, 	(255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (100,290)
    window.blit(text_surface, text_rect)
    text_surface = instruções.render("Trás", True, 	(255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (300,350)
    window.blit(text_surface, text_rect)
    text_surface = instruções2.render("S ou ↓", True, 	(255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (305,390)
    window.blit(text_surface, text_rect)
    text_surface = instruções2.render("clique qualquer tecla para iniciar", True, 	(0,255,0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (305,500)
    window.blit(text_surface, text_rect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo = False
            GAME = True
            controles = False
        if event.type == pygame.KEYUP:
                GAME = True
                controles = False
                #para a música de intro
                intro.stop()
    pygame.display.update() 
#loop principal
while GAME:
    #definindo váriaveis necessárias 
    score = 0
    score_750 = 0
    score_100 = 0
    mova = True
    tempo = 0
    tempo_ruas = 0
    c = 0
    v = 4

    #carrega sons
    pygame.mixer.music.load('assets/sounds/transito.mp3')
    pygame.mixer.music.set_volume(0.6)
    pygame.mixer.music.load('assets/sounds/drift.mp3')
    pygame.mixer.music.set_volume(0.6)

    batida_sound = pygame.mixer.Sound('assets/sounds/batida.mp3')

    jogo = True

    #cria objetos do jogo
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

    #lista de ruas para animação do fundo
    lista_ruas = [rua_img,rua2_img,rua3_img,rua4_img,rua5_img,rua6_img,rua7_img,rua8_img,rua9_img,rua10_img]

    i = len(lista_ruas)-1

    

 #Construçao das classes de objetos   
    class Carro(pygame.sprite.Sprite):
        def __init__(self, img):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)
            
            #posicionamento inicial do carro principal
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.centerx = LARGURA / 2
            self.rect.bottom = ALTURA - 10
            self.speedx = 0
            self.speedy = 0

        def update(self):
            # Atualização da posição do carro principal
            self.rect.x += self.speedx
            self.rect.y += self.speedy

            # Mantem o carro principal dentro da tela
            if self.rect.right > LARGURA:
                self.rect.right = LARGURA
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.y < 0:
                self.rect.y = 0
            if self.rect.y>ALTURA - ALTURA_CARRO:
                self.rect.y = ALTURA - ALTURA_CARRO
                
    class Taxi(pygame.sprite.Sprite):
        def __init__(self, img,carros):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)
            self.carros = carros
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = (100)
            self.rect.y = (-500)
            self.speedx = (0)
            self.speedy = (4)
        def update(self):
            # Atualizando a posição do objeto
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            # Se o objeto passa do final da tela, sua nova posição  em x é sorteada aleatoriamente
            if self.rect.top > ALTURA:
                self.rect.x = (random.randint((0),(LARGURA-LARGURA_TAXI)))
                self.rect.y = (-130)
                self.speedx = (0)
                self.speedy = (v)
                colide = pygame.sprite.spritecollide(self, self.carros, False)
                while len(colide) > 1:
                    self.rect.x = (random.randint((0),(LARGURA-LARGURA_TAXI)))
                    colide = pygame.sprite.spritecollide(self, self.carros, False)
            
    class Carro_verde(pygame.sprite.Sprite):
        def __init__(self, img,carros):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)
            self.carros = carros
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = (170)
            self.rect.y = (-700)
            self.speedx = (0)
            self.speedy = (4)

        def update(self):
            # Atualizando a posição do objeto
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            # Se o objeto passa do final da tela, sua posição em x é sorteada aleatoriamente
            if self.rect.top > ALTURA:
                self.rect.x = (random.randint((0),(LARGURA-LARGURA_VERDE)))
                self.rect.y = (-700)
                self.speedx = (0)
                self.speedy = (v)
                colide = pygame.sprite.spritecollide(self, self.carros, False)
                #Impede que os objetos se sobreponham
                while len(colide) > 1:
                    self.rect.x = ((random.randint((0),(LARGURA-LARGURA_VERDE))))
                    colide = pygame.sprite.spritecollide(self, self.carros, False)
            
    class Carro_rosa(pygame.sprite.Sprite):
        def __init__(self, img,carros):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)
            self.carros = carros

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = (250)
            self.rect.y = (-700)
            self.speedx = (0)
            self.speedy = (5.4)

        def update(self):
            # Atualizando a posição do objeto
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            # Se o objeto passa do final da tela, sua nova posição em x é sorteada aleatoriamente 
            if self.rect.top > ALTURA:
                self.rect.x = (random.randint((0),(LARGURA-LARGURA_ROSA)))
                self.rect.y = (-500)
                self.speedx = (0)
                self.speedy = (v)
                colide = pygame.sprite.spritecollide(self, self.carros, False)
                #Impede que os objetos se sobreponham
                while len(colide) > 1:
                    self.rect.x = ((random.randint((0),(LARGURA-LARGURA_ROSA))))
                    colide = pygame.sprite.spritecollide(self, self.carros, False)
            
    class Van(pygame.sprite.Sprite):
        def __init__(self, img,carros):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)
            self.carros = carros

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = (330)
            self.rect.y = (-700)
            self.speedx = (0)
            self.speedy = (6.1)

        def update(self):
            # Atualizando a posição do objeto
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            # Se o objeto passa do final da tela, sua nova posição em x é sorteada aleatoriamente 
            if self.rect.top > ALTURA:
                self.rect.x = (random.randint((0),(LARGURA-LARGURA_VAN)))
                self.rect.y = (-700)
                self.speedx = (0)
                self.speedy = (v)
                colide = pygame.sprite.spritecollide(self, self.carros, False)
                #Impede que os objetos se sobreponham
                while len(colide) > 1:
                    self.rect.x = ((random.randint((0),(LARGURA-LARGURA_VAN))))
                    colide = pygame.sprite.spritecollide(self, self.carros, False)
            
    class Polícia(pygame.sprite.Sprite):
        def __init__(self, img,carros):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)
            self.carros = carros

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = (360)
            self.rect.y = (-200)
            self.speedx = (0)
            self.speedy = (4.7)

        def update(self):
            # Atualizando a posição do objeto
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            # Se o objeto passa do final da tela, sua nova posição em x é sorteada aleatoriamente 
            if self.rect.top > ALTURA:
                self.rect.x = (random.randint((0),(LARGURA-LARGURA_POLÍCIA)))
                self.rect.y = (-400)
                self.speedx = (0)
                self.speedy = (v)
                colide = pygame.sprite.spritecollide(self, self.carros, False)
                #Impede que os objetos se sobreponham
                while len(colide) > 1:
                    self.rect.x = (random.randint((0),(LARGURA-LARGURA_POLÍCIA)))
                    colide = pygame.sprite.spritecollide(self, self.carros, False)
            
    class Caminhão(pygame.sprite.Sprite):
        def __init__(self, img,carros):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)
            self.carros = carros

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = (-200)
            self.rect.y = (-400)
            self.speedx = (0)
            self.speedy = (6.8)

        def update(self):
            #  Atualizando a posição do objeto
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            # Se o objeto passa do final da tela, sua nova posição em x é sorteada aleatoriamente 
            if self.rect.top > ALTURA:
                self.rect.x = (random.randint((0),(LARGURA-LARGURA_CAMINHÃO)))
                self.rect.y = (-400)
                self.speedx = (0)
                self.speedy = (v)
                colide = pygame.sprite.spritecollide(self, self.carros, False)
                #Impede que os objetos se sobreponham
                while len(colide) > 1:
                    self.rect.x = ((random.randint((0),(LARGURA-LARGURA_CAMINHÃO))))
                    colide = pygame.sprite.spritecollide(self, self.carros, False)

    #carrega as classes       
    jogadô = Carro(carro_img)
    clock = pygame.time.Clock()
    FPS = 60
    all_sprites = pygame.sprite.Group()
    carros = pygame.sprite.Group()

    for i in range(1):
        taxi = Taxi(taxi_img,carros)
        carro_verde = Carro_verde(verde_img,carros)
        carro_rosa = Carro_rosa(carro_rosa_img,carros)
        van = Van(van_img,carros)
        polícia = Polícia(polícia_img,carros)
        caminhão = Caminhão(caminhão_img,carros)
        all_sprites.add(jogadô,carro_verde,taxi)
        carros.add(taxi,carro_verde,caminhão,carro_rosa,polícia,van)
    #toca a música em loop
    pygame.mixer.music.play(loops=-1)
  
    while jogo:

        clock.tick(FPS)
    #estabelece a movimentação do carro principal
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade, ou seja a posição
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
                # Dependendo da tecla, altera a velocidade, ou seja a posição.
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
            #cria a opção de sair do jogo       
            if event.type == pygame.QUIT:
                jogo = False
        #cria a lista de carros que serão adicionados ao longo do jogo
        lista_adicionais = [polícia,carro_rosa,van,caminhão]

        #cria a condição de adição dos novos carros, de acordo com a pontuação e aumenta a velocidade dos carros
        if score_750 == 750 and c < len(lista_adicionais):
            all_sprites.add(lista_adicionais[c])
            score_750 = 0
            c += 1

        if score_100 == 100:
            score_100 == 0
            v += 0.1

        #coloca o fundo do jogo e estabelece os parâmetros da janela
        all_sprites.update()
        #loop da tela de aviso
        while mova:
            window.blit(lista_ruas[i], (0, 0))
            window.blit(carro_img,(265,470))
            text_surface = aviso.render('NÃO BATA NOS CARROS!', True, 	(255,0,0))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (300,200)
            window.blit(text_surface,text_rect)
            for event in pygame.event.get():
                # #verifica se o usuário apertou quit e fecha o jogo
                    if event.type == pygame.QUIT:
                        mova = False
                        end = False
            #define o tempo em que o aviso aparecerá na tela
            if tempo == 2000:
                end = True
                mova = False
                i = 0
            tempo += 1
            tempo_ruas += 1
            #animação das ruas
            if tempo_ruas == 15:
                tempo_ruas = 0
                i -= 1
            if i < 0:
                i = len(lista_ruas)-1    
            pygame.display.update()

        window.blit(lista_ruas[i], (0, 0))
        all_sprites.draw(window)
    
    #altera a cor do score de acordo com a pontuação
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
            text_rect.midtop = (LARGURA / 2,  10    )
            window.blit(text_surface, text_rect)
        
        elif score >= 5000:
            text_surface = Pontuação.render("{:08d}".format(score), True, (255, 0, 0))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (LARGURA / 2,  10)
            window.blit(text_surface, text_rect)

        #incrementa o score continuamente ao longo do tempo
        score += 1
        score_750 += 1
        score_100 += 1

        pygame.display.update() 

        #loop da animação das ruas
        i -= 1
        if i < 0:
            i = len(lista_ruas)-1

        #verifica se houve colisão entre o carro principal e os demais objetos
        hits = pygame.sprite.spritecollide(jogadô, carros, True)
        #caso haja colisão, termina o jogo e atualiza para a tela final
        if len(hits)>0:
            tela_final = pygame.image.load('assets/Images/tela_final.png').convert()
            #toca o som de batida com a colisão
            batida_sound.play()
            pygame.mixer.music.set_volume(0.1)
            end = True
            GAME = False
            jogo = False
            #adiciona o score atual na lista de scores
            lista_score.append(score)
            #verifica qual o maior score e atualiza a variável com ele
            for pontos in lista_score:
                if pontos >= high_score:
                    high_score = pontos

            while end:
                window.blit(tela_final, (0, 0))
                text_surface = Pontuação.render("{:08d}".format(high_score), True, 	(255,255,255))
                text_rect = text_surface.get_rect()
                text_rect.midtop = (450,530)
                window.blit(text_surface, text_rect)
                text_surface = Pontuação.render("high_score:", True, 	(255,255,255))
                text_rect = text_surface.get_rect()
                text_rect.midtop = (190,530)
                window.blit(text_surface, text_rect)
                for event in pygame.event.get():
                # #verifica se o usuário apertou quit e fecha o jogo
                    if event.type == pygame.QUIT:
                        end = False
                #verifica se o jogador apertou o espaço e reinicia o jogo
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_SPACE:
                            GAME = True
                            end = False
                
                pygame.display.update()
        #verifica se o usuário apertou quit e fecha o jogo
        if event.type == pygame.QUIT:
            jogo = False
            GAME = False 
pygame.quit() 