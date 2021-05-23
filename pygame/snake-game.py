import pygame
import time
import random

from pygame import display

clock = pygame.time.Clock()

screen_width=400
screen_height=400
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.init()
pygame.display.set_caption("My first game with pygame")

def waitKeys(keyArr):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key in keyArr:
                    return event.key


def message(msg, posx, posy, r, g, b):
    screen.blit(font.render(msg,True,(r,g,b)), [posx,posy])

def validatePosition(posx, posy, snake):
    return ((posx in range (0,screen_width)) and (posy in range (0,screen_height))) and not ([posx,posy] in snake)

def game():
    
    snake = []
    snake_length = 1
    posx=screen_width/2
    posy=screen_height/2
    foodx = round(random.randrange(0, screen_width-10)/10.0)*10.0
    foody = round(random.randrange(0, screen_height-10)/10.0)*10.0
    
    

    GAMEOVER=False
    var_posx=0
    var_posy=0
    prev = 'X'
    while not GAMEOVER:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if prev != 'R':
                        var_posx=-10
                        var_posy=0
                        prev= 'L'
                if event.key == pygame.K_RIGHT:
                    if prev!= 'L':
                        var_posx=10
                        var_posy=0
                        prev = 'R'
                if event.key == pygame.K_UP:
                    if prev != 'D':
                        var_posy=-10
                        var_posx=0
                        prev = 'U'
                if event.key == pygame.K_DOWN:
                    if prev!= 'U':
                        var_posy=10
                        var_posx=0
                        prev = 'D'

        posx+=var_posx
        posy+=var_posy   

        if(validatePosition(posx,posy,snake)):
            print("{} , head = {}".format(snake,[posx,posy]))
            
            if(posx == foodx and posy == foody):
                snake_length+=1
                snake.append([posx,posy])
                foodx = round(random.randrange(0, screen_width-10)/10.0)*10.0
                foody = round(random.randrange(0, screen_height-10)/10.0)*10.0
            #else:
            if snake.__len__()>1:
                for i in range (0,snake.__len__()-1):
                    snake[i] = snake[i+1]
                snake[snake.__len__()-1] = [posx-var_posx, posy-var_posy]
            else:
                if snake.__len__()==1: snake[snake.__len__()-1] = [posx-var_posx, posy-var_posy]

            screen.fill((255,255,255))

            for x in snake:
                pygame.draw.rect(screen,(255,0,0),[x[0],x[1],10,10])
            pygame.draw.rect(screen,(255,0,0),[posx,posy,10,10])
            pygame.draw.rect(screen,(0,0,255),[foodx,foody,10,10])
            
        else:
            GAMEOVER=True
        
        pygame.display.update()

        
        clock.tick(17)
    
    return snake_length-1

while True:
    
    points=game()
    
    screen.fill((255,255,255))
    font = pygame.font.SysFont(None,50)
    message("GAME OVER",100,160,0,0,0)
    pygame.display.update()
    time.sleep(1)

    font = pygame.font.SysFont(None,20)
    message("Points: {}".format(points),175,210,0,0,0)
    message("Play Again?",165,240,0,0,0)
    message("Yes - ENTER",160,260,0,0,0)
    message("No - ESCAPE",160,280,0,0,0)
    pygame.display.update()

    if waitKeys([pygame.K_ESCAPE,pygame.K_RETURN]) == pygame.K_ESCAPE:
        break
