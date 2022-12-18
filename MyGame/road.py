import pygame
import hero as Hero
import traps
class Road():
    """
    Класс для создания блоков дороги,
    по которым может перемещаться игровой персонаж
    """
    def __init__(self,screen,y):
        """
        Инициализация дороги
        :param screen:игровое окно
        :param y:высота, на которой появится дорога
        """
        self.screen=screen
        self.test=False
        self.image=pygame.transform.scale(pygame.image.load("sprites/road.png"),(100,100))
        self.image1=pygame.transform.scale(self.image,(100,100))
        self.image2=pygame.transform.scale(self.image,(100,200))
        self.image3=pygame.transform.scale(self.image,(100,300))
        self.image4=pygame.transform.scale(self.image,(100,400))
        self.up_image1=pygame.transform.rotate(self.image1,180)
        self.up_image2=pygame.transform.rotate(self.image2,180)
        self.up_image3=pygame.transform.rotate(self.image3,180)
        self.up_image4=pygame.transform.rotate(self.image4,180)
        self.road=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.road.centery=self.screen_rect.centery
        self.road.bottom=self.screen_rect.bottom
        self.road.centerx=900
        self.road.centery=y
        self.image_chek=1
    def Draw(self, hero):
        """
        Отрисовка дороги снизу экрана
        :param hero:игровой пресонаж
        :return: None
        """
        #self.hero=Hero(self.screen)
        self.screen.blit(self.image,self.road)
        if(self.road.centery==750):
            self.image=self.image1
        elif(self.road.centery==650):
            self.image=self.image2
        elif(self.road.centery==550):
            self.image=self.image3
        elif(self.road.centery==450):
            self.image=self.image4
        if self.road.centerx>-50 :
            self.road.centerx-=5
        if(self.road.centerx==0):
            Hero.meters+=1
        if self.road.centerx==-50:
            self.road.centerx=1250
            self.road.centery=750
    def UP_Draw(self, hero):
        """
        Отрисовка дороги сверху экрана
        :param hero:игровой персонаж
        :return: None
        """
        #self.hero=Hero(self.screen)
        self.screen.blit(self.image,self.road)
        if(self.image_chek==1):
            self.image=self.up_image1
        elif(self.image_chek==2):
            self.image=self.up_image2
        elif(self.image_chek==3):
            self.image=self.up_image3
        elif(self.image_chek==4):
            self.image=self.up_image4
        if self.road.centerx>-50 :
            self.road.centerx-=5
        if self.road.centerx==-50:
            self.road.centerx=1250
            self.image_chek=1
            self.road.centery=50
class BackGround():
    """
    Класс для создания заднего фона
    """
    def __init__(self,screen):
        """
        Инициализация заднего фона
        :param screen:игровое окно
        """
        self.screen=screen
        self.bg_image=pygame.image.load("sprites/level_bg.png")
        self.bg=self.bg_image.get_rect()
        self.bg_screen_rect=screen.get_rect()
        self.bg.centery=self.bg_screen_rect.centery
        self.bg.bottom=self.bg_screen_rect.bottom
        self.bg.centerx=600
    def BG_Draw(self):
        """
        Отрисовка заднего фона
        :return: None
        """
        self.screen.blit(self.bg_image, self.bg)
