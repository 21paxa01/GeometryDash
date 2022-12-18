import unittest
import pygame
from Buttons import Button
from traps import Spike
import hero as HERO
import portals
class GameTest(unittest.TestCase):
    def test_true_start(self):
        pygame.init()
        screen=pygame.display.set_mode((1200,800))
        button=Button(screen)
        button.StartGame()
        self.assertTrue(button.startgame==True)
    def test_false_start(self):
        pygame.init()
        screen=pygame.display.set_mode((1200,800))
        button=Button(screen)
        button.StartGame()
        self.assertFalse(button.startgame==False)
    def test_on_spike(self):
        pygame.init()
        screen=pygame.display.set_mode((1200,800))
        spike=Spike(screen)
        spike.spike.centery,spike.spike.centerx=0,0
        hero=HERO.Hero(screen)
        hero.hero.centery,hero.hero.centerx=0,0
        HERO.restart=0
        spike.Draw(hero)
        self.assertTrue(HERO.restart==-1)
    def test_out_spike(self):
        pygame.init()
        screen=pygame.display.set_mode((1200,800))
        spike=Spike(screen)
        spike.spike.centery,spike.spike.centerx=-100,-100
        hero=HERO.Hero(screen)
        hero.hero.centery,hero.hero.centerx=100,100
        HERO.restart=0
        spike.Draw(hero)
        self.assertFalse(HERO.restart==-1)
    def test_ship_portal_true(self):
        pygame.init()
        screen=pygame.display.set_mode((1200,800))
        portal=portals.Portal(screen,0)
        portal.meters_i=0
        hero=HERO.Hero(screen)
        HERO.meters=150
        hero.hero.centery,hero.hero.centerx=1300,1300
        hero.hero_sprite="deafolt"
        portal.Draw_left(hero,HERO.meters)
        self.assertTrue(hero.hero_sprite=="ship")
    def test_ship_portal_false(self):
        pygame.init()
        screen=pygame.display.set_mode((1200,800))
        portal=portals.Portal(screen,0)
        portal.meters_i=0
        hero=HERO.Hero(screen)
        HERO.meters=150
        hero.hero.centery,hero.hero.centerx=1300,1300
        hero.hero_sprite="deafolt"
        portal.Draw_left(hero,HERO.meters)
        self.assertFalse(hero.hero_sprite!="ship")
    def test_deafolt_portal_true(self):
        pygame.init()
        screen=pygame.display.set_mode((1200,800))
        portal=portals.Portal(screen,1)
        portal.meters_i=1
        hero=HERO.Hero(screen)
        HERO.meters=283
        hero.hero.centery,hero.hero.centerx=1300,1300
        hero.hero_sprite="ship"
        portal.Draw_left(hero,HERO.meters)
        self.assertTrue(hero.hero_sprite=="deafolt")
    def test_deafolt_portal_false(self):
        pygame.init()
        screen=pygame.display.set_mode((1200,800))
        portal=portals.Portal(screen,1)
        portal.meters_i=1
        hero=HERO.Hero(screen)
        HERO.meters=283
        hero.hero.centery,hero.hero.centerx=1300,1300
        hero.hero_sprite="ship"
        portal.Draw_left(hero,HERO.meters)
        self.assertFalse(hero.hero_sprite!="deafolt")
    def test_flip_portal_true(self):
        pygame.init()
        screen=pygame.display.set_mode((1200,800))
        portal=portals.Portal(screen,2)
        portal.meters_i=2
        hero=HERO.Hero(screen)
        HERO.meters=295
        hero.hero.centery,hero.hero.centerx=1300,1300
        hero.hero_sprite="deafolt"
        portal.Draw_left(hero,HERO.meters)
        self.assertTrue(hero.hero_sprite=="flip")
    def test_flip_portal_false(self):
        pygame.init()
        screen=pygame.display.set_mode((1200,800))
        portal=portals.Portal(screen,2)
        portal.meters_i=2
        hero=HERO.Hero(screen)
        HERO.meters=295
        hero.hero.centery,hero.hero.centerx=1300,1300
        hero.hero_sprite="deafolt"
        portal.Draw_left(hero,HERO.meters)
        self.assertFalse(hero.hero_sprite!="flip")
    def test_ball_portal_true(self):
        pygame.init()
        screen=pygame.display.set_mode((1200,800))
        portal=portals.Portal(screen,3)
        portal.meters_i=3
        hero=HERO.Hero(screen)
        HERO.meters=440
        hero.hero.centery,hero.hero.centerx=1300,1300
        hero.hero_sprite="flip"
        portal.Draw_left(hero,HERO.meters)
        self.assertTrue(hero.hero_sprite=="ball")
    def test_ball_portal_false(self):
        pygame.init()
        screen=pygame.display.set_mode((1200,800))
        portal=portals.Portal(screen,3)
        portal.meters_i=3
        hero=HERO.Hero(screen)
        HERO.meters=440
        hero.hero.centery,hero.hero.centerx=1300,1300
        hero.hero_sprite="flip"
        portal.Draw_left(hero,HERO.meters)
        self.assertFalse(hero.hero_sprite!="ball")
if __name__ == '__main__':
    unittest.main()