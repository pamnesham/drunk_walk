import turtle
import random

turtle.showturtle()

#Setup the speed, turtle coordinates, and canvas color and size
def main():
    turtle.setup(width = 500, height = 500)
    turtle.speed(10)
    turtle.bgcolor("#800080")
    turtle.setworldcoordinates(0, 0, 500, 500)
    turtle.pu()
    turtle.goto(250,250)
    turtle.pd()
    drunkWalk()

#The turtle's direction is determined by random numbers
#   associated with 0, 90, 180, and 270 degrees
def direction():
    direct = random.randint(1,4)
    if direct == 1:
        turtle.left(0)
    elif direct == 2:
        turtle.left(90)
    elif direct  == 3:
        turtle.left(180)
    else:
        turtle.left(270)

#Moving the turtle and counting total steps taken
def drunkWalk():
    counter = 0
    while turtle.xcor() > 0 and turtle.xcor() < 500 and turtle.ycor() > 0 and turtle.ycor() < 500:
        direction()
        turtle.forward(20)
        counter  = counter + 20
    turtle.pu()
    turtle.goto(250,400)
    turtle.hideturtle()
    turtle.pd()
    turtle.write("Steps taken to escape Dinkytown: " + str(counter), align = "center", font=("Arial", 13, "bold"))

if __name__=='__main__':
    main()
