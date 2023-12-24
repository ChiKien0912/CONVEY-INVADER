import pygame, sys
pygame.init()

gamemenu=pygame.image.load(r'assets/menu.png')
sound4=pygame.mixer.Sound(r'sound/CHRIS.mp3')
icon=pygame.image.load(r'assets/stock.png')
pygame.display.set_icon(icon)
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('CHRISTMAS MAIN GAME')
screen=pygame.display.set_mode((1200,600))
menu1=screen.blit(gamemenu,(0,0))
 
#setting font settings
font = pygame.font.Font(r'04B_19.TTF', 30)
 
"""
A function that can be used to write text on our screen and buttons
"""
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
def sound():
    pygame.mixer.Sound.play(sound4)
 
# A variable to check for the status later
click=False
 
# Main container function that holds the buttons and game functions
def main_menu():
    while True:
        sound()
        mx, my = pygame.mouse.get_pos()
        #creating buttons
        button_1 = pygame.Rect(410, 300, 370, 70)
        button_2 = pygame.Rect(410, 390, 370, 70)
        button_3 = pygame.Rect(410, 480, 370, 70)
        global click
        #defining functions when a certain button is pressed
        if button_1.collidepoint((mx, my)):
            if click:
                pygame.mixer.Sound.stop(sound4)
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.mixer.Sound.stop(sound4)
                game1()
        if button_3.collidepoint((mx, my)):
            if click:
                pygame.mixer.Sound.stop(sound4)
                pygame.quit()
                sys.exit()


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
def game1():
    import game1              
def game():
    import game
main_menu()