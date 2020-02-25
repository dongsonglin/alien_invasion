import sys
import pygame


def run_game():
    screen = pygame.display.set_mode((1800,900))
    pygame.display.set_caption('这次也很牛逼')

    bullet = pygame.draw.rect(screen,(200,20,20),(50,50,500,50))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.K_DOWN:
                if event.key == pygame.K_q:
                    sys.exit()
        pygame.display.flip()











run_game()