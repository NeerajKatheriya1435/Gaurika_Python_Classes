import turtle

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)

colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A8", "#A833FF"]

for i in range(360):
    t.pencolor(colors[i % 5])
    t.circle(i * 0.5)
    t.left(50)

turtle.done()