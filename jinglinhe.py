import pygame

SCREEN_RECT = pygame.Rect(0,0,480,700)


FRAME_PER_SCE = 60
class GameSprite(pygame.sprite.Sprite):
    def __init__(self,image_name,speed=1):

        super().__init__()
        #定义 图片 位置 速度
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed


    def  update(self):
        #在屏幕的垂直方向 上移动
        self.rect.y += self.speed