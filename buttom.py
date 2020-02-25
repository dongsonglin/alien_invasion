import pygame

class Buttom():
    def __init__(self,screen,mes):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width,self.height = 200,50
        self.color = (0,255,0)
        self.test_color = (255,255,255)
        self.font = pygame.font.SysFont(None,40)

        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        self.prep_mes(mes)

    def prep_mes(self,mes):
        self.mes_image = self.font.render(mes,True,self.test_color,self.color)
        self.mes_rect = self.mes_image.get_rect()
        self.mes_rect.center = self.rect.center

    def draw_buttom(self):
        self.screen.fill(self.color,self.rect)
        self.screen.blit(self.mes_image,self.mes_rect)