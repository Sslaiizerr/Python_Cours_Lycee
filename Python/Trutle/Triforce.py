from turtle import *


def triangle(n):
    begin_fill()
    for i in range(3):
        forward(n)
        left(120)
    end_fill()


triangle(100)
forward(100)
triangle(100)
left(60)
forward(100)
left(120)
forward(100)
left(180)
triangle(100)

exitonclick()
