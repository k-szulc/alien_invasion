import pygame
from pygame.sprite import Sprite

import game_functions as gf

class Alien(Sprite):

    def __init__(self, ai_settings, screen):

        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load(gf.get_path()+'/images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)


    def blitme(self):

        self.screen.blit(self.image, self.rect)
