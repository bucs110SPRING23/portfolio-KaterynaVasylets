import random
import math
import turtle

import pygame
import math

#Part A
turtle1= turtle.Turtle()
turtle1.shape("turtle")

turtle2= turtle.Turtle()
turtle2.shape("turtle")

window=turtle.Screen()

turtle1.up()
turtle1.goto(-100,20)
turtle1.pendown()

turtle2.up()
turtle2.goto(-100,-20)
turtle2.pendown()



#Race 1
turtle1.color("red")
turtle2.color("blue")
ranMove=random.randint(1,100)
turtle1.forward(ranMove)
turtle2.forward(ranMove)
turtle1.up()
turtle2.up()
turtle1.goto(-100,20)
turtle2.goto(-100,-20)


#Race 2
turtle1.color("purple")
turtle2.color("green")
turtle1.pendown()
turtle2.pendown()
for i in range(1):
    turt1Dis=random.randrange(1,10)
    turt2Dis=random.randrange(1,10)
    turtle1.fd(turt1Dis)
    turtle2.fd(turt2Dis)
    turtle1.goto(-100,20)
    turtle2.goto(-100,-20)

window.exitonclick()




#Part B
pygame.init()
window = pygame.display.set_mode()
points=[]
xpos=0
ypos=0


num_sides=int(input("Please enter the number of sides for the shape: "))
side_length=int(input("please enter the length of each side: "))

for i in range(num_sides):
    iAngle=360/num_sides
    radians= math.radians(iAngle*i)
    x= xpos+side_length*math.cos(radians)
    y= ypos+side_length*math.sin(radians)
    points.append([x,y])
    
    pygame.draw.polygon(window,"red",points,)
    pygame.display.flip()
    pygame.time.wait(1500)

    window.fill("white")
    pygame.display.flip()

