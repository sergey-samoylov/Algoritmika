from turtle import *
from random import choice

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

getscreen().bgcolor("#994444")

for i in range(40):
    color(choice(colors))
    forward(250)
    left(170)

exitonclick()
