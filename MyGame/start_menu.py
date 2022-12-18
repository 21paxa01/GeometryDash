import pygame

class StartMenu():
    def __init__(self,screen):
        """
        Инициализация стартового меню
        :param screen: игровое окно
        """
        self.screen=screen
        self.image=pygame.image.load("sprites/background.png")
        self.logo_image=pygame.image.load("sprites/logo.png")
        self.logo=self.logo_image.get_rect()
        self.logo.centery=200
        self.logo.centerx=650
        self.start_bg=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.start_bg.centerx=600
        self.start_bg.centery=400
        self.start_bg.bottom=self.screen_rect.bottom
    def StartGame(self):
        """
        Отрисовка стартового меню
        :return: None
        """
        self.screen.blit(self.image, self.start_bg)
        self.screen.blit(self.logo_image,self.logo)