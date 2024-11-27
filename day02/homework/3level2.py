import turtle

# ეკრანის შექმნა
screen = turtle.Screen()
screen.bgcolor("lightblue")

# ძირითადი სასახლის შექმნა
def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

# სასახლის სახურავი
def draw_roof(x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(45)
    turtle.begin_fill()
    turtle.fillcolor("brown")
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(45)
    turtle.end_fill()

# სასახლის კოშკები
def draw_tower(x, y, width, height):
    draw_rectangle("gray", x, y, width, height)
    draw_roof(x - width/2, y + height, width, width)

# მთავარი კორპუსი
draw_rectangle("lightgray", -200, -150, 400, 300)

# კოშკების შექმნა
draw_tower(-300, -150, 50, 150)
draw_tower(250, -150, 50, 150)

# კარი
draw_rectangle("brown", -50, -150, 100, 150)

# ფანჯრები
draw_rectangle("white", -150, 50, 50, 50)
draw_rectangle("white", 100, 50, 50, 50)

# Turtle-ის დასრულება
turtle.hideturtle()
turtle.done()
