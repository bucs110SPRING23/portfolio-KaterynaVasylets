import pygame
import random
import math
# PART A
pygame.init()

screen_width=500
screen_height=500
screen = pygame.display.set_mode([screen_width, screen_height])


pygame.draw.circle(screen, (0, 0, 0), (250,250), 250, width=3)
pygame.draw.line(screen, "black", (500,-250), (500,250), width=3)
pygame.draw.line(screen, "black", (0,250), (500,250), width=3)
pygame.display.flip()

#part B

for darts in range(10):
    x = random.randrange(0,500)
    y = random.randrange(0,500)
    distance_from_center = math.hypot(x-250, y-250)
    is_in_circle = distance_from_center 
    if  is_in_circle < 500:
        pygame.draw.circle(screen, "blue", [x,y], 10)
    else:
        pygame.draw.circle(screen, "green", [x,y], 10) 
        print("wrong", distance_from_center)
pygame.display.flip()
pygame.time.wait()