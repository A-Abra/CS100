'''
Anosh Abraham
CS 100 2019 Section 004
HW 03, September 23, 2019
'''

import turtle
paper = turtle.Screen()
pen = turtle.Turtle()
length = 100
pen.speed(0)

#1
def drawShapes(sideLength):
    pen.up()
    pen.goto(-200,0)
    pen.down()

    for each in range(3):
        pen.forward(sideLength)
        pen.right(120)

    pen.up()
    pen.forward(125)
    pen.down()

    for each in range(4):
        pen.forward(sideLength)
        pen.right(90)

    pen.up()
    pen.forward(150)
    pen.down()

    for each in range(5):
        pen.forward(sideLength)
        pen.right(72)

drawShapes(length)

#2
def drawCircle(r,pos):
    pen.up()
    pen.goto(0,pos)
    pen.down()
    pen.circle(r)


drawCircle(50,0)
drawCircle(100,-50)
drawCircle(150,-100)
drawCircle(200,-150)

#3
import math

print("factorial of  100!: "+str(math.factorial(100)))
print()
print("log base 2 of 1000000: "+str(math.log(1000000,2)))
print()
print("GCD of 63 and 49: "+str(math.gcd(63,49)))
