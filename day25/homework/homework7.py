import turtle

# შექმნა ეკრანი
screen = turtle.Screen()
screen.bgcolor("white")

# შემქმნელის შექმნა
pen = turtle.Turtle()

# პირველი კვადრატი
for _ in range(4):
    pen.forward(100)  # მარჯვენა მიმართულებით 100 პიქსელი
    pen.left(90)  # 90 გრადუსით მარცხნივ

# გადაადგილება მეორეზე
pen.penup()
pen.goto(150, 0)  # გადატანა მეორე ადგილას
pen.pendown()

# მეორე კვადრატი
for _ in range(4):
    pen.forward(100)
    pen.left(90)

# მეოთხე კვადრატი
pen.penup()
pen.goto(0, 150)
pen.pendown()

for _ in range(4):
    pen.forward(100)
    pen.left(90)

pen.hideturtle()

# ამოცანა დასრულებულია
screen.mainloop()
