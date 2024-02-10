from turtle import *
from colorsys import *

setup(800, 800)
speed(0)
width(2)
color("black")
for j in range(25):
    for i in range(15):
        color(hsv_to_rgb(i/15, j/25, 1))
        right(90)
        circle(200-j*4,90)
        left(90)
        circle(200-j*4, 90)
        right(180)
        circle(50, 24)
hideturtle()
done()