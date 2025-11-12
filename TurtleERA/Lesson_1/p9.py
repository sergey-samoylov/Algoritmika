#!/usr/bin/env python3

from turtle import *
pensize(2)
color("black")
begin_fill()
circle(60)
end_fill()
penup()


color("red")
goto(100,100)
pendown()
begin_fill()
circle(20)
end_fill()
penup()


color("green")
goto(-100,-100)
pendown()
begin_fill()
circle(30)
end_fill()
penup()


color("blue")
goto(-100,100)
pendown()
begin_fill()
circle(40)
end_fill()
penup()


color("yellow")
goto(100,-100)
pendown()
begin_fill()
circle(80)
end_fill()


exitonclick()
