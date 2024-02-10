import turtle
from turtle import *
x = float(input("Choisir une valeur pour l'arrète du triangle : "))

speed(2)
down()

# base triangle
for i in range(3):
    forward(x)
    left(360/3)

for i in range(3):
    left(30)
    forward(x/2)
    left(180)
    forward(x/2)
    left(180+60-90)
    forward(x)
