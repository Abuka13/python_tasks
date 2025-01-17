import turtle
screen = turtle.Screen()
screen.title("Turtle Drawing")
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(3)
t.penup()
t.goto(-150, 100)
t.pendown()
for _ in range(4):
    t.forward(100)
    t.right(90)
t.penup()
t.goto(100, 50)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
t.circle(50)
t.end_fill()
t.penup()
t.goto(-50, -150)
t.write("Two Figures: Square and Colored Circle", align="center", font=("Arial", 14, "normal"))
t.hideturtle()
screen.mainloop()
