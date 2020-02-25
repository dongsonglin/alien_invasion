import pygame

class GameState():
    def __init__(self,ai_setting):
        self.setting = ai_setting
        self.reset_state()
        self.game_active = False


    def reset_state(self):
        self.ship_left = self.setting.ship_limit


