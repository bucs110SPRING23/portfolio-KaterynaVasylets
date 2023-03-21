import random
import pygame
import math

# Initialize pygame and create game window
pygame.init()
window = pygame.display.set_mode((1000, 1000))

# Set up game screen properties
screen_size = window.get_size()
center_of_screen = (screen_size[0]/2, screen_size[1]/2)
half_of_width = screen_size[0]/2
half_of_height = screen_size[1]/2
width = screen_size[0]
height = screen_size[1]

# Set up game variables
amount_of_throws_hits_in_circle_dart_1 = 1
amount_of_throws_hits_in_circle_dart_2 = 1
turns = 1
result = ""

# Set up game screen elements
window.fill((0, 0, 300)) 
hitboxes = {
    "red": pygame.Rect(screen_size[0]/6.4, screen_size[1]/2.85, 350, 350),
    "green":pygame.Rect(screen_size[0]/1.67, screen_size[1]/2.85, 350, 350)
}
main_colors = {
    "red": (100, 0, 0),
    "green": (0, 100, 0)
}
highlight_colors = {
    "red": (200, 0, 0),
    "green": (0, 200, 0)
}
font = pygame.font.Font(None, 60)
text1 = font.render("Guess Who Wins The Dart Game!", True, (0, 0, 0)) 
text2 = font.render("Please Select Your Player", True, (0, 0, 0))
text3 = font.render("Player 1", True, (0, 0, 0))
text4 = font.render("Player 2", True, (0, 0, 0))

# Start game loop
done = False
while not done:
    window.fill((0, 0, 255))
    pygame.draw.rect(window, main_colors["green"], hitboxes["green"])
    pygame.draw.rect(window, main_colors["red"], hitboxes["red"])
    window.blit(text1, (80, half_of_height/3))
    window.blit(text2, (200, half_of_height/2))
    window.blit(text3, (screen_size[0]/4.5, screen_size[1]/2.1))
    window.blit(text4, (screen_size[0]/1.48, screen_size[1]/2.1))

    # Check for player selection
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            turns = turns - 1
            if hitboxes["red"].collidepoint(event.pos):
                pygame.draw.rect(window, highlight_colors["red"], hitboxes["red"])
                result = "red"
            done = True
            if hitboxes["green"].collidepoint(event.pos):
                pygame.draw.rect(window, highlight_colors["green"], hitboxes["green"])
                result = "green"
            done = True
    pygame.display.update()

# Clear game screen and draw dart board
window.fill((0, 0, 255))
pygame.draw.circle(window, (0, 0, 0), center_of_screen, half_of_height) 
pygame.draw.circle(window, (255, 192, 203), center_of_screen, half_of_height - 5)
pygame.draw.line(window, (0, 0, 0), (half_of_width,0),(half_of_width, height), 3)
pygame.draw.line

