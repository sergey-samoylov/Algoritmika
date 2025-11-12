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

#отрисовка волны, не менять
penup()
goto(-110,-25)
pendown()
color("blue")
pensize(2)
left(45)
speed(0)
i=0

while i<20:
  forward(10)
  right(90)
  forward(10)
  left(90)
  i=i+1

right(45)
#отрисовка кораблика
penup()
goto(0,50)
pendown()
ship()
exitonclick()
