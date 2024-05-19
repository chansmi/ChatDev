'''
This file contains the Maze class which represents a maze.
'''
import random
class Maze:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = [[0] * columns for _ in range(rows)]
        self.generate_maze()
    def generate_maze(self):
        stack = [(0, 0)]
        visited = set()
        while stack:
            current_cell = stack[-1]
            visited.add(current_cell)
            neighbors = self.get_unvisited_neighbors(current_cell, visited)
            if neighbors:
                next_cell = random.choice(neighbors)
                self.remove_wall(current_cell, next_cell)
                stack.append(next_cell)
            else:
                stack.pop()
    def get_unvisited_neighbors(self, cell, visited):
        row, col = cell
        neighbors = []
        if row > 0 and (row - 1, col) not in visited:
            neighbors.append((row - 1, col))
        if row < self.rows - 1 and (row + 1, col) not in visited:
            neighbors.append((row + 1, col))
        if col > 0 and (row, col - 1) not in visited:
            neighbors.append((row, col - 1))
        if col < self.columns - 1 and (row, col + 1) not in visited:
            neighbors.append((row, col + 1))
        return neighbors
    def remove_wall(self, cell1, cell2):
        row1, col1 = cell1
        row2, col2 = cell2
        if row1 == row2:
            if col1 < col2:
                self.grid[row1][col1 + 1] = 1
            else:
                self.grid[row1][col1 - 1] = 1
        else:
            if row1 < row2:
                self.grid[row1 + 1][col1] = 1
            else:
                self.grid[row1 - 1][col1] = 1