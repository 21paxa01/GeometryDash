import pygame
onMouse=False
class Button():
    """
    Класс для создания кнопок,после нажатия на которые
    выполняются соответствующие функции
    """
    def __init__(self,screen):
        """
        Инициализация кнопки
        :param screen:игровое окно
        """
        self.screen=screen
        self.image_off=pygame.image.load("sprites/Play_button.png")
        self.image_on = pygame.image.load("sprites/Play_button_on.png")
        self.image=self.image_off
        self.button=self.image.get_rect()
        self.startgame=False
        self.clicksound=pygame.mixer.Sound("sounds/clicksoundeffect.mp3")
        self.sound_chek=False
        self.sound=pygame.mixer.Sound("sounds/onButton.mp3")
    def Draw(self):
        """
        Отрисовка кнопки
        :return: None
        """
        self.screen.blit(self.image,self.button)
    def StartGame(self):
        """
        Запуск игрового цикла
        :return: None
        """
        self.startgame=True
    def ClickChek(self,rad):
        """
        Проверка позиции курсора мыши и нажатия на ЛКМ.
        Игра запустится, если игрок навелся на кнопку и нажал ЛКМ.
        :param rad:радиус кнопки
        :return: None
        """
        self.mouse_pos=pygame.mouse.get_pos()
        if(self.mouse_pos[0]>self.button.centerx-rad and self.mouse_pos[0]<self.button.centerx+rad and self.mouse_pos[1]>self.button.centery-rad and self.mouse_pos[1]<self.button.centery+rad):
            self.image=self.image_on
            if(self.sound_chek==False):
                self.sound_chek=True
                self.sound.play()
            if onMouse==True:
                self.image=self.image_off
                self.clicksound.play()
                self.StartGame()
        else:
            self.image=self.image_off
            self.sound_chek = False

