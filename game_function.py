import sys
import pygame
from bullet import Bullet
from alien import Alien
import time

def check_keydown(event, ship, ai_setting, screen,bullet):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True

    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_q:
        sys.exit()

#如果是空格键 创造子弹 加入子弹组里
    if event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullet.add(new_bullet)


def check_keyup(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False



def check_events(ship,ai_setting,screen,bullet,play_buttom,state,aliens):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, ship,ai_setting,screen,bullet)
        elif event.type == pygame.KEYUP:
            check_keyup(event,ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if state.game_active == False:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                check_play_buttom(play_buttom,mouse_x,mouse_y,state,aliens,bullet,ship)

def check_play_buttom(play_buttom,mouse_x,mouse_y,state,aliens,bullet,ship):
    if play_buttom.rect.collidepoint(mouse_x,mouse_y):
        state.game_active = True
        state.reset_state()
        aliens.empty()
        bullet.empty()
        ship.replace_center()
        #隐藏光标
        pygame.mouse.set_visible(False)




def update_screen(bg_color, screen, ship, bullet,aliens,state,play_buttom):
    screen.fill(bg_color)
    for bulleta in bullet.sprites():
        bulleta.drew_bullet()
    ship.blitme()
    aliens.draw(screen)
    if state.game_active == False:
        play_buttom.draw_buttom()
    pygame.display.flip()

def update_bullet(bullet,aliens,screen,ai_setting,ship):
    bullet.update()

    for spirit in bullet.sprites():
        if spirit.rect.bottom < 0:
            bullet.remove(spirit)
    deal_bullet_aliens(bullet,aliens,screen,ai_setting,ship)


def deal_bullet_aliens(bullet,aliens,screen,ai_setting,ship):
    #消灭碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullet,aliens,True,True)
    #判断是否全部消灭完 如果是 重新生成
    if len(aliens) == 0:
        bullet.empty()
        create_fleet(screen,aliens,ai_setting,ship)


def get_alien_numx(ai_setting,alien_width):
    available_space_x = ai_setting.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width) + 1)
    return number_alien_x

def get_num_rows(ai_setting,ship,alien_height):
    available_space_y = ai_setting.screen_height-3*alien_height-ship.rect.height
    number_rows = int(available_space_y/(2*alien_height)+1)
    return number_rows

def creat_alien(screen,alien_number,aliens,row_number,ai_setting):
    alien = Alien(screen,ai_setting)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.rect.x = alien_width + 2*alien_width*alien_number
    alien.rect.y = alien_height +2*alien_height*row_number
    aliens.add(alien)

def create_fleet(screen,aliens,ai_setting,ship):
    alien = Alien(screen,ai_setting)
    number_alien_x = get_alien_numx(ai_setting, alien.rect.width)
    row_numbers = get_num_rows(ai_setting, ship, alien.rect.height)

    for row_number in range(row_numbers):
        for alien_number in range(number_alien_x):
            creat_alien(screen, alien_number, aliens, row_number, ai_setting)


def check_fleet_edge(aliens,ai_setting):
    for alien in aliens.sprites():
        if alien.check_edge() is True:
            change_fleet_direction(aliens,ai_setting)

            break

def change_fleet_direction(aliens,ai_setting):
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.alien_drop_speed
        alien.speed_factor *=-1
    #ai_setting.direction *= -1


def alien_hit(state,bullet,aliens,screen,ai_setting,ship):
    if state.ship_left >0 :
        state.ship_left -= 1
        bullet.empty()
        aliens.empty()
        create_fleet(screen,aliens,ai_setting,ship)
        time.sleep(0.5)
        ship.replace_center()
    else:
        state.game_active = False
        pygame.mouse.set_visible(True)

def check_alien_bottom(aliens,screen,state,bullet,ai_setting,ship):
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.y >= screen_rect.bottom:
            alien_hit(state,bullet,aliens,screen,ai_setting,ship)
            break



def update_aliens(aliens,ai_setting,ship,state,bullet,screen):
    check_fleet_edge(aliens,ai_setting)
    check_alien_bottom(aliens,screen,state,bullet,ai_setting,ship)
    aliens.update(aliens,screen,state,bullet,ai_setting,ship)
    if pygame.sprite.spritecollideany(ship,aliens):
        alien_hit(state,bullet,aliens,screen,ai_setting,ship)