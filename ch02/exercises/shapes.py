import pygame


pygame.init()
screen = pygame.display.set_mode()
dimensions = screen.get_size() #[width, and height]
starting_point = (dimensions[0] // 2, dimensions[1] //2 )
# draw library
# where to draw it
# color: "red", [r, g, b] =>[0-255, 0-255, 0-255]
#starting point: [x,y]
#radius: 50
radius =200
for_ in range(3)
pygame.draw.circle(screen, "red", starting_point, radius)
starting_point[1] = starting_point[1] - radius
radius = radius // 2
starting_point[1] = starting_point[1]

pygame.display.flip()
pygame. time. wait (2000)
pygame.event.pump()










