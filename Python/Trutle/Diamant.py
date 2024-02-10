from turtle import*
import turtle

pendown()
speed(5)
color("blue")
width(5)

# trait axe x
forward(250)
forward(-500)

# trait axe y
goto(0, 0)
left(90)
forward(125)
left(180)
forward(250)

# coté supérieur droit
goto(0, 0)
left(90)
for i in range(1, 6):
    d = i * 50
    forward(d)
    goto(0, 125)
    penup()
    goto(0, 0)
    pendown()

# coté inférieur droit
goto(0, 0)
for i in range(1, 6):
    d = i * 50
    forward(d)
    goto(0, -125)
    penup()
    goto(0, 0)
    pendown()

# coté supérieur gauche
goto(0, 0)
for i in range(1, 6):
    d = i * -50
    forward(d)
    goto(0, 125)
    penup()
    goto(0, 0)
    pendown()

# coté inférieur gauche
goto(0, 0)
for i in range(1, 6):
    d = i * -50
    forward(d)
    goto(0, -125)
    penup()
    goto(0, 0)
    pendown()

hideturtle()
exitonclick()
