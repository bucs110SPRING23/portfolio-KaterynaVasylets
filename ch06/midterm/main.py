import turtle
import random

def draw_bubble(pen, x, y, size):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("black")
    pen.begin_fill()
    pen.circle(size)
    pen.end_fill()

    pen.speed("fastest")


def num_bubbles():

    bubbles = random.randint(0, 50)
    return bubbles


def main():
    # Define the colors for the background
    colors = ['pink', 'white']

    # Set up the turtle screen
    screen = turtle.Screen()
    screen.bgcolor("black")

    # Set up the turtle pen
    pen = turtle.Turtle()
    pen.pensize(10)

    # Define the colors of the rainbow
    colors = ['pink', 'black', 'pink', 'black', 'pink', 'black']

    # Draw the rainbow
    for color in colors:
        pen.color(color)
        pen.circle(100)
        pen.penup()
        pen.right(90)
        pen.forward(10)
        pen.left(90)
        pen.pendown()



    # Add a vertical and horizontal line in the middle
    pen.color('pink')
    pen.penup()
    pen.goto(0, 150)
    pen.pendown()
    pen.goto(0, -150)
    pen.penup()
    pen.goto(-250, 0)
    pen.pendown()
    pen.goto(250, 0)


    # Draw a flower in the middle
    pen.color('pink')
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    for i in range(5):
        pen.forward(100)
        pen.right(144)
    pen.penup()
    pen.goto(0, 25)
    pen.color('pink')
    pen.pendown()
    pen.begin_fill()
    pen.circle(25)
    pen.end_fill()

    # Draw a star in the middle
    pen.color('pink')
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    for i in range(5):
        pen.forward(100)
        pen.right(144)


    # Draw a star in the middle
    pen.color('pink')
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    for i in range(5):
        pen.forward(-100)
        pen.right(-144)

        # Draw a pentagon in the middle
    pen.color('pink')
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    for i in range(5):
        pen.forward(200)
        pen.right(288)


    # Draw a pentagon in the middle
    pen.color('pink')
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    for i in range(5):
        pen.forward(-200)
        pen.right(-288)

    # Add a vertical and horizontal line in the middle
    pen.color('black')
    pen.penup()
    pen.goto(0, 300)
    pen.pendown()
    pen.goto(0, -300)
    pen.penup()
    pen.goto(-400, 0)
    pen.pendown()
    pen.goto(400, 0)

    # go over
    pen.color('pink')
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()




        # Draw bubbles all over the screen

    number_bubbles = num_bubbles()


    for i in range(number_bubbles):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        size = random.randint(10, 50)
        draw_bubble(pen, x, y, size)


    # Change the background color rapidly between pink and white
    while True:
        color = random.choice(colors)
        screen.bgcolor(color)

    

    # Close the turtle screen on click
    screen.exitonclick()




main()








