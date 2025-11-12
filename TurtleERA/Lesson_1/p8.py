#!/usr/bin/env python3

from turtle import *


def ship():
   color('light blue')
   pensize(5)
   forward(50)
   left(180-45)
   forward(70)
   left(180-45)
   forward(50)
   color('black')
   pensize(2)
   forward(30)
   right(90)
   forward(45)
   left(180-45)
   forward(50)
   left(45)
   forward(80)
   left(45)
   forward(50)
   left(180-45)
   forward(105)


penup()
goto(0,-30)
pendown()
ship()
penup()
goto(130,130)
pendown()
right(180)
ship()
penup()
goto(-130,130)
pendown()
right(180)
ship()
exitonclick()

