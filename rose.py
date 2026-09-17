import turtle

screen = turtle.Screen()
screen.bgcolor("black")

rose = turtle.Turtle()
rose.speed(0)
rose.color("red")
rose.pensize(2)

for i in range(36):
    for j in range(8):
        rose.circle(80)
        rose.left(45)
    rose.left(10)

turtle.done()
