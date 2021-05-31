import pygame
from plane_sprites import  *

pygame.init()

screen = pygame.display.set_mode((480,700))

bg = pygame.image.load('./images/background.png')
screen.blit(bg,(0,0))

hero = pygame.image.load('./images/me1.png')
screen.blit(hero,(200,300))

pygame.display.update()

clock = pygame.time.Clock()

hero_rect = pygame.Rect(200,300,102,126)

#创建敌机的景林
enemy = GameSprite('./images/enemy1.png')
enemy1 = GameSprite('./images/enemy1.png',2)
#创建敌机的景林组
enemy_group = pygame.sprite.Group(enemy,enemy1)

while True:
    clock.tick(60)

    # event_list = pygame.event.get()
    # if len(event_list)>0:
    #     print((event_list))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print('游戏推出')

            pygame.quit()
            exit()

    hero_rect.y -= 1

    if hero_rect.y <= 0:
        hero_rect.y = 700

    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)

    # 让精灵组 调用两个方法
    # update-让组中的所有精灵更新位置
    enemy_group.update()
    # draw- 在screen画出所有的精灵
    enemy_group.draw(screen)


    pygame.display.update()
    pass

pygame.quit()