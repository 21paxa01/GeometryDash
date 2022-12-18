import pygame,events
import  hero as HERO
from road import Road, BackGround
import  traps
from start_menu import StartMenu
from  Buttons import Button
from portals import Portal
start_game=False
onMouse=False
onRoad=True
meters=13
meters_arr=[[18,18,2],[22,22,3],[26,26,4],[29,29,3],[33,33,4],[36,36,3],[39,39,2],[65,65,3],[68,68,2],[72,72,3],[75,75,2],[85,85,3],[93,93,3],[103,103,2],[107,117,3],[120,120,2],[124,124,3],[128,128,4],[131,131,3],[134,134,2],[138,138,3],[157,157,3],[169,169,3],[182,213,2],[243,243,2],[244,244,3],[245,245,2],[257,257,2],[258,258,3],[259,259,2],[264,271,2],[283,283,3],[304,304,2],[311,311,2],[371,371,2],[378,378,2],[470,500,2],[511,511,3],[521,521,3],[541,552,2]]
up_meters_arr=[[65,65,3],[85,85,3],[93,93,3],[152,152,3],[163,163,3],[175,175,3],[182,213,2],[236,236,2],[237,237,3],[238,238,2],[250,250,2],[251,251,3],[252,252,2],[264,271,2],[304,304,3],[307,307,2],[311,311,3],[314,314,2],[318,318,3],[322,322,4],[325,325,3],[328,328,2],[346,346,2],[350,350,3],[354,354,4],[357,357,3],[361,361,4],[371,371,3],[378,378,3],[407,407,2],[411,411,3],[415,415,4],[418,418,3],[422,422,4],[470,500,2],[516,516,3],[526,526,3],[532,540,2]]
spikes_meters_arr=[[18,39,2],[44,44,2],[49,50,2],[54,56,2],[66,76,2],[104,107,2],[110,111,4],[114,115,4],[118,146,2],[157,157,4],[169,169,4],[182,186,3],[196,200,3],[214,232,2],[242,242,2],[243,243,3],[244,244,4],[245,245,3],[246,246,2],[256,256,2],[257,257,3],[258,258,4],[259,259,3],[260,260,2],[304,304,3],[371,371,3],[378,378,3],[440,443,2],[448,451,2],[456,459,2],[477,478,3],[483,484,3],[489,491,3],[497,500,3],[508,510,2],[511,511,4],[518,520,2],[521,521,4],[532,540,2]]
up_spikes_meters_arr=[[65,65,4],[85,85,4],[93,93,4],[152,152,4],[163,163,4],[175,175,4],[189,193,3],[203,207,3],[214,232,2],[235,235,2],[236,236,3],[237,237,4],[238,238,3],[239,239,2],[249,249,2],[250,250,3],[251,251,4],[252,252,3],[253,253,2],[289,290,2],[294,295,2],[304,328,2],[338,340,2],[346,361,2],[390,391,2],[396,397,2],[401,402,2],[407,424,2],[444,447,2],[452,455,2],[460,469,2],[474,475,3],[480,481,3],[486,487,3],[493,495,3],[501,507,2],[513,515,2],[516,516,4],[523,525,2],[526,526,4],[527,531,2],[541,552,2]]
def run():
    """
    Функция с игровым циклом,которая запускается
    после нажатия на кнопку "старт" в стартовом меню,
    а также после проигрыша игрока.
    :return:None
    """
    pygame.init()
    pygame.mixer.music.unload()
    pygame.mixer.music.load("sounds/StayInsideMe.mp3")
    pygame.mixer.music.play()
    screen=pygame.display.set_mode((1200,800))
    pygame.display.set_caption("game")
    bg_color=(255,255,255)
    hero=HERO.Hero(screen)
    ship_portal=Portal(screen,0)
    HERO.meters=13
    meters_i=0
    up_meters_i=0
    spikes_i=0
    up_spikes_i=0
    road1_0,road2_0,road3_0,road4_0,road5_0,road6_0,road7_0,road8_0,road9_0,road10_0,road11_0,road12_0,road13_0 = Road(screen,750),Road(screen,750),Road(screen,750),Road(screen,750),Road(screen,750),Road(screen,750),Road(screen,750),Road(screen,750),Road(screen,750),Road(screen,750),Road(screen,750),Road(screen,750),Road(screen,750)
    road_arr_0=[road1_0,road2_0,road3_0,road4_0,road5_0,road6_0,road7_0,road8_0,road9_0,road10_0,road11_0,road12_0,road13_0]
    road1_1, road2_1, road3_1, road4_1, road5_1, road6_1, road7_1, road8_1, road9_1, road10_1, road11_1, road12_1, road13_1 = Road(screen,50),Road(screen,50),Road(screen,50),Road(screen,50),Road(screen,50),Road(screen,50),Road(screen,50),Road(screen,50),Road(screen,50),Road(screen,50),Road(screen,50),Road(screen,50),Road(screen,50)
    road_arr_1 = [road1_1, road2_1, road3_1, road4_1, road5_1, road6_1, road7_1, road8_1, road9_1, road10_1, road11_1,road12_1, road13_1]
    bg = BackGround(screen)
    spike1,spike2,spike3,spike4,spike5,spike6,spike7,spike8,spike9,spike10,spike11,spike12,spike13=traps.Spike(screen),traps.Spike(screen),traps.Spike(screen),traps.Spike(screen),traps.Spike(screen),traps.Spike(screen),traps.Spike(screen),traps.Spike(screen),traps.Spike(screen),traps.Spike(screen),traps.Spike(screen),traps.Spike(screen),traps.Spike(screen)
    spikes_arr=[spike1,spike2,spike3,spike4,spike5,spike6,spike7,spike8,spike9,spike10,spike11,spike12,spike13]
    up_spike1, up_spike2, up_spike3, up_spike4, up_spike5, up_spike6, up_spike7, up_spike8, up_spike9, up_spike10, up_spike11, up_spike12, up_spike13 = traps.Spike(screen), traps.Spike(screen), traps.Spike(screen), traps.Spike(screen), traps.Spike(screen), traps.Spike(screen), traps.Spike(screen), traps.Spike(screen), traps.Spike(screen), traps.Spike(screen), traps.Spike(screen), traps.Spike(screen), traps.Spike(screen)
    up_spikes_arr = [up_spike1, up_spike2, up_spike3, up_spike4, up_spike5, up_spike6, up_spike7, up_spike8, up_spike9, up_spike10, up_spike11, up_spike12,up_spike13]
    traps.restart = False
    HERO.restart=0
    for i in range(13):
        road_arr_0[i].road.centerx=100*i+50
        road_arr_1[i].road.centerx=100*i+50
        spikes_arr[i].spike.centerx=100*i+50
        up_spikes_arr[i].spike.centerx=100*i+50
        up_spikes_arr[i].up=True
        up_spikes_arr[i].image=pygame.transform.rotate(up_spikes_arr[i].image,180)

    while HERO.restart!=-1 and HERO.finish==False:
        events.event(hero)
        HERO.restart=hero.ChekRoad(meters_arr,up_meters_arr)
        if(HERO.restart==0):
            HERO.onRoad=False
        elif HERO.restart==1:
            HERO.onRoad=True
        if(HERO.restart==-2):
            HERO.underRoad=True
        elif HERO.restart==-3:
            HERO.underRoad=False
        elif HERO.restart==3:
            HERO.finish=True
        hero.Hero_pos()
        hero.Jump()
        screen.fill(bg_color)
        bg.BG_Draw()
        if HERO.meters>meters_arr[meters_i][1] and meters_i<len(meters_arr)-1:
            meters_i+=1
        if HERO.meters>up_meters_arr[up_meters_i][1] and up_meters_i<len(up_meters_arr)-1:
            up_meters_i+=1
        road_i=HERO.meters%13-2
        if(road_i==-1):
            road_i=12
        if HERO.meters>spikes_meters_arr[spikes_i][1] and spikes_i<len(spikes_meters_arr)-1:
            spikes_i+=1
        if HERO.meters>up_spikes_meters_arr[up_spikes_i][1] and up_spikes_i<len(up_spikes_meters_arr)-1:
            up_spikes_i+=1
        if(HERO.meters>=meters_arr[meters_i][0] and HERO.meters<=meters_arr[meters_i][1]):
            road_arr_0[road_i].road.centery=850-meters_arr[meters_i][2]*100
        if(HERO.meters>=up_meters_arr[up_meters_i][0] and HERO.meters<=up_meters_arr[up_meters_i][1]):
            road_arr_1[road_i].image_chek=up_meters_arr[up_meters_i][2]
        if(HERO.meters>=spikes_meters_arr[spikes_i][0] and HERO.meters<=spikes_meters_arr[spikes_i][1]):
            spikes_arr[road_i].spike.centery=850-spikes_meters_arr[spikes_i][2]*100
        if (HERO.meters >= up_spikes_meters_arr[up_spikes_i][0] and HERO.meters <= up_spikes_meters_arr[up_spikes_i][1]):
            up_spikes_arr[road_i].spike.centery = -50 + up_spikes_meters_arr[up_spikes_i][2] * 100
        for i in range(13):
            spikes_arr[i].Draw(hero)
            up_spikes_arr[i].Draw(hero)
            road_arr_0[i].Draw()
            road_arr_1[i].UP_Draw()
        ship_portal.Draw_left(hero,HERO.meters)
        hero.Draw()
        ship_portal.Draw_right(HERO.meters)
        pygame.display.flip()
        hero.Rotate()
    if(HERO.finish==False):
        run()
    start()
def start():
    """
    Функция, которая запускатся после старта игры. 
    Она создает стартовое меню для дальнейшего запуска игрового уровня.
    :return: None
    """
    HERO.finish=False
    pygame.init()
    pygame.mixer.music.load("sounds/menuLoop.mp3")
    pygame.mixer.music.play(-1)
    screen=pygame.display.set_mode((1200,800))
    pygame.display.set_caption("game")
    menu=StartMenu(screen)
    bg_color=(255,255,255)
    hero=HERO.Hero(screen)
    start_button=Button(screen)
    start_button.button.centerx,start_button.button.centery=600,450
    while start_button.startgame == False:
        events.event(hero)
        screen.fill(bg_color)
        menu.StartGame()
        start_button.Draw()
        start_button.ClickChek(150)
        pygame.display.flip()
    run()
start()