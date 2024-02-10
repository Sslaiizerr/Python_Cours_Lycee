from turtle import*
import turtle

speed(3)
pendown()

# rectangle base
for i in range(2):
    forward(75)
    left(90)
    forward(50)
    left(90)

# rectangle bleu
color("blue", "blue")
begin_fill()
for i in range(2):
    forward(25)
    left(90)
    forward(50)
    left(90)
end_fill()

# avancer
forward(25)

# rectangle blanc
color("black", "white")
begin_fill()
for i in range(2):
    forward(25)
    left(90)
    forward(50)
    left(90)
end_fill()

# avancer
forward(25)

# rectangle rouge
color("red", "red")
begin_fill()
for i in range(2):
    forward(25)
    left(90)
    forward(50)
    left(90)
end_fill()

hideturtle()
