from turtle import Turtle, done

# Программа нарисует сердце для Мамы на 8 марта.
t = Turtle()

t.color("red")
t.fillcolor("red")

t.begin_fill()

t.left(140)
t.fd(180)
t.circle(-90, 200)
t.left(120)
t.circle(-90, 200)
t.fd(180)

t.end_fill()

t.hideturtle()
done()
