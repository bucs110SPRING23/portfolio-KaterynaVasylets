import pygame

# Part A
def threenp1(n):
    count = 0
    while n > 1.0:
        count = count + 1
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3*n+1)
    return count
        

def threenp1range(upper_limit):
    threenp1_dict = {}
    for i in range(2, upper_limit + 1):
        count = threenp1(i)
        threenp1_dict[i] = count
    return threenp1_dict

def graph_coordinates(threenplus1_iters_dict):

    pygame.init()
    screen = pygame.display.set_mode((1100, 700))
    
    # while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return
    
    pygame.draw.lines(screen, (0, 0, 255), False, list(threenplus1_iters_dict.items()))
    screen.blit(screen, (0,0))

    width, height = screen.get_size()
    new_screen = pygame.transform.scale(screen, (width * 5, height * 5))
    screen.blit(new_screen, (0,0))

    new_screen = pygame.transform.flip(screen, False, True)
    screen.blit(new_screen, (0,0))
    

    max_count = max(threenplus1_iters_dict)
    max_msg = f"Max count so far is: {max_count}"
    font = pygame.font.Font(None, 48)
    max_text = font.render(max_msg, True, (0, 0, 255))
    
    screen.blit(max_text, (400, 20))
    pygame.display.flip()

    pygame.time.wait(3000)



def main():
    print(threenp1range(20))
    graph_coordinates(threenp1range(20))

main()
