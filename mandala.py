import turtle
import math

turtle.bgcolor('black')
turtle.speed('fastest')
turtle.title('Blue Archive')

colors = ["red", "white"]

def sensei(a, b):
    turtle.penup()
    turtle.goto(a, b)
    turtle.pendown()
    turtle.pencolor('white')
    turtle.pensize('5')

def arona():
    for i in range(23):
                turtle.forward(360)
                turtle.fillcolor('#7FFFD4')
                turtle.begin_fill()
                turtle.circle(20)
                turtle.end_fill()
                turtle.left(219)

def shiroko():
    for i in range(9):
                turtle.forward(80)
                turtle.left(160)
                
class HiganBana:
    @staticmethod
    def set_pos(pos_x, pos_y):
        turtle.penup()
        turtle.setpos(pos_x, pos_y)
        turtle.pensize('5')
        a=turtle.pendown()

    @staticmethod
    def halo(size, color):
        turtle.width(1)
        turtle.color(color)
        for i in range(size):
            turtle.circle(size - i, 90)
            turtle.left(90)
            turtle.circle(size - i, 90)
            turtle.left(18)
        turtle.penup()
        turtle.setpos (0, -280)
        turtle.pensize('5')
        turtle.pendown()
        turtle.circle(315)
        turtle.penup()
        turtle.setpos (0, -300)
        turtle.pensize('5')
        turtle.pendown()
        turtle.circle(335)

pattern = HiganBana()

pattern.set_pos(0, 35)
pattern.halo(220, "red")

sensei(-180, 100)
arona()
sensei(-40, 30)
shiroko()
sensei(-10, -184)
turtle.circle(220)
sensei(-10, -194)
sensei(-10, -144)
turtle.circle(180)
sensei(-2, -10)
turtle.circle(46)

turtle.penup()
turtle.pencolor('blue')
turtle.pensize('7')
turtle.setpos(40, 35)
turtle.pendown()

'''Could refactor this a bit more'''
turtle.left(45)
turtle.goto(0, 60)
turtle.goto(0, 1000)
turtle.goto(-1,1000)
turtle.goto(-1,60)
turtle.left(45)
turtle.goto(-40, 35)
turtle.goto(-1000, 35)
turtle.goto(-1000, 34)
turtle.goto(-40, 34)
turtle.left(45)
turtle.goto(-1, 5)
turtle.goto(-1, -1000)
turtle.goto(0,-1000)
turtle.goto(0, 5)
turtle.left(45)
turtle.goto(40, 34)
turtle.goto(1000, 34)
turtle.goto(1000, 35)
turtle.goto(40, 35)

turtle.penup()
turtle.setpos (25, 450)
turtle.pensize('5')
turtle.pendown()
turtle.circle(420)
turtle.penup()
turtle.setpos (25, 470)
turtle.pensize('5')
turtle.pendown()
turtle.circle(440)
turtle.setpos (25, 490)
turtle.pensize('5')
turtle.pendown()
turtle.circle(460)

turtle.hideturtle()
turtle.done()
