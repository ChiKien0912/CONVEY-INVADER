import pygame
pygame.init()
import player1 as pl
import random

obstacle_rect_list=[]
result=[]
score = 0
score = 0
high_score=0
attack=[]
game_active=[]



def make_creep():
    if random.randint(0,2):
        pl.obstacle1_surface_rect = pl.obstacle1_surface.get_rect(bottomright=(random.randint(900,1000),350))
        pl.obstacle2_surface_rect = pl.obstacle2_surface.get_rect(bottomright=(random.randint(900,1000),250))
        pl.obstacle3_surface_rect = pl.obstacle3_surface.get_rect(bottomright=(random.randint(900,1000),440))
        pl.obstacle4_surface_rect = pl.obstacle4_surface.get_rect(bottomright=(-5,210))
        pl.obstacle5_surface_rect = pl.obstacle5_surface.get_rect(bottomright=(random.randint(900,1000),315))
        pl.obstacle6_surface_rect = pl.obstacle6_surface.get_rect(bottomright=(-10,300))
        pl.obstacle7_surface_rect = pl.obstacle7_surface.get_rect(bottomright=(random.randint(900,1000),330))
        pl.obstacle8_surface_rect = pl.obstacle8_surface.get_rect(bottomright=(-15,430))
        pl.obstacle9_surface_rect = pl.obstacle9_surface.get_rect(bottomright=(random.randint(900,1000),220))
        pl.obstacle10_surface_rect = pl.obstacle10_surface.get_rect(bottomright=(random.randint(900,1000),420))
        ob_list_1 = [pl.obstacle4_surface_rect,pl.obstacle5_surface_rect,pl.obstacle6_surface_rect]
        ob_list_3 = [pl.obstacle7_surface_rect,pl.obstacle8_surface_rect,pl.obstacle9_surface_rect,pl.obstacle10_surface_rect]
        ob_list_2 = [pl.obstacle1_surface_rect,pl.obstacle2_surface_rect,pl.obstacle3_surface_rect]
        ob_list =[random.choice(ob_list_1),random.choice(ob_list_2),random.choice(ob_list_3)]
        obstacle_rect_list.append(random.choice(ob_list))
    else:
        pl.obstacle11_surface_rect = pl.obstacle11_surface.get_rect(bottomright=(random.randint(900,1000),280))
        pl.obstacle12_surface_rect = pl.obstacle12_surface.get_rect(bottomright=(random.randint(900,1000),410))
        pl.obstacle13_surface_rect = pl.obstacle13_surface.get_rect(bottomright=(random.randint(900,1000),455))
        pl.obstacle14_surface_rect = pl.obstacle14_surface.get_rect(bottomright=(-5,441))
        pl.obstacle15_surface_rect = pl.obstacle15_surface.get_rect(bottomright=(random.randint(900,1000),285))
        pl.obstacle16_surface_rect = pl.obstacle16_surface.get_rect(bottomright=(-10,310))
        pl.obstacle17_surface_rect = pl.obstacle17_surface.get_rect(bottomright=(random.randint(900,1000),340))
        pl.obstacle18_surface_rect = pl.obstacle18_surface.get_rect(bottomright=(-15,430))
        pl.obstacle19_surface_rect = pl.obstacle19_surface.get_rect(bottomright=(random.randint(900,1000),373))
        pl.obstacle20_surface_rect = pl.obstacle20_surface.get_rect(bottomright=(random.randint(900,1000),410))
        fly_frame1_rect = pl.fly_frame1.get_rect(bottomright=(random.randint(900,1100),200))
        bird_up_rect = pl.bird_up.get_rect(bottomright=(0,130))
        bird_list_rect = [fly_frame1_rect, bird_up_rect,pl.obstacle12_surface_rect,pl.obstacle13_surface_rect]
        obs_list_2 = [pl.obstacle14_surface_rect,pl.obstacle15_surface_rect,pl.obstacle16_surface_rect]
        obs_list_3 = [pl.obstacle17_surface_rect,pl.obstacle18_surface_rect,pl.obstacle19_surface_rect,pl.obstacle20_surface_rect]
        obs_list =[random.choice(bird_list_rect),random.choice(obs_list_2),random.choice(obs_list_3)]
        obstacle_rect_list.append(random.choice(obs_list))



    return obstacle_rect_list

def check_collision(obstacle_rect_list):
    if obstacle_rect_list:
        for obstacle in obstacle_rect_list:
            if pl.player_rect.colliderect(obstacle):
                attack.extend(range(10))
                if obstacle.bottom ==350 or obstacle.bottom == 250 or obstacle.bottom ==210:
                    obstacle.x -=1000
                    result.append(1)
                if obstacle.bottom ==315 or obstacle.bottom ==300 or obstacle.bottom == 430:
                    result.append(2)
                    obstacle.x -=1000
                if obstacle.bottom ==420 or obstacle.bottom ==410 or obstacle.bottom == 455:
                    obstacle.x -=1000
                    result.append(3)
                if obstacle.bottom ==441 or obstacle.bottom == 310 or obstacle.bottom == 340:
                    obstacle.x -=1000
                    result.append(4)
                if obstacle.bottom ==430 or obstacle.bottom == 410 or obstacle.bottom == 373:
                    obstacle.x -=1000
                    result.append(5)
                if obstacle.bottom ==200 or obstacle.bottom == 130:
                    result.append(6)
                else:
                    result.append(7)

        obstacle_rect_list = [obstacle for obstacle in obstacle_rect_list if obstacle.x >-150]
    return obstacle_rect_list, result, attack

def flappy():
    if pl.fly_frame_index == 0:pl.fly_frame_index =1
    else:pl.fly_frame_index = 0
    pl.fly_surf = pl.fly_frames[pl.fly_frame_index]
    if pl.bird_index <2:
        pl.bird_index +=1
    else: pl.bird_index = 0
    pl.bird_surf=pl.bird_list[pl.bird_index]
    if pl.player_index <=3:pl.player_index  +=1
    else:pl.player_index =0


def state_game(state):
    print("aaa")
    return True




