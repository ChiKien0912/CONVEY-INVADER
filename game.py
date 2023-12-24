
#1 Import thư viện
import pygame, sys, random
import player as pl
import finish
pygame.init()
from pygame import mixer
sound1=pygame.mixer.Sound(r'sound/CHRIS.mp3')
#Các biến điểm
score =50
hscore=50
result=[]
obstacle_rect_list = []
#Hàm vẽ sàn
def draw_floor():
    screen.blit(pl.bg,(0,0))
    screen.blit(pl.floor,(pl.floor_x_pos,365))
    screen.blit(pl.floor,(pl.floor_x_pos+870,365))

# Hàm hiển thị điểm ra ngoài
def score_display():   
    if score==300 and star_game==False and game_active==False:
        score_state1 = game_font.render('WANNA TRY!',True,(0,0,128) )
        score_state1_rect=score_state1.get_rect(center = (400,300.5))
        screen.blit(score_state1,score_state1_rect)
    else:
        score_surface = game_font.render(f'Score:{int(score)}',True,(0,0,128) )
        score_rect=score_surface.get_rect(center = (400,170))
        screen.blit(score_surface,score_rect)
        hscore_txt=game_font.render(f'High Score: {int(hscore)}', True ,(128,0,0)  )
        screen.blit(hscore_txt,(280,180))
# Hàm hiển thị điểm cuối cùng:
def score_over():
    hscore_txt=game_font.render(f'High Score: {int(hscore)}', True ,(128,0,0)  )
    screen.blit(hscore_txt,(280,180)) 
#Hàm lọc và di chuyển của creep
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:

            if obstacle_rect.bottom ==200:
                obstacle_rect.x -=1.8
                screen.blit(pl.fly_surf,obstacle_rect)
            if obstacle_rect.bottom ==350:
                obstacle_rect.x -=2.2
                screen.blit(pl.obstacle1_surface,obstacle_rect)
            if obstacle_rect.bottom ==250:
                obstacle_rect.x -=2.3
                screen.blit(pl.obstacle2_surface,obstacle_rect)
            if obstacle_rect.bottom ==440:
                obstacle_rect.x -=2.8
                screen.blit(pl.obstacle3_surface,obstacle_rect)
            if obstacle_rect.bottom ==130:
                obstacle_rect.x +=1.9
                screen.blit(pl.bird_surf,obstacle_rect)
            if obstacle_rect.bottom ==210:
                obstacle_rect.x +=1.14
                screen.blit(pl.obstacle4_surface,obstacle_rect)
            if obstacle_rect.bottom ==315:
                obstacle_rect.x -=2.11
                screen.blit(pl.obstacle5_surface,obstacle_rect)
            if obstacle_rect.bottom ==300:
                obstacle_rect.x +=2.63
                screen.blit(pl.obstacle6_surface,obstacle_rect)
            if obstacle_rect.bottom ==330:
                obstacle_rect.x -=2.74
                screen.blit(pl.obstacle7_surface,obstacle_rect)
            if obstacle_rect.bottom ==430:
                obstacle_rect.x +=2.56
                screen.blit(pl.obstacle8_surface,obstacle_rect)
            if obstacle_rect.bottom ==220:
                obstacle_rect.x -=5
                screen.blit(pl.obstacle9_surface,obstacle_rect)
            if obstacle_rect.bottom ==420:
                obstacle_rect.x -=3
                screen.blit(pl.obstacle10_surface,obstacle_rect)
            if obstacle_rect.bottom ==280:
                obstacle_rect.x -=7
                screen.blit(pl.obstacle11_surface,obstacle_rect)
            if obstacle_rect.bottom ==410:
                obstacle_rect.x -=2.4
                screen.blit(pl.obstacle12_surface,obstacle_rect)
            if obstacle_rect.bottom ==455:
                obstacle_rect.x -3
                screen.blit(pl.obstacle13_surface,obstacle_rect)
            if obstacle_rect.bottom ==441:
                obstacle_rect.x +=3.5
                screen.blit(pl.obstacle14_surface,obstacle_rect)
            if obstacle_rect.bottom ==285:
                obstacle_rect.x -=4.1
                screen.blit(pl.obstacle15_surface,obstacle_rect)
            if obstacle_rect.bottom ==310:
                obstacle_rect.x +=3.56
                screen.blit(pl.obstacle16_surface,obstacle_rect)
            if obstacle_rect.bottom ==340:
                obstacle_rect.x -=3.3
                screen.blit(pl.obstacle17_surface,obstacle_rect)
            if obstacle_rect.bottom ==430:
                obstacle_rect.x +=2.69
                screen.blit(pl.obstacle18_surface,obstacle_rect)
            if obstacle_rect.bottom ==373:
                obstacle_rect.x -=2.25
                screen.blit(pl.obstacle19_surface,obstacle_rect)
            if obstacle_rect.bottom ==410:
                obstacle_rect.x -=3.5
                screen.blit(pl.obstacle20_surface,obstacle_rect)
            if (obstacle_rect.bottom>70) and obstacle_rect.bottom <=100 :
                obstacle_rect.x +=2
                obstacle_rect.y -=2
                screen.blit(pl.stock_surface,obstacle_rect)
            if obstacle_rect.bottom ==70:
                obstacle_rect.x +=2
                screen.blit(pl.stock_surface,obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x >-150]
        return obstacle_list
    else: return []


