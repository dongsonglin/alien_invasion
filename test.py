# main
import sys

import pygame


def run_game():

    pygame.init()
    screen = pygame.display.set_mode((1600, 800))
    pygame.display.set_caption('我是不是很牛逼')
    #以下为rocket相关
    rocket1 = pygame.image.load('images/rocket.bmp')
    width, height = rocket1.get_size()
    rocket = pygame.transform.scale(rocket1, (width // 4, height // 4))
    screen_rect = screen.get_rect()
    rocket_rect = rocket.get_rect()
    rocket_rect.center = screen_rect.center
    moving_right_state = False
    moving_left_state = False
    moving_up_state = False
    moving_down_state = False

    #以下内容为子弹





    while True:
        screen.fill((200, 200, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moving_right_state = True
                if event.key == pygame.K_LEFT:
                    moving_left_state = True
                if event.key == pygame.K_UP:
                    moving_up_state = True
                if event.key == pygame.K_DOWN:
                    moving_down_state = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    moving_right_state = False
                if event.key == pygame.K_LEFT:
                    moving_left_state = False
                if event.key == pygame.K_UP:
                    moving_up_state = False
                if event.key == pygame.K_DOWN:
                    moving_down_state = False

        if moving_right_state is True and rocket_rect.right < screen_rect.right:
            rocket_rect.centerx += 10
        if moving_left_state is True and rocket_rect.left > 0:
            rocket_rect.centerx -= 10
        if moving_up_state is True and rocket_rect.top > 0:
            rocket_rect.centery -= 10
        if moving_down_state is True and rocket_rect.bottom < screen_rect.bottom:
            rocket_rect.centery += 10

        screen.fill((200, 200, 200))
        screen.blit(rocket, rocket_rect)
        bullet = pygame.draw.rect(screen, (200, 50, 50), (400, 400, 5, 10))
        pygame.display.flip()


run_game()
