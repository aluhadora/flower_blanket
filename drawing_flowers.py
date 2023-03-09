#Python Turtle - Spirograph - www.101computing.net/python-turtle-spirograph/
import turtle
from math import cos,sin,pi
from time import sleep

def init():
    window = turtle.Screen()
    window.bgcolor("tan")
    window.screensize = (1920, 1080)
    turtle.tracer(False)
    window.tracer(0)

def draw_petals(offset_x, offset_y, color, mult, offset_angle):
    myPen = turtle.Turtle()
    myPen.hideturtle()
    myPen.speed(0)
    myPen.pensize(3)
    myPen.color(color.upper())
    offset_y += 50

    R = 6 * mult
    r = mult
    d = 6 * mult

    angle = 0

    myPen.penup()
    x = (R - r) * cos(angle+offset_angle) + d * cos(((R-r)/r)*angle+offset_angle) + offset_x
    y = (R - r) * sin(angle+offset_angle) - d * sin(((R-r)/r)*angle+offset_angle) + offset_y
    myPen.goto(x, y)
    myPen.pendown()

    theta = 0.05
    steps = int(2*pi/theta) + 1

    myPen.begin_fill()

    for t in range(0,steps):
        angle+=theta

        x = (R - r) * cos(angle+offset_angle) + d * cos(((R-r)/r)*angle+offset_angle) + offset_x
        y = (R - r) * sin(angle+offset_angle) - d * sin(((R-r)/r)*angle+offset_angle) + offset_y
        
        myPen.goto(x, y)

    myPen.end_fill()        

    myPen.getscreen().update()

def draw_center(offset_x, offset_y, color):
    myPen = turtle.Turtle()
    myPen.hideturtle()
    myPen.fillcolor(color)
    myPen.speed(0)
    myPen.pensize(3)
    myPen.color(color)
    offset_y += 50

    R = 12

    angle = 0

    myPen.penup()
    myPen.goto(offset_x, offset_y)
    myPen.pendown()

    theta = 0.05
    steps = int(2*pi/theta) + 1

    myPen.begin_fill()
    for t in range(0,steps):
        angle+=theta

        x = (R) * cos(angle) + offset_x
        y = (R) * sin(angle) + offset_y
        
        myPen.goto(x, y)

    myPen.end_fill()
    myPen.penup()
    # myPen.getscreen().update()

def draw_flower(x, y, petal_color, center_color, offset_angle):
    draw_petals(x, y, petal_color, 4, offset_angle)
    # draw_petals(x, y, petal_color, 3, offset_angle)
    # draw_petals(x, y, petal_color, 2, offset_angle)
    # draw_petals(x, y, petal_color, 1, offset_angle)
    draw_center(x, y, center_color)
    turtle.Screen().update()


  
