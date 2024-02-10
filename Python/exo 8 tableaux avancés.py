from random import *
from turtle import *

def dessine(tab):
    speed(0)
    hideturtle()
    for ligne in range(len(tab[0])):
        for elt in range(len(tab)):
            if tab[ligne][elt] == True:
                fillcolor("black")
                color("black")
            else:
                fillcolor("white")
                color("white")
            begin_fill()
            for i in range(4):
                forward(50)
                left(90)
            end_fill()
            forward(50)
        up()
        left(180)
        forward(50 * len(tab))
        left(90)
        forward(50)
        left(90)
        down()
    
tab = [[True, False, True],
       [False, True, False],
       [True, False, True]]

dessine(tab)
exitonclick()
