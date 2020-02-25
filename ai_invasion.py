import sys
import pygame
from pygame.sprite import Group
from setting import Setting
from ship import Ship
import game_function as gf
from alien import Alien
ai_setting = Setting()
from game_state import GameState
from buttom import Buttom

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption(ai_setting.title)
    bg_color = ai_setting.bg_color
    ship = Ship(screen, ai_setting)
    bullet: Group = pygame.sprite.Group()
    aliens = Group()
    state = GameState(ai_setting)
    gf.create_fleet(screen, aliens, ai_setting, ship)
    play_buttom = Buttom(screen,"Play")

    while True:
        gf.check_events(ship,ai_setting,screen,bullet,play_buttom,state,aliens)
        if state.game_active is True:
            ship.update_ship()
            gf.update_bullet(bullet,aliens,screen,ai_setting,ship)
            gf.update_aliens(aliens,ai_setting,ship,state,bullet,screen)
        gf.update_screen(bg_color, screen, ship, bullet, aliens,state,play_buttom)


run_game()

