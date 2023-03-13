import turtle
sides= input("Enter the number of sides:")
sides= int(sides)
length= int(input("Enter the length of the sides:"))
pen= turtle. Turtle ()
pen.color("green")
window= turtle. Screen()
for s in range (sides):
    pen. forward(length)
    pen. right(360/sides)
