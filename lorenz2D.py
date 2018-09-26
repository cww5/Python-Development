import turtle

t = turtle.Turtle()
t.hideturtle()
x, y, z = 0.01, 0.01, 0.01

a = 10
b = 28
c = 8/3

dt = 0.01

for time in range(2000):
    dx = (a * (y - x))*dt
    dy = (x * (b - z) - y)*dt
    dz = (x * y - c * z)*dt
    x = x + dx
    y = y + dy
    z = z + dz
    t.pendown()
    t.goto(x*5,y*5)
