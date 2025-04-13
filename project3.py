"""
    Filename: project3.py
    Author:Jamie Olson
    Date:5/8/23
    Course:COMP 1353
    Assignment: Percolation 
    Collaborators:n/a
    Internet Source:n/a
"""


import time
import random
import dudraw

dudraw.set_canvas_size(400,400)
dudraw.set_x_scale(0,20)
dudraw.set_y_scale(0,20)


time.sleep(10)  # ⏳ Pauses the program for 5 seconds before running

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col

class Forest:
    def __init__(self, width, height, d):
        self.width = width
        self.height = height
        self.grid = []
        for i in range(height):
            row = []
            for j in range(width):
                if random.random() < d:
                    row.append(1)
                else:
                    row.append(0)
            self.grid.append(row)

    def __str__(self):
        return '\n'.join([' '.join([str(cell) for cell in row]) for row in self.grid])

    def depth_first_search(self):
        stack = []

        #for i in range (len(self.grid[0])-1):
        #    if stack[0][i] == 1:
        #        stack.append(2)
        
        for i in range(len(self.grid[0])):
            if self.grid[0][i] == 1 :
                self.grid[0][i] = 2 
                stack.append(Cell(0,i))
         


        while len(stack) > 0:
            self.draw()
            dudraw.show(10)
            current = stack.pop()
            if current.row == self.height-1:
                return True

            if current.col > 0 and self.grid[current.row][current.col-1] == 1:
                stack.append(Cell(current.row, current.col-1))
                self.grid[current.row][current.col-1] = 2
            if current.col < len(self.grid[0])-1 and self.grid[current.row][current.col+1] == 1:
                stack.append(Cell(current.row, current.col+1))
                self.grid[current.row][current.col+1] = 2
            if current.row > 0 and self.grid[current.row-1][current.col] == 1:
                stack.append(Cell(current.row-1, current.col))
                self.grid[current.row-1][current.col] = 2
            if current.row < len(self.grid)-1 and self.grid[current.row+1][current.col] == 1:
                stack.append(Cell(current.row+1, current.col))
                self.grid[current.row+1][current.col] = 2
        #return False
            #if current.row > 0 and self.grid[current.row][current.col] == 1:
            #    self.grid[current.row][current.col-1] = 2
            #    return True
            #if current.col > 0 and self.grid[current.row][current.col-1] == 1:
            #    stack.append(Cell(current.row, current.col-1))
            #    self.grid[current.row][current.col-1] = 2
            #if current.col < len(self.grid[0])-1  and self.grid[current.row][current.col+1] == 1:
            #    stack.append(Cell(current.row, current.col+1))
            #    self.grid[current.row][current.col-1] = 2
            #if current.row > 0 and self.grid[current.row-1][current.col] == 1:
            #    stack.append(Cell(current.row-1, current.col))
            #    self.grid[current.row][current.col-1] = 2
            #if current.row < len(self.grid[0])-1 and self.grid[current.row+1][current.col] == 1:
            #    stack.append(Cell(current.row+1, current.col))
            #    self.grid[current.row][current.col-1] = 2
    

    def breadth_first_search(self):
        start = Cell(0, 0)
        visited = set()
        queue = [start]
        while len(queue) > 0 :
            current = queue.pop(0)
            if current in visited:
                continue
            visited.add(current)
            row, col = current.row, current.col
            if row == self.height - 1 and self.grid[row][col] == 0:
                return True
            if col > 0 and self.grid[row][col-1] == 1:
                queue.append(Cell(row, col-1))
            if col < self.width - 1 and self.grid[row][col+1] == 1:
                queue.append(Cell(row, col+1))
            if row > 0 and self.grid[row-1][col] == 1:
                queue.append(Cell(row-1, col))
            if row < self.height - 1 and self.grid[row+1][col] == 2:
                queue.append(Cell(row+1, col))
        return False

    def draw(self):
        for i in range(len(self.grid[0])):
            for j in range(len(self.grid)):
                if self.grid[j][i] == 0:
                    dudraw.set_pen_color(dudraw.BLACK)

                if self.grid[j][i] == 1:
                    dudraw.set_pen_color(dudraw.GREEN)

                if self.grid[j][i] == 2:
                    dudraw.set_pen_color(dudraw.RED)
                
                dudraw.filled_square(i+0.5, j+0.5, 0.6)



# create a 10x10 forest with density 0.75
forest = Forest(20, 20, 0.75)
forest.draw()

print(forest.depth_first_search())
#print(forest.breadth_first_search())

## perform depth-first search
#if forest.depth_first_search():

#    print("Fire spread using depth-first search")
#else:
#    print("Fire did not spread using depth-first search")

## perform breadth-first search
#if forest.breadth_first_search():
#    print("Fire spread using breadth-first search")
#else:
#    print("Fire did not spread using breadth-first search")

dudraw.show(float('inf'))


#what am i going to do


