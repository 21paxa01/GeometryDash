import pygame

meters_arr=[138,271,283,422,552]
images=["sprites/portal_ship_left.png","sprites/portal_ship_right.png","sprites/portal_deafolt_left.png","sprites/portal_deafolt_right.png","sprites/portal_flip_left.png","sprites/portal_flip_right.png","sprites/portal_ball_left.png","sprites/portal_ball_right.png","sprites/portal_deafolt_left.png","sprites/portal_deafolt_right.png"]
import hero as Hero
class Portal():
    """
    Класс для создания порталов в нашей игре.
    После того,как игрок пройдет через портал,
    в зависимости от вида портала,режим героя
    изменится на соответствующий этому порталу.
    """
    def __init__(self, screen, img):
        """
        Инициализация портала
        :param screen:игровое окно
        :param img:массив со спрайтами для порталов
        """
        self.screen=screen
        self.left_image=pygame.image.load(images[img])
        self.right_image=pygame.image.load(images[img+1])
        self.portal_left=self.left_image.get_rect()
        self.portal_right = self.right_image.get_rect()
        self.portal_right.centery,self.portal_left.centery=350,350
        self.portal_left.centerx,self.portal_right.centerx=1225,1225
        self.meters_i=0
    def Draw_left(self,hero,meters):
        """
        Отрисовка левой части портала
        :param hero: игровой персонаж
        :param meters: пройденные метры
        :return: None
        """
        self.left_image = pygame.image.load(images[self.meters_i*2])
        if(meters>=meters_arr[self.meters_i]):
            self.screen.blit(self.left_image,self.portal_left)
            self.portal_left.centerx-=10
            if hero.hero.centerx>self.portal_left.centerx:
                if(self.meters_i==0 and hero.hero_sprite=='deafolt'):
                    hero.Ship()
                if(self.meters_i==1 and hero.hero_sprite=="ship"):
                    hero.Deafolt()
                    Hero.onRoad=False
                if(self.meters_i==2 and hero.hero_sprite=="deafolt"):
                    hero.Flip()
                if (self.meters_i == 3 and hero.hero_sprite == "flip"):
                    hero.Ball()
                    Hero.onRoad=False
                if (self.meters_i == 4 and hero.hero_sprite == "ball"):
                    hero.Deafolt()
                    Hero.onRoad=False
        if (meters_arr[self.meters_i] < meters-10 and self.meters_i<4):
            self.meters_i += 1
            self.portal_left.centerx, self.portal_right.centerx = 1225, 1225
            if(self.meters_i==3):
                self.portal_left.centery, self.portal_right.centery = 550, 550
            if(self.meters_i==4):
                self.portal_left.centery, self.portal_right.centery = 450, 450
    def Draw_right(self,meters):
        """
        Отрисовка правой части портала
        :param meters: пройденные метры
        :return:None
        """
        self.right_image=pygame.image.load(images[self.meters_i*2+1])
        if(meters>=meters_arr[self.meters_i]):
            self.screen.blit(self.right_image,self.portal_right)
            self.portal_right.centerx-=10