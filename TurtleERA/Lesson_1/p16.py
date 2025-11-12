#!/usr/bin/env python3

from turtle import *

colors = (
    "red",
    "yellow",
    "green",
    "blue",
    "purple",
    "orange",
)

speed(500)
bgcolor("black")

for x in range(360):
    pencolor(colors[x % 6])
    width(x // 100 + 1)
    forward(x)
    left(59)

exitonclick()
