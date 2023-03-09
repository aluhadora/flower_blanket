#Python Turtle - Spirograph - www.101computing.net/python-turtle-spirograph/
import turtle
from math import cos,sin,pi
from time import sleep
import random
import flower_colors

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

def randomly_generate_petal(colors):
    total_index = 0
    indexed_colors = {}
    current_index = 0

    for color, element in colors.items():
        weight = element[1]
        total_index += weight
    
        for _ in range(weight):
            indexed_colors[current_index] = color
            current_index += 1

    index = random.randrange(0, total_index - 1)
    return indexed_colors[index]

init()

colors = {
    'Admiral': ("", 1),              # 0
    'Ivory': ("", 1),                # 1, 2
    'Himalayan': ("", 2),            # 3, 4
    'Canyon': ("", 2),               # 5, 6
    'Bee Pollen': ("", 1),           # 7
    'Dijon': ("", 1),
    'Tourmaline': ("", 1),
    'Caper': ("", 1),
    'Peacock': ("", 2),
    'Stonewash': ("", 1),
    'Amethyst': ("#6F6A81", 1),
    'Raisin': ("", 1),
    'Satellite': ("", 1),
    'Bone': ("", 1),
    'Nutmeg': ("", 1),
    'Moonbeam': ("", 1),
    'Provence': ("", 1),
    'Thunder': ("", 1),
    'Badlands': ("", 1),
    'Channel Islands': ("", 1),
    'Wolf Trap': ("", 1),
    'Indiana Dunes': ("", 1)
}

colors = {
    "Admiral": ("#2b293e", 1),
    "Amethyst": ("#79748b", 1),
    "Bee Pollen": ("#beaa47", 1),
    "Bone": ("#bfaca6", 1),
    "Canyon": ("#83493d", 2),
    "Caper": ("#878463", 1),
    "Channel Islands": ("#c4e5b8", 1),
    "Dijon": ("#9e7c35", 1),
    "Himalayan": ("#d99e74", 2),
    "Indiana Dunes": ("#8f7552", 1),
    "Ivory": ("#efecd9", 1),
    "Moonbeam": ("#e3e1d5", 1),
    "Nutmeg": ("#9f7a5d", 1),
    "Peacock": ("#1a433f", 2),
    "Provence": ("#bdb2c3", 1),
    "Raisin": ("#956853", 1),
    "Satellite": ("#b2b3ab", 1),
    "Stonewash": ("#62747e", 1),
    "Thunder": ("#222126", 1),
    "Tourmaline": ("#96b3af", 1),
    "Wolf Trap": ("#E5D0C6", 1),
}

spacing = 80

# index = 0
# one_off = []
# for color, _ in colors.items():
#     one_off.append(color)

# for j in range(-2,2):
#     for i in range(-3,3):
#         if (index < len(one_off)):
#             color = colors[one_off[index]][0]
#             draw_flower(spacing*i + (j%2) * spacing/2, spacing*j, color, color, (i % 2) * .82)
#             index += 1

all_colors = list(colors.keys())
allowable_colors, _ = flower_colors.build_allowable_colors(all_colors)

for i in range(-15,15):
    for j in range(-13,13):
        petal_color = randomly_generate_petal(colors)
        petal_color_hex = colors[petal_color][0]
        
        middle_color = random.choice(allowable_colors[petal_color])
        middle_color_hex = colors[middle_color][0]
        draw_flower(spacing*i + (j%2) * spacing/2, spacing*j, petal_color_hex, middle_color_hex, (i % 2) * .82)

turtle.exitonclick()

  
