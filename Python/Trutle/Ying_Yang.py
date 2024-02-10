from turtle import *
import turtle

# mettre la flèche en bas
up()
goto(0, -150)
down()

# contour rond
circle(150)

# coté noir
begin_fill()
circle(75)
end_fill()
begin_fill()
circle(150, 180)
goto(0, -150)
end_fill()

# coté blanc
left(180)

circle(150, 180)
fillcolor("white")
left(90)
forward(150)
left(90)
begin_fill()
circle(75, 180)
end_fill()

# petit cercle noir
left(90)
up()
forward(100)
left(90)
forward(5)
down()

fillcolor("black")
begin_fill()
circle(25)
end_fill()

# petit rond blanc
up()
goto(0, -150)
left(70)
forward(75)
down()

fillcolor("white")
begin_fill()
circle(25)
end_fill()

hideturtle()
