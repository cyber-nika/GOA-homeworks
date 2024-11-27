import turtle

# შექმენით ტერტლი
screen = turtle.Screen()
screen.bgcolor("skyblue")  # ფონი ცისფერია

t = turtle.Turtle()
t.speed(10)

# მთა
def draw_mountain(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.fillcolor("gray")
    t.setheading(60)
    for _ in range(3):
        t.forward(100)
        t.left(120)
    t.end_fill()

# მდინარე
def draw_river():
    t.penup()
    t.goto(-400, -100)
    t.pendown()
    t.begin_fill()
    t.fillcolor("blue")
    t.setheading(0)
    t.forward(800)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(800)
    t.right(90)
    t.forward(100)
    t.end_fill()

# გზა
def draw_road():
    t.penup()
    t.goto(-150, -100)
    t.pendown()
    t.begin_fill()
    t.fillcolor("gray")
    t.setheading(0)
    t.forward(300)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(300)
    t.right(90)
    t.forward(20)
    t.end_fill()

# ხეები
def draw_tree(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    # ხის ტრUNKი
    t.begin_fill()
    t.fillcolor("brown")
    t.setheading(0)
    for _ in range(2):
        t.forward(20)
        t.left(90)
        t.forward(40)
        t.left(90)
    t.end_fill()
    # ხის ფოთლები
    t.penup()
    t.goto(x - 30, y + 40)
    t.pendown()
    t.begin_fill()
    t.fillcolor("green")
    t.circle(30)
    t.end_fill()

# სახლი
def draw_house():
    t.penup()
    t.goto(-50, -150)
    t.pendown()
    # სახლის კედელი
    t.begin_fill()
    t.fillcolor("yellow")
    for _ in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()

    # სახლის სახურავი
    t.penup()
    t.goto(-50, -50)
    t.pendown()
    t.begin_fill()
    t.fillcolor("brown")
    t.setheading(45)
    for _ in range(2):
        t.forward(70)
        t.right(90)
    t.end_fill()

# მზე
def draw_sun():
    t.penup()
    t.goto(250, 150)
    t.pendown()
    t.begin_fill()
    t.fillcolor("yellow")
    t.circle(50)
    t.end_fill()

# დავხატოთ ყველა ელემენტი
draw_mountain(-300, 50)
draw_mountain(50, 100)
draw_river()
draw_road()
draw_tree(-200, -50)
draw_tree(100, -70)
draw_tree(-50, -30)
draw_house()
draw_sun()

# დახურვა
t.hideturtle()
screen.mainloop()
