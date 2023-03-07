import random
import turtle
t = turtle.Turtle ()
t.shape("square")
t.speed(0)
wn = turtle. Screen()
wn.bgcolor("green")
distance = 10
angle = 90
is_in_screen = True
colors = ["red", "green", "blue", "purple", "red"]
while is_in_screen: 
    coin = random.randrange(0,2)
    if coin: # heads
        t.right(angle)
    else: # tails
        t.left(angle)
        t.forward(distance)
        turtleX = t.xcor()
        turtleY = t.ycor()
        x_range = wn.window_width() / 2
        y_rnage = wn.window_height() / 2
        t.color(random.choice(colors))
        if abs(turtleX) > x_range or abs(turtleY) > x_range:
            is_in_screen - False
            wn.exitonclick()
