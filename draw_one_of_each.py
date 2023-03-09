import turtle
from math import cos,sin,pi
from time import sleep
from mapped_colors import colors
from drawing_flowers import draw_flower

def init_screen():
    window = turtle.Screen()
    window.bgcolor("tan")
    window.screensize = (1920, 1080)
    turtle.tracer(False)
    window.tracer(0)

def main():
    init_screen()

    spacing = 80

    index = 0
    one_off = []
    for color, _ in colors.items():
        one_off.append(color)

    for j in range(-2,2):
        for i in range(-3,3):
            if (index < len(one_off)):
                color = colors[one_off[index]][0]
                draw_flower(spacing*i + (j%2) * spacing/2, spacing*j, color, color, (i % 2) * .82)
                index += 1

    turtle.exitonclick()
    

if __name__ == "__main__":
    main()