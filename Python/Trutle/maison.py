from turtle import *
import turtle


speed(5)
up()
goto(0, 0)
down()

# base carré de la maison
for i in range(4):
    forward(100)
    left(90)

# se mettre en haut du carré
left(90)
forward(100)
right(90)

# triangle du toit
for i in range(3):
    forward(100)
    left(120)

exitonclick()
