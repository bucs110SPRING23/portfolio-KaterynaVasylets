#Part A 

import pygame 
import math
import random

pygame.init()
sides = 360
s_length = 250
xpos = 250
ypos = 250
points = [] 

while 1:
    window = pygame.display.set_mode(size = (500, 500))
    pygame.event.get()
    screensize = pygame.display.get_window_size()

    for i in range(sides):
        angle = 360/sides
        radians = math.radians(angle * i)
        x = int(xpos + s_length * math.cos(radians))
        y = int(ypos + s_length * math.sin(radians))
        points.append([x,y])

    window.fill("White")
    pygame.display.flip()
    pygame.draw.polygon(window, "Red", points)
    pygame.display.flip()
    pygame.draw.line(window,"Black",[250,500], [250,0])
    pygame.display.flip()
    pygame.draw.line(window,"Black", [0,250], [500,250])
    pygame.display.flip()
    pygame.time.wait(2000)

    for x in range(10):
        a = random.randrange(0,501)
        b = random.randrange(0,501)
        distance_from_center = math.hypot(a-250,b-250)
        is_in_circle = distance_from_center <= 250
        if is_in_circle == True:
            pygame.draw.circle(window,"Green", [a,b],10)
            pygame.display.flip()
            pygame.time.wait(1000)
        else:
            pygame.draw.circle(window,"Blue", [a,b], 10)
            pygame.display.flip()
            pygame.time.wait(1000)
    break