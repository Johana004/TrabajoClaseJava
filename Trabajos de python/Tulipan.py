import turtle

window = turtle.Screen()
window.bgcolor("white")

pen = turtle.Turtle()
pen.color("red")
pen.speed(10)

pen.left(90)
pen.forward(100)
pen.right(90)
pen.width(10)
pen.forward(100)

for _ in range(45):
    pen.right(2)
    pen.forward(1)

for _ in range(45):
    pen.left(2)
    pen.forward(1)

pen.hideturtle()
window.exitonclick()