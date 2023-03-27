import pygame
import random
import math
while 1:
    # PART A
    pygame.init()

    screen_width=500
    screen_height=500
    screen = pygame.display.set_mode([screen_width, screen_height])
    screen.fill("black")

    pygame.draw.circle(screen, (0, 0, 0), (250,250), 250, width=3)
    pygame.draw.line(screen, "white", (500,-250), (500,250), width=3)
    pygame.draw.line(screen, "white", (0,250), (500,250), width=3)
    pygame.display.flip()

    #part B

    for darts in range(10):
        dart1x = random.randrange(0,500)
        dart1y = random.randrange(0,500)
        dart2x = random.randrange(0,500)
        dart2y = random.randrange(0,500)
        distance_from_center1 = math.hypot(dart1x-250, dart1y-250)
        distance_from_center2 = math.hypot(dart2x-250, dart2y-250)
        is_in_circle1 = (distance_from_center1 <= 250)
        is_in_circle2 = (distance_from_center2 <= 250)
        if  is_in_circle1 < 500:
            pygame.draw.circle(screen, "blue", [dart1x,dart1y], 10)
        else:
            pygame.draw.circle(screen, "green", [dart1x,dart1y], 10) 
            print("wrong", distance_from_center1)

        if  is_in_circle2 < 500:
            pygame.draw.circle(screen, "blue", [dart2x,dart2y], 10)
        else:
            pygame.draw.circle(screen, "green", [dart2x,dart2y], 10) 
            print("wrong", distance_from_center2)
    pygame.display.flip()
    pygame.time.wait(5000)