"""
    Filename: olsonProj5.py
    Author:Jamie Olson
    Date:2/13/2023
    Course:COMP 1352
    Assignment: Project 5 - Conga Line 
    Collaborators:n/a
    Internet Source:n/a
"""




from dudraw import dudraw, Color
from random import random, randint
class Dancer:
    def __init__(self,xPrime = 0, yPrime = 0, x = 0, y = 0):
        self.xPrime = xPrime
        self.yPrime = yPrime
        self.x = x
        self.y = y
        self.color = Color(randint(0,255), randint(0,255),randint(0,255))

    def __str__(self):
        return f'current XY: {self.x} {self.y} \n target: {self.xPrime} {self.yPrime}'
    
    def draw(self):
        dudraw.set_pen_color(self.color)
        dudraw.filled_circle(self.xPrime,self.yPrime,randint(0,10))
    def move(self):
        self.xPrime += (self.x - self.xPrime) * 0.3
        self.yPrime += (self.y - self.yPrime ) * 0.3
    def set_target(self,x,y):
        self.x = x
        self.y = y

w=400
h=400

dudraw.set_canvas_size(w,h)
dudraw.set_x_scale(0, w)
dudraw.set_y_scale(0, h)

CONGA = []
dancers = [Dancer(randint(0,w),randint(0,w),0,0) for _ in range(6)]
key = ''

while key != 'q':
    dudraw.clear(dudraw.LIGHT_GRAY)
    for i in range(len(dancers)):
        if i == 0:
            dancers[i].set_target(dudraw.mouse_x(), dudraw.mouse_y())
        else:
            dancers[i].set_target(dancers[i-1].xPrime, dancers[i-1].yPrime)
        dancers[i].move()
        dancers[i].draw()
    if dudraw.has_next_key_typed():
        key = dudraw.next_key_typed()
        if key == 'n':
            dancers.append(Dancer(randint(0,400),randint(0,400),0,0))
    dudraw.show(30)


