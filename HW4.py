'''
Anosh Abraham
CS 100 2019 Section 004
HW 04, September 29, 2019
'''

#1 & 2
a = 3
b = 4
c = 5

if a<b:
    print("OK")
else:
    print("NOT OK")
if c<b:
    print("OK")
else:
    print("NOT OK")
if a+b==c:
    print("OK")
else:
    print("NOT OK")
if a**2+b**2==c**2:
    print("OK")
else:
    print("NOT OK")


#3
import turtle
paper = turtle.Screen()
pen = turtle.Turtle()

color = str(input("what color?"))
width = int(input("what line width?"))
length = int(input("what line length?"))
shape = str(input("line, triangle or square"))

color = color.lower()
pen.color(color)
pen.width(width)
shape = shape.lower()

if shape == 'line':
    pen.forward(length)
if shape == 'triangle':
    for i in range(3):
        pen.forward(length)
        pen.right(120)
if shape == 'square':
    for i in range(4):
        pen.forward(length)
        pen.right(90)
        
    
