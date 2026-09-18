# import turtle

# screen = turtle.Screen()
# screen.bgcolor("black")

# rose = turtle.Turtle()
# rose.speed(0)
# rose.color("red")
# rose.pensize(2)

# for i in range(36):
#     for j in range(8):
#         rose.circle(80)
#         rose.left(45)
#     rose.left(10)

# turtle.done()


import turtle
import math
import time

screen = turtle.Screen()
screen.bgcolor("#06110a")
screen.title("🌸 Blooming Lily")
screen.tracer(0, 0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)


# ----------------------------
# Draw a petal
# ----------------------------
def draw_petal(angle, size, color):
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.forward(12)
    t.pendown()

    t.color(color)
    t.begin_fill()

    # Left side
    t.setheading(angle + 25)
    t.circle(size * 0.45, 55)

    # Rounded tip
    t.setheading(angle + 90)
    t.circle(size * 0.35, 60)

    # Right side
    t.setheading(angle + 180)
    t.circle(size * 0.45, 55)

    # Return to center
    t.setheading(angle + 205)
    t.circle(size * 0.35, 60)

    t.end_fill()


# ----------------------------
# Stem animation
# ----------------------------
def draw_stem(length):
    t.penup()
    t.goto(0, -300)
    t.setheading(90)
    t.pendown()

    t.color("#277a35")
    t.pensize(10)

    t.forward(length)


# ----------------------------
# Leaf
# ----------------------------
def draw_leaf(x, y, angle, size):
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()

    t.color("#328c3d")
    t.begin_fill()

    t.circle(size, 35)
    t.left(145)
    t.circle(size, 35)

    t.end_fill()


# ----------------------------
# Bloom animation
# ----------------------------
angles = [90, 30, 150, 210, 270, 330]

# Stem grows
for length in range(0, 301, 10):
    t.clear()
    draw_stem(length)

    # Leaves appear gradually
    if length > 130:
        draw_leaf(0, -170, 145, 70)

    if length > 190:
        draw_leaf(0, -220, 35, 65)

    screen.update()
    time.sleep(0.03)


# Petals slowly open
for size in range(20, 181, 5):

    t.clear()

    # Stem
    draw_stem(300)

    # Leaves
    draw_leaf(0, -170, 145, 70)
    draw_leaf(0, -220, 35, 65)

    # Petals
    for angle in angles:
        draw_petal(angle, size, "#fffaf2")

    screen.update()
    time.sleep(0.04)


# ----------------------------
# Pink veins appear
# ----------------------------
for angle in angles:
    t.penup()
    t.goto(8, 0)
    t.setheading(angle)
    t.forward(20)
    t.pendown()

    t.color("#e98da8")
    t.pensize(3)
    t.forward(115)

    screen.update()
    time.sleep(0.12)


# ----------------------------
# Stamens grow outward
# ----------------------------
for angle in [65, 90, 115, 245, 270, 295]:

    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.forward(10)
    t.pendown()

    t.color("#d9a900")
    t.pensize(3)

    for length in range(0, 75, 5):
        t.forward(5)
        screen.update()
        time.sleep(0.02)

    # Anther
    t.dot(10, "#f2c230")


# ----------------------------
# Flower center
# ----------------------------
t.penup()
t.goto(0, 0)
t.dot(22, "#e8ad32")

# Pollen
for angle in range(0, 360, 30):
    x = math.cos(math.radians(angle)) * 30
    y = math.sin(math.radians(angle)) * 30

    t.goto(x, y)
    t.dot(4, "#f5cf4a")

screen.update()

turtle.done()


