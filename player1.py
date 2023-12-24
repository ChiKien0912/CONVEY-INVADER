import pygame

# import hình ảnh
bg = pygame.image.load('assets1/background.png')
bg1 = pygame.image.load('assets1/background1.png')
bg2 = pygame.image.load('assets1/background2.png')
among = pygame.image.load('assets1/among.png')
back_star = pygame.image.load('assets1/back1.png')

player_index= 0
player2_surface = pygame.image.load('player/a2.png')
player22_surface  = pygame.image.load('player/a22.png')
player3_surface  = pygame.image.load('player/a3.png')
player33_surface  = pygame.image.load('player/a33.png')
player4_surface  = pygame.image.load('player/a4.png')
player44_surface  = pygame.image.load('player/a44.png')
player5_surface  = pygame.image.load('player/a5.png')
player55_surface  = pygame.image.load('player/a55.png')
player6_surface  = pygame.image.load('player/a6.png')
player66_surface  = pygame.image.load('player/a66.png')
player7_surface  = pygame.image.load('player/a7.png')
player_rect_list = [player2_surface,player3_surface,player4_surface,player5_surface,player6_surface]
player_rect_list_left=[player22_surface,player33_surface,player44_surface,player55_surface,player66_surface]

playerb2_surface  = pygame.image.load('player/b2.png')
playerb3_surface  = pygame.image.load('player/b3.png')
playerb4_surface  = pygame.image.load('player/b4.png')
player_rect_list_up = [playerb2_surface,playerb2_surface,playerb3_surface,playerb3_surface,playerb4_surface]
player_rect_list_stand = [player2_surface,player3_surface,player4_surface,player3_surface,player2_surface]


#Import bird 1
bird_index= 0

bird_down = pygame.transform.scale2x(pygame.image.load('Fly/yellowbird-downflap.png'))
bird_up = pygame.transform.scale2x(pygame.image.load('Fly/yellowbird-upflap.png'))
bird_mid = pygame.transform.scale2x(pygame.image.load('Fly/yellowbird-midflap.png'))
bird_list=[bird_down,bird_mid,bird_up]
bird_surf=bird_list[bird_index]

#Import bird 2
fly_frame_index = 0
fly_frame1 = pygame.image.load('Fly/Fly1.png')
fly_frame2 = pygame.image.load('Fly/Fly2.png')
fly_frames =[fly_frame1,fly_frame2]
fly_surf = fly_frames[fly_frame_index]

#Tạo hiệu ứng factory
stock_surface = pygame.image.load('assets1/stock.png')
stock_rect_list = []
#Import pl.floor
floor = pygame.image.load('assets1/runway.png')
floor_x_pos = 0


#Tạo các chướng ngại vật
obstacle1_surface = pygame.image.load('obstacle1/obstacle1.png')
obstacle2_surface = pygame.image.load('obstacle1/obstacle2.png')
obstacle3_surface = pygame.image.load('obstacle1/obstacle3.png')
obstacle4_surface = pygame.image.load('obstacle1/obstacle4.png')
obstacle5_surface = pygame.image.load('obstacle1/obstacle5.png')
obstacle6_surface = pygame.image.load('obstacle1/obstacle6.png')
obstacle7_surface = pygame.image.load('obstacle1/obstacle7.png')
obstacle8_surface = pygame.image.load('obstacle1/obstacle8.png')
obstacle9_surface = pygame.image.load('obstacle1/obstacle9.png')
obstacle10_surface = pygame.image.load('obstacle1/obstacle10.png')
obstacle11_surface = pygame.image.load('obstacle1/obstacle11.png')
obstacle12_surface = pygame.image.load('obstacle1/obstacle12.png')
obstacle13_surface = pygame.image.load('obstacle1/obstacle13.png')
obstacle14_surface = pygame.image.load('obstacle1/obstacle14.png')
obstacle15_surface = pygame.image.load('obstacle1/obstacle15.png')
obstacle16_surface = pygame.image.load('obstacle1/obstacle16.png')
obstacle17_surface = pygame.image.load('obstacle1/obstacle17.png')
obstacle18_surface = pygame.image.load('obstacle1/obstacle18.png')
obstacle19_surface = pygame.image.load('obstacle1/obstacle19.png')
obstacle20_surface = pygame.image.load('obstacle1/obstacle20.png')
obstacle_list1 =[obstacle16_surface,obstacle17_surface,obstacle18_surface,obstacle19_surface,obstacle20_surface]
obstacle_list2 = [obstacle15_surface,obstacle14_surface,obstacle13_surface,obstacle12_surface,obstacle11_surface]
obstacle_list3 =[obstacle6_surface,obstacle7_surface,obstacle8_surface,obstacle9_surface,obstacle10_surface]
obstacle_list4 = [obstacle1_surface,obstacle2_surface,obstacle3_surface,obstacle4_surface,obstacle5_surface]





player_rect= player2_surface.get_rect(center = (400,385))
gravity = 0.25
player_movement_y = 0
player_movement_x = 0