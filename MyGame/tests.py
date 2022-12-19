import unittest
import pygame
from Buttons import Button
from traps import Spike
import hero as HERO
import portals
meters_arr=[[18,18,2],[22,22,3],[26,26,4],[29,29,3],[33,33,4],[36,36,3],[39,39,2],[65,65,3],[68,68,2],[72,72,3],[75,75,2],[85,85,3],[93,93,3],[103,103,2],[107,117,3],[120,120,2],[124,124,3],[128,128,4],[131,131,3],[134,134,2],[138,138,3],[157,157,3],[169,169,3],[182,213,2],[243,243,2],[244,244,3],[245,245,2],[257,257,2],[258,258,3],[259,259,2],[264,271,2],[283,283,3],[304,304,2],[311,311,2],[371,371,2],[378,378,2],[470,500,2],[511,511,3],[521,521,3],[541,552,2]]
up_meters_arr=[[65,65,3],[85,85,3],[93,93,3],[152,152,3],[163,163,3],[175,175,3],[182,213,2],[236,236,2],[237,237,3],[238,238,2],[250,250,2],[251,251,3],[252,252,2],[264,271,2],[304,304,3],[307,307,2],[311,311,3],[314,314,2],[318,318,3],[322,322,4],[325,325,3],[328,328,2],[346,346,2],[350,350,3],[354,354,4],[357,357,3],[361,361,4],[371,371,3],[378,378,3],[407,407,2],[411,411,3],[415,415,4],[418,418,3],[422,422,4],[470,500,2],[516,516,3],[526,526,3],[532,540,2]]
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
    def test_finish_true(self):
        pygame.init()
        screen=pygame.display.set_mode((1200,800))
        hero=HERO.Hero(screen)
        HERO.meters=553
        self.assertTrue(hero.ChekRoad(meters_arr,up_meters_arr)==3)
    def test_finish_false(self):
        pygame.init()
        screen=pygame.display.set_mode((1200,800))
        hero=HERO.Hero(screen)
        HERO.meters=551
        self.assertFalse(hero.ChekRoad(meters_arr,up_meters_arr)==3)

if __name__ == '__main__':
    unittest.main()