""""
'''This program intends to recreate Hermann Scintillating Grid Illusion '''
file name: olson_optical_illusion.py
author : Jamie Olson
Date : October 9 , 2022
Course: COMP 1351
Assignment: Project 4 
Collaborators : None

"""

import dudraw
dudraw.set_canvas_size(500,500)
dudraw.clear(dudraw.LIGHT_GRAY)
dudraw.set_pen_color(dudraw.BLACK)

#This is the starting value of the x
x = 0.08
y = 0.08
w = 0.05
h = 0.05

 
#nested for to make the squares in a grid 
for i in range (8) : 
    for j in range(8) : 
        dudraw.filled_rectangle(x, y, w, h)
        x = x + 0.12
    y = y + 0.12 
    x=0.08

#new values for the circles 
y1 = 0.14
x1 = 0.14
w1 = 0.01

dudraw.set_pen_color(dudraw.WHITE)

#nested loop to make inner circle grid 
for i in range (7) :
    for j in range(7) : 
        dudraw.filled_circle(x1, y1, w1,)
        x1 = x1 + 0.12
    y1 = y1 + 0.12 
    x1 = 0.14
    
    

dudraw.show((float('inf')))

