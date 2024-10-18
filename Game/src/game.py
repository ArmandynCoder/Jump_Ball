from src.relogio import Relogio
import pygame
from pygame.locals import *
from sys import exit


class Bola:
    def __init__(self):
        pygame.init()
        self.__tempo = Relogio()
        self.altura = 400
        self.largura = 900
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Pula Pula")
        self.loop = True
        self.raio_bola = 20
        self.bola_x = 10 + self.raio_bola
        self.bola_y = self.altura - self.raio_bola
        self.y_quadrado = self.altura
        self.velocidade_bola = 0
        self.forca_pulo = -15
        self.gravidade = 1
        self.pulando = False
        self.tronco_x = 850
        self.velocidade_tronco = 10
    
    # def temporizador(self):
    #     self.__tempo.segundos()
    
    def rodando(self):
        self.__tempo.segundos()
        while self.loop:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.loop = False
                    pygame.quit()
                    exit()
                
            
                if event.type == KEYDOWN:
                    if event.key == K_SPACE and not self.pulando:
                        self.velocidade_bola = self.forca_pulo
                        self.pulando = True
            
            self.velocidade_bola += self.gravidade
            self.bola_y += self.velocidade_bola
            
            if self.bola_y >= self.altura - self.raio_bola:
                self.bola_y = self.altura - self.raio_bola
                self.velocidade_bola = 0
                self.pulando = False
            if self.bola_x <= 0 + self.raio_bola:
                self.bola_x = 0 + self.raio_bola
            
            self.tela.fill((147,180,215))
            bola = pygame.draw.circle(self.tela, (255,0,0), (self.bola_x, int(self.bola_y)), self.raio_bola)
            tronco = pygame.draw.rect(self.tela, (140,95,78), (self.tronco_x, 350, 30, 200))
            
            self.tronco_x -= self.velocidade_tronco
            
            if bola.colliderect(tronco):
                self.loop = False
                pygame.quit()
                exit()

            if self.tronco_x <= -5:
                self.tronco_x = 900
            
            pygame.time.Clock().tick(60)
            self.__tempo.segundos()
            pygame.display.flip() 
        pygame.quit()