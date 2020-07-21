"""This is a demo of the Shapes"""

import turtle as turtle
import math
import sys
WINDOW_SIZE = 500



def init():
    turtle.setworldcoordinates(-500, -500, 500, 500)
    turtle.speed()
    turtle.hideturtle()

def draw_shape_1(radius):
    turtle.color('red')
    turtle.circle(radius)

def draw_shape_2a(radius):
    turtle.color('green')
    while turtle.circle(radius):
        (draw_shape_1(radius/2))

def draw_shape_2b(radius):
    turtle.color('green')
    turtle.circle(radius)
    while draw_shape_2b(radius/2):
        draw_shape_1()

def draw_shape_rec(radius, depth):
    if depth > 0:
        pass
    for _ in range(6):
        turtle.circle(radius)
        draw_shape_1(radius, depth)
    return draw_shape_rec(radius/2, depth-1)


def main():
    init()
    draw_shape_2a(100)
    #draw_shape_2b(100)
    #draw_shape_rec(100, 100)
    turtle.mainloop()

if __name__ == "__main__":
    main()
