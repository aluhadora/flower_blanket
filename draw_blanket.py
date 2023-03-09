import turtle
from math import cos,sin,pi
from time import sleep
import random
from mapped_colors import colors
from drawing_flowers import draw_flower
import flower_colors
from numpy.random import choice


def init_screen():
    window = turtle.Screen()
    window.bgcolor("tan")
    window.screensize = (1920, 1080)
    turtle.tracer(False)
    window.tracer(0)

def randomly_generate_petal(colors):
    all_colors = []
    all_weights = []
    totalWeight = sum(map(lambda x : x[1][1], colors.items()))

    for color, element in colors.items():
        weight = element[1]
        all_colors.append(color)
        all_weights.append(weight/totalWeight)

    return choice(all_colors, 1,
              p=all_weights)[0]

def main():
    init_screen()

    all_colors = list(colors.keys())
    allowable_colors, _ = flower_colors.build_allowable_colors(all_colors)

    spacing = 80

    for i in range(-15,15):
        for j in range(-13,13):
            petal_color = randomly_generate_petal(colors)
            petal_color_hex = colors[petal_color][0]
            
            middle_color = random.choice(allowable_colors[petal_color])
            middle_color_hex = colors[middle_color][0]
            draw_flower(spacing*i + (j%2) * spacing/2, spacing*j, petal_color_hex, middle_color_hex, (i % 2) * .82)

    turtle.exitonclick()
    

if __name__ == "__main__":
    main()