import turtle
import random

turtle.showturtle()

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


def drunkWalk():
    counter = 0
    while turtle.xcor() > 0 and turtle.xcor() < 500 and turtle.ycor() > 0 and turtle.ycor() < 500:
        direction()
        turtle.forward(20)
        counter  = counter + 20
    turtle.write(counter, font=("Arial", 10, "normal"))

def main():
    turtle.speed(10)
    turtle.setworldcoordinates(0, 0, 500, 500)
    turtle.pu()
    turtle.goto(250,250)
    turtle.pd()
    drunkWalk()

if __name__=='__main__':
    main()
