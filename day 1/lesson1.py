from turtle import *

#we want to paint a house

#step 1: draw a square
shape("turtle")
speed(10)
width(7)
color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("black")
begin_fill()
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(60, 150)
pendown()

color("blue")
begin_fill()
left(30)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

penup()
goto(140, 150)
pendown()

color("blue")
begin_fill()
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()



exitonclick()