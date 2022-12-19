import pygame
import sys
import Buttons
import hero as Hero
jump_chek=0
def event(hero):
    """
    Эта функция отвечает за управление персонажем.
    Она реагирует на взаимодейстие игрока с клавиатурой и мышкой.
    При нажаитии на определенные кнопки будут выполняться соответствующие функции.
    :param hero:игровой персонаж
    :return: None
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                if hero.hero_sprite=="ship":
                    hero.hero_up=True
                    hero.ship_kef=1
                    Hero.onRoad=False
                if hero.hero_sprite=="deafolt":
                    if(Hero.onRoad==True):
                        hero.hero_jump_high=hero.hero.centery-300
                        hero.hero_jump=True
                if hero.hero_sprite=="flip":
                    if (Hero.onRoad == True):
                        hero.hero_jump_high = hero.hero.centery + 300
                        hero.hero_jump = True
                if hero.hero_sprite=="ball":
                    if(Hero.onRoad==True):
                        hero.hero_up=True
                    if(Hero.underRoad==True):
                        hero.hero_up=False
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_SPACE:
                if hero.hero_sprite == "ship":
                    hero.hero_up=False
                    Hero.onRoad=False
                    hero.ship_kef=1
                if hero.hero_sprite=="deafolt":
                        hero.hero_jump=False
                if hero.hero_sprite=="flip":
                        hero.hero_jump=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                Buttons.onMouse=True
        elif event.type==pygame.MOUSEBUTTONUP:
            if event.button==1:
                Buttons.onMouse=False