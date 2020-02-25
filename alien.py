import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,screen,ai_setting):
        super().__init__()
        self.screen = screen
        self.image1 = pygame.image.load('images/alien.png')
        width, height = self.image1.get_size()
        self.image = pygame.transform.smoothscale(self.image1,(width//4,height//4))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.speed = ai_setting.alien_speed
        self.speed_factor = ai_setting.direction
        self.dorp_speed = ai_setting.alien_drop_speed

    def check_edge(self):
        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        else: return False

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def update(self, *args):
        self.rect.x -= (self.speed * self.speed_factor)