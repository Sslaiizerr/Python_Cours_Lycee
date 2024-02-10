from turtle import *

setup(1000, 1000)
speed(5)
up()
goto(-200, -200)
down()


def triangle(n):
    """
    permet de construire un triangle de longeur 'n'
    """
    begin_fill()
    for i in range(3):
        forward(n)
        left(120)
    end_fill()


def monter(n):
    """
    permet d'aller au sommet du triangle de meme longeur que le triangle construit précédemment
    """
    forward(n)
    left(120)
    forward(n)
    left(60)


def prochain_triangle(n):
    left(90)
    forward(n/1.50)
    right(90)
    forward(n/2)
    right(180)


triangle(300)
monter(300)
prochain_triangle(200)
triangle(200)
monter(200)
prochain_triangle(100)
triangle(100)


exitonclick()
