import pygame


class Ship:
    def __init__(self, screen, ai_setting):
        self.screen = screen  # ship 所处屏幕是screen
        self.ai_setting = ai_setting  # 在飞船类中使用设置类的对象

        self.image = pygame.image.load('images/rocket.bmp')  # 加载照片
        width, height = self.image.get_size()  # 图片的宽，高
        self.image1 = pygame.transform.smoothscale(self.image, (width // 4, height // 4))  # 将原图尺寸缩小1/4后记录为image1
        self.rect = self.image1.get_rect()  # 图片的矩形的值为图片image1获取到的矩形的值x,y
        self.screen_rect = screen.get_rect()  # 用变量存储 屏幕整体的矩形坐标

        #self.centers = float(self.screen_rect.centerx)  # 新建一个属性 将转为小数形式的坐标给他复制
        # 收获1 不能在函数里乱用''''''可能会打断定义函数
        # 收获2 如果给self.centers 直接用小数赋值，飞机将去到赋值到位置，因为程序在不断到循环，马上会在update_ship里用这个小数定位
        self.rect.centerx = self.screen_rect.centerx  # 将ship放置于屏幕中间
        self.rect.bottom = self.screen_rect.bottom  # 将其放置于屏幕底部



        self.moving_right = False  # 初始化向右属性
        self.moving_left = False  # 初始化向左属性
        self.moving_up = False
        self.moving_down = False


    def blitme(self):
        self.screen.blit(self.image1, self.rect)  # 在屏幕上画自己（飞船）

    # 根据指示移动飞船
    def update_ship(self):
        if self.moving_right is True and self.rect.right < self.screen_rect.right:  # 用and来使飞船不飞出屏幕
            self.rect.centerx += self.ai_setting.ship_speed
        if self.moving_left is True and self.rect.left > 0:
            self.rect.centerx -= self.ai_setting.ship_speed
        #self.rect.centerx = self.centers  # 将小数型变量交给矩形坐标     j

        if self.moving_up is True and self.rect.y > 0:
            self.rect.y -= self.ai_setting.ship_speed
        if self.moving_down is True and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.ai_setting.ship_speed


    def replace_center(self):
        self.rect.centerx = 600
        self.rect.bottom = self.screen_rect.bottom

