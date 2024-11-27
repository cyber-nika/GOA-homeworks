import turtle

# ეკრანის დამზადება
screen = turtle.Screen()
screen.bgcolor("white")

# დასაწყისის turtle
ronaldo = turtle.Turtle()
ronaldo.shape("turtle")
ronaldo.color("blue")

# Turtle-ის დაწყება
ronaldo.penup()
ronaldo.goto(-50, 0)
ronaldo.pendown()

# მისი სახელი "CR" ტილზე
ronaldo.write("CR", font=("Arial", 40, "bold"))

# ცოტა ელემენტების დასამატებლად, რომ ლოგო შევქმნათ
ronaldo.penup()
ronaldo.goto(-50, -50)
ronaldo.pendown()
ronaldo.circle(50)  # პატარა წრე, რომელიც შეიძლება ნაჩვენები იყოს ფეხბურთის ბურთის მარკირებისთვის

# დასრულება
ronaldo.hideturtle()

turtle.done()
