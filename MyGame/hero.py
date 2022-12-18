import pygame

onRoad=False
underRoad=False
meters=0
restart=0
finish=False
class Hero():
    """
    Класс для создания игрового персонажа.
    Вкслючает в себя несколько игровых режимов
    """
    def __init__(self,screen):
        """
        Инициализация персонажа
        :param screen:
        """
        self.screen=screen
        self.image=pygame.image.load("sprites/deafolt.png")
        self.hero=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.hero.centery=self.screen_rect.centery
        self.hero.centerx=200
        self.hero.centery=650
        self.hero_up=False
        self.hero_jump=False
        self.hero_sprite="deafolt"
        self.ship_time=0
        self.deafolt_time = 0
        self.rotate_image=self.image
        self.ship_rotate_image = pygame.image.load("sprites/ship.png")
        self.angle=0
        self.ship_angle=0
        self.hero_jump_chek_up=False
        self.hero_jump_chek=0
        self.hero_jump_high=self.hero.centery-300
        self.onMouse=False
        self.array_i=0
        self.up_array_i=0
        self.ship_kef=1
    def Draw(self):
        """
        Отрисовка персонажа
        :return: None
        """
        self.screen.blit(self.image,self.hero)
    def Hero_pos(self):
        """
        Отслеживание позиции персонажа.
        Перемещение персонажа в зависимости от его состояния.
        :return: None
        """
        if self.hero_sprite=="ship":
            self.hero.centery -= 2 * (self.ship_angle/10)
        if self.hero_sprite=="deafolt":
            if self.hero_jump==False and self.hero_jump_chek==0 and onRoad==False:
                self.hero.centery+=5
        if self.hero_sprite=="flip":
            if self.hero_jump==False and self.hero_jump_chek==0 and onRoad==False:
                self.hero.centery-=5
        if self.hero_sprite=="ball":
            if self.hero_up==True and underRoad==False:
                self.hero.centery-=7.5
            elif self.hero_up==False and onRoad==False:
                self.hero.centery+=7.5
    def Ship(self):
        """
        Переход в лежим летающего корабля.
        При удержании пробела персонаж летит вверх,
        иначе падает вниз.
        :return: None
        """
        self.image=pygame.image.load("sprites/ship.png")
        self.hero_sprite="ship"
    def Deafolt(self):
        """
        Переход в обычный режим.
        Персонаж двигается вперед и может совершить прыжок,
        если в этот момент находится на земле.
        :return: None
        """
        self.hero_up = False
        self.image=pygame.image.load("sprites/deafolt.png")
        self.rotate_image=self.image
        self.hero_sprite="deafolt"
    def Flip(self):
        """
        Переход в режим с обратной гравитацией.
        :return: None
        """
        self.hero_sprite="flip"
        self.hero_jump_chek_up=True
        self.hero_jump=False
    def Ball(self):
        """
        Переход в режим шара.
        Шар может тольк двигаться вперед,
        но если игрой находится на земле и нажимает на пробел,
        то происходит смена гравитации.
        :return: None
        """
        self.image=pygame.image.load("sprites/ball.png")
        self.rotate_image=self.image
        self.hero_sprite="ball"
        self.hero_up=False
    def Rotate(self):
        """
        Вращение персонажа в зависимости от его состоянияю
        :return: None
        """
        if self.hero_sprite=="deafolt":
            self.image=pygame.transform.rotate(self.rotate_image,self.angle)
            if onRoad==False:
                self.angle-=2
            if onRoad==True:
                self.angle-=self.angle%90
        if self.hero_sprite=="flip":
            self.image = pygame.transform.rotate(self.rotate_image, self.angle)
            if onRoad == False:
                self.angle += 2
            if onRoad == True:
                self.angle -= self.angle % 90
        if self.hero_sprite=="ship":
            if(onRoad==False and underRoad==False):
                if self.hero_up==True and self.ship_angle<30 and underRoad == False:
                    self.ship_angle+=0.5
                elif self.hero_up==False and self.ship_angle>-30 and onRoad==False:
                    self.ship_angle-=0.5
            if(onRoad==True or underRoad==True):
                self.ship_angle=0
            self.image=pygame.transform.rotate(self.ship_rotate_image,self.ship_angle)
        if self.hero_sprite=="ball":
            self.image = pygame.transform.rotate(self.rotate_image, self.angle)
            if self.hero_up==True:
                self.angle+=4
            else:
                self.angle-=4
        self.hero=self.image.get_rect(center=self.hero.center)
    def Jump(self):
        """
        Функция реализует прыжок персонажа.
        Прыжок предназначен для преодоления препятствий.
        :return: None
        """
        if self.hero_sprite=="deafolt":
            if(self.hero_jump==True or self.hero_jump_chek==1):
                self.hero_jump_chek=1
                if self.hero.centery>self.hero_jump_high and self.hero_jump_chek_up==False:
                        self.hero.centery-=7.5
                        if self.hero.centery <= self.hero_jump_high:
                            self.hero_jump_chek_up=True
                elif onRoad==False and self.hero_jump_chek_up==True:
                    self.hero.centery+=7.5
                elif onRoad==True:
                    #self.hero_jump=False
                    self.hero_jump_chek_up=False
                    self.hero_jump_chek=0
                    self.hero_jump_high=self.hero.centery-300
        if(self.hero_sprite=="flip"):
            if (self.hero_jump == True or self.hero_jump_chek == 1):
                self.hero_jump_chek = 1
                if self.hero.centery < self.hero_jump_high and self.hero_jump_chek_up == False:
                    self.hero.centery += 7.5
                    if self.hero.centery >= self.hero_jump_high:
                        self.hero_jump_chek_up = True
                elif onRoad == False and self.hero_jump_chek_up == True:
                    self.hero.centery -= 7.5
                elif onRoad == True:
                    # self.hero_jump=False
                    self.hero_jump_chek_up = False
                    self.hero_jump_chek = 0
                    self.hero_jump_high = self.hero.centery + 300

    def ChekRoad(self,array,up_array):
        """
        Функция проверяет,где находится персонаж.
        :param array:
        :param up_array:
        :return:
        (-3)-персонаж под потолком
        (-2)-песонаж не под потолком
        (-1)-персонаж врезался в обьект(поражение)
        0-персонаж не на дороге.
        1-персонаж на дороге
        3-уровень пройден
        """
        if self.hero_sprite=="deafolt":
            if meters > 552:
                return 3
            if(meters>array[self.array_i][1]+10 and self.array_i<len(array)-1):
                self.array_i+=1
            if(self.hero.centery-50<90):
                return -1
            if (meters>=array[self.array_i][0]+9 and meters<=array[self.array_i][1]+10 ):
                if(self.hero.centery<750-100*array[self.array_i][2]):
                    return 0
                elif(self.hero.centery<750-100*array[self.array_i][2]+15):
                    if(self.hero.centery>750-100*array[self.array_i][2]):
                        self.hero.centery=750-100*array[self.array_i][2]
                    return 1
                else:
                    return -1
            else:
                if(self.hero.centery<650):
                    return 0
                elif(self.hero.centery>=650):
                    return 1
        elif self.hero_sprite=="flip":
            if (meters > up_array[self.up_array_i][1] + 10 and self.up_array_i < len(up_array)-1):
                self.up_array_i += 1
            if (self.hero.centery + 50 > 760):
                return -1
            if (meters >= up_array[self.up_array_i][0] + 9 and meters <= up_array[self.up_array_i][1] + 10):
                if (self.hero.centery > 50 + 100 * up_array[self.up_array_i][2]):
                    return 0
                elif (self.hero.centery > 50 + 100 * up_array[self.up_array_i][2] - 15):
                    if (self.hero.centery < 50 + 100 * up_array[self.up_array_i][2]):
                        self.hero.centery = 50 + 100 * up_array[self.up_array_i][2]
                    return 1
                else:
                    return -1
            else:
                if (self.hero.centery > 150):
                    return 0
                elif (self.hero.centery <= 150):
                    return 1
        elif self.hero_sprite=="ship":
            if(meters>array[self.array_i][1]+10 and self.array_i<len(array)-1):
                self.array_i+=1
            if(meters>up_array[self.up_array_i][1]+10 and self.up_array_i<len(up_array)-1):
                self.up_array_i+=1
            if(self.hero.centery-40<=100 and self.hero_up==True):
                self.hero.centery=140
                return -2
            if(self.hero.centery<=400):
                if (meters >= up_array[self.up_array_i][0] + 9 and meters <= up_array[self.up_array_i][1] + 10):
                    if (self.hero.centery > 40 + 100 * array[self.array_i][2]):
                        return -3
                    elif (self.hero.centery > 40 + 100 * array[self.array_i][2] - 10):
                        if (self.hero.centery <= 40 + 100 * array[self.array_i][2] and self.hero_up==True):
                            self.hero.centery = 40 + 100 * array[self.array_i][2]
                            return -2
                        elif(self.hero.centery > 40 + 100 * array[self.array_i][2] and self.hero_up==False):
                            return -3
                    else:
                        return -1
                if (self.hero.centery <= 140):
                    if(self.hero_up == True):
                        self.hero.centery = 140
                        return -2
                    else:
                        self.hero.centery = 141
                        return -3
            else:
                if (meters>=array[self.array_i][0]+9 and meters<=array[self.array_i][1]+10):
                    if(self.hero.centery<760-100*array[self.array_i][2]):
                        return 0
                    elif(self.hero.centery<760-100*array[self.array_i][2]+10):
                        if(self.hero.centery>=760-100*array[self.array_i][2]and self.hero_up==False):
                            self.hero.centery=760-100*array[self.array_i][2]
                            return 1
                        elif(self.hero.centery<760-100*array[self.array_i][2]and self.hero_up==True):
                            return 0
                    else:
                        return -1
                if (self.hero.centery >= 660):
                    if(self.hero_up == False):
                        self.hero.centery = 660
                        return 1
                    else:
                        self.hero.centery = 659
                        return 0
        elif self.hero_sprite=="ball":
            if (meters > array[self.array_i][1] + 10 and self.array_i < len(array) - 1):
                self.array_i += 1
            if (meters > up_array[self.up_array_i][1] + 10 and self.up_array_i < len(up_array) - 1):
                self.up_array_i += 1
            if(self.hero.centery>650 and onRoad==False):
                self.hero.centery=650
                return 1
            elif(self.hero.centery<150 and underRoad==False):
                self.hero.centery=150
                return -2
            elif(self.hero_up==True and self.hero.centery<650 and onRoad==True):
                return 0
            elif(self.hero_up==False and self.hero.centery>150 and underRoad==True):
                return -3
            if (self.hero.centery <= 400):
                if (meters >= up_array[self.up_array_i][0] + 9 and meters <= up_array[self.up_array_i][1] + 10):
                    if (self.hero.centery > 50 + 100 * array[self.array_i][2]):
                        return -3
                    elif (self.hero.centery > 50 + 100 * array[self.array_i][2] - 10):
                        if (self.hero.centery <= 50 + 100 * array[self.array_i][2] and self.hero_up == True):
                            self.hero.centery = 50 + 100 * array[self.array_i][2]
                            return -2
                        elif (self.hero.centery > 50 + 100 * array[self.array_i][2] and self.hero_up == False):
                            return -3
                    else:
                        return -1
                if(self.hero.centery>150):
                    return -3
            else:
                if (meters >= array[self.array_i][0] + 9 and meters <= array[self.array_i][1] + 10):
                    if (self.hero.centery < 750 - 100 * array[self.array_i][2]):
                        return 0
                    elif (self.hero.centery < 750 - 100 * array[self.array_i][2] + 10):
                        if (self.hero.centery >= 750 - 100 * array[self.array_i][2] and self.hero_up == False):
                            self.hero.centery = 750 - 100 * array[self.array_i][2]
                            return 1
                        elif (self.hero.centery < 750 - 100 * array[self.array_i][2] and self.hero_up == True):
                            return 0
                    else:
                        return -1
                if(self.hero.centery<650):
                    return 0