pygame.init()
screen = pygame.display.set_mode((800,495))
pygame.display.set_caption('Univermix')
clock = pygame.time.Clock()
# Tải font
font = pygame.font.Font(None, 36)
game_font = pygame.font.Font('04B_19.ttf',50)
def mainmenu():
    import maingame

#background sound
if random.randint(0,2):
    mixer.music.load('sound/Jingle Bells.mp3')
    mixer.music.play(-1)
else:
    mixer.music.load('sound/CHRIS.mp3')
    mixer.music.play(-1)




# Tạo timer cho các chướng ngại vật
make_obstacle= pygame.USEREVENT + 1
pygame.time.set_timer(make_obstacle,2000)

background_timer = pygame.USEREVENT + 2
pygame.time.set_timer(background_timer,1000)

flytimer = pygame.USEREVENT + 3
pygame.time.set_timer(flytimer,100)
game_active = True
star_game=False



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and game_active==True:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                pl.player_movement_x=0 
                pl.player_movement_y = 0
                pl.player_movement_y = -8

            if event.key== pygame.K_LEFT:
                pl.player_movement_y= 0
                pl.player_movement_x=0
                pl.player_movement_x =-8
            if event.key== pygame.K_RIGHT:
                pl.player_movement_y= 0
                pl.player_movement_x = 0
                pl.player_movement_x = 8
            if event.key== pygame.K_DOWN:
                pl.player_movement_y= 5
                pl.player_movement_x=0

        if event.type == make_obstacle and game_active:
            obstacle_rect_list=finish.make_creep()

        if event.type == flytimer:
            finish.flappy()

        # Vẽ dải băng 
        if event.type ==background_timer and game_active:
            pl.stock_rect_list.append(pl.stock_surface.get_rect(bottomright = (100,100)))
            
    while game_active==False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    game_active=True
                if event.key==pygame.K_ESCAPE:                
                    mixer.music.stop()
                    mainmenu()
        screen.blit(pl.bg1,(0,0))
        score_over()
        pygame.display.update()



    while star_game==False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    star_game=True
                if event.key==pygame.K_ESCAPE:                
                    mixer.music.stop()
                    mainmenu()
        screen.blit(pl.bg2,(0,0))
        pygame.display.update() 

                    
  
    pl.floor_x_pos -=2
    draw_floor()
    if pl.floor_x_pos <-870: pl.floor_x_pos=0
        
        #Player phạm vi di chuyển và hành động:
    pl.player_rect.centerx += pl.player_movement_x
    pl.player_movement_y += pl.gravity
    pl.player_rect.centery += pl.player_movement_y
    if pl.player_rect.centerx>=800:pl.player_rect.centerx = 800
    if pl.player_rect.centerx<=0:pl.player_rect.centerx=0
    if pl.player_rect.centery>=410:pl.player_rect.centery=410
    if pl.player_movement_x<0:screen.blit(pl.player_rect_list_left[pl.player_index ],pl.player_rect)
    if pl.player_movement_x>0:screen.blit(pl.player_rect_list[pl.player_index ],pl.player_rect)
    if pl.player_movement_y <0 :screen.blit(pl.player_rect_list_up[pl.player_index ],pl.player_rect)
    if pl.player_movement_x==0 and pl.player_movement_y>0:screen.blit(pl.player_rect_list_stand[pl.player_index ],pl.player_rect)
    if pl.player_rect.centery <=10:
        pl.player_rect.centery=10
        pl.player_rect.centery +=pl.player_movement_y



    obstacle_rect_list = obstacle_movement(obstacle_rect_list)
    pl.stock_rect_list =obstacle_movement(pl.stock_rect_list)


    #Tính điểm cho người chơi:
    #score_display(game_active)
    for achivement in result:
        if achivement ==1:score +=50
        if achivement ==2:score +=40
        if achivement ==3:score +=5
        if achivement ==4:score +=10
        if achivement ==5:score +=15
        if achivement ==6:score -=2
        else:score -=5
    if hscore<score: hscore=score
    score_display()
    if score <0:
        game_active=False
        score=50
    result.clear()


    obstacle_rect_list,result, attack = finish.check_collision(obstacle_rect_list)
    for attack_display in attack:
        if attack_display >=1:
            screen.blit(pl.player7_surface,pl.player_rect)
            Chem_sound =mixer.Sound('sound/chem.mp3')
            Chem_sound.play()
    attack.clear()

    pygame.display.update()
    clock.tick(60)


