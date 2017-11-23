"""
This is a Point class, the solution to a homework assignment I created for
the class I help teach, Roadmap to Computing using Python. This is to
demonstrate to students the basics of object oriented programming.
The Point class is a classic used in the introduction, and I thought it
would be fun for students to see the output on the screen using turtle graphics.
"""
import math
import turtle
class Point:
    '''This is a Point'''
    count = 0
    def __init__(self, xc, yc, col): #def Point(self,xc,yc):
        self.x = xc
        self.y = yc
        self.t = turtle.Turtle()
        self.t.color(col)
        Point.count += 1

    def coordinates(self):
        #Return a tuple of the coordinates
        return (self.x, self.y)

    def move_to(self, xc, yc):
        self.x = xc
        self.y = yc
        self.t.up()
        self.t.goto(xc,yc)
        self.t.down()
        

    def move(self, xD, yD):
        self.x += xD
        self.y += yD
        self.t.up()
        self.t.fd(xD)
        if (yD > 0):
            self.t.lt(90)
            self.t.fd(yD)
            self.t.rt(90)
        elif (yD < 0):
            self.t.rt(90)
            self.t.fd(yD)
            self.t.lt(90)
        self.t.down()

    def drawAxes(self,x,y):
        self.t.fd(x)
        self.t.bk(x * 2)
        self.t.fd(x)
        self.t.lt(90)
        self.t.fd(y)
        self.t.bk(y * 2)
        self.t.fd(y)
        self.t.rt(90)

    def distance_to(self, point):
        #sqrt((x2-x1)^2 + (y2-y1)^2)
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)

    def drawPolygon(self, size, sides):
        for i in range(sides):
            self.t.fd(size)
            self.t.lt(360/sides)
def getCount():
    return Point.count
