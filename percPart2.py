"""
    Filename: percolationP2.py
    Author:Jamie Olson
    Date:5/8/23
    Course:COMP 1353
    Assignment: Percolation  (part 2)
    Collaborators:n/a
    Internet Source:n/a
"""


import random
import matplotlib.pyplot as plt


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
        
        for i in range(len(self.grid[0])):
            if self.grid[0][i] == 1 :
                self.grid[0][i] = 2 
                stack.append(Cell(0,i))
         


        while len(stack) > 0:
            #self.draw()
            #dudraw.show(10)
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



class FireProbability:
    # probability of fire spreading using depth-first search
    def probability_of_fire_spread_dfs(density):
        fire_spread_count = 0
        for _ in range(1000):
            forest = Forest(20, 20, density)
            if forest.depth_first_search():
                fire_spread_count += 1
        return fire_spread_count / 1000

    # probability of fire spreading -- breadth-first 
    def probability_of_fire_spread_bfs(density):
        fire_spread_count = 0
        num_tests = 100  # Decrease the number of tests?? 

        for _ in range(num_tests):
            forest = Forest(20, 20, density)
            if forest.breadth_first_search():
                fire_spread_count += 1
        return fire_spread_count / num_tests

    # Find the highest density depth first 
    def highest_density_dfs():
        low_density = 0.0
        high_density = 1.0

        for _ in range(20):
            density = (high_density + low_density) / 2.0
            p = FireProbability.probability_of_fire_spread_dfs(density)
            if p < 0.5:
                low_density = density
            else:
                high_density = density
        
        return density

    # Find the highest density that results in fire spreading with less than 0.5 probability using breadth-first search
    def highest_density_bfs():
        low_density = 0.0
        high_density = 1.0

        for _ in range(20):
            density = (high_density + low_density) / 2.0
            p = FireProbability.probability_of_fire_spread_bfs(density)
            if p < 0.5:
                low_density = density
            else:
                high_density = density
        
        return density

# Testing the FireProbability class

print("Using depth_first_search:")
probability_dfs = FireProbability.probability_of_fire_spread_dfs(0.75)
print(f"The probability of fire spreading with density 0.75 using depth-first search: {probability_dfs}") #not sure if its broken or just takes literally forever to run but its not printing things 

print("\nUsing breadth_first_search:")
probability_bfs = FireProbability.probability_of_fire_spread_bfs(0.75)
print(f"The probability of fire spreading with density 0.75 using breadth-first search: {probability_bfs}")

print("\nHighest density using depth_first_search:")
highest_density_dfs = FireProbability.highest_density_dfs()
print(f"The highest density that results in fire spreading with less than 0.5 probability (DFS): {highest_density_dfs}")

print("\nHighest density using breadth_first_search:")
highest_density_bfs = FireProbability.highest_density_bfs()
print(f"The highest density that results in fire spreading with less than 0.5 probability (BFS): {highest_density_bfs}")




#matplotlib thingsss

# Create a list of density values to test
density_values = [i / 100 for i in range(1, 100)]

# Create empty lists to store the probability values
dfs_probabilities = []
bfs_probabilities = []

# Calculate probabilities for each density value using depth-first search and breadth-first search
for density in density_values:
    dfs_prob = FireProbability.probability_of_fire_spread_dfs(density)
    bfs_prob = FireProbability.probability_of_fire_spread_bfs(density)
    dfs_probabilities.append(dfs_prob)
    bfs_probabilities.append(bfs_prob)

# Plotting the graph
plt.plot(density_values, dfs_probabilities, label='Depth-First Search')
plt.plot(density_values, bfs_probabilities, label='Breadth-First Search')
plt.xlabel('Forest Density')
plt.ylabel('Probability of Fire Spread')
plt.title('Impact of Forest Density on Fire Spread Probability')
plt.legend()
plt.show() #this is so stinkyyyyy why no worky  :////
