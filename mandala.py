import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.title("Geometric Mandala")

pattern = turtle.Turtle()
pattern.speed(0)
pattern.hideturtle()
pattern.width(1)

total_shapes = 120
hue = 0.0

for i in range(total_shapes):
    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    pattern.color(color)
    hue += 1.0 / total_shapes
    
    pattern.penup()
    pattern.goto(0, 0)
    pattern.pendown()
    pattern.forward(120)
    pattern.right(45)
    pattern.forward(60)
    pattern.right(135)
    
    pattern.circle(100, 180)
    pattern.left(90)
    pattern.circle(100, 180)
    
    pattern.right(360 / total_shapes + 1.5)

pattern.penup()
pattern.goto(0, -30)
pattern.pendown()
pattern.setheading(0)

for i in range(60):
    color = colorsys.hsv_to_rgb(1.0 - (i / 60.0), 1.0, 1.0)
    pattern.color(color)
    pattern.circle(30)
    pattern.right(360 / 60)

screen.exitonclick()
