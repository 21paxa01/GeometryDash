import pygame

import hero as HERO
class Spike():
    """
    Класс для создания шипов,
    при взаимодействии с которыми игрок проигрывает.
    """
    def __init__(self,screen):
        """
        Инициализация шипа
        :param screen:игровое окно
        """
        self.screen=screen
        self.image=pygame.image.load("sprites/spike.png")
        self.spike=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.spike.centery=self.screen_rect.centery
        self.spike.bottom=self.screen_rect.bottom
        self.spike.centerx=1250
        self.spike.centery=850
        self.hero = HERO.Hero(self.screen)
        self.up=False
    def Draw(self,hero):
        """
        Отрисовка шипа
        :param hero:игровой персонаж
        :return: None
        """
        self.screen.blit(self.image,self.spike)
        self.spike.centerx-=5
        if self.spike.centerx==-50 :
            self.spike.centerx=1250
            if self.up==False:
                self.spike.centery=850
            else:
                self.spike.centery=-50
        if hero.hero.centerx>=self.spike.centerx-50 and hero.hero.centerx<=self.spike.centerx+50 and hero.hero.centery>=self.spike.centery-40and hero.hero.centery<=self.spike.centery+40:
            HERO.restart=-1
