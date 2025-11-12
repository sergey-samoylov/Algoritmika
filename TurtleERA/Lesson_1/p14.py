#!/usr/bin/env python3

from turtle import *

colors = (
    "black",
    "blue",
    "red",
    "green",
    "yellow",
    "cyan",
    "violet",
    "purple",
)

def draw_cube():
    for side in range(4):
        forward(100)
        left(90)

def choose_color():
    for i in colors:
        color(i)
        draw_cube()
        left(12)
    
for i in range(4):
    choose_color()

exitonclick()
