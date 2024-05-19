'''
This file contains the Maze class which generates and stores the maze.
'''
import random
import tkinter as tk
class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0] * width for _ in range(height)]
        self.start_row = 0
        self.start_col = 0
        self.end_row = height - 1
        self.end_col = width - 1
    def generate(self):
        self._generate_maze_recursive(self.start_row, self.start_col)
    def _generate_maze_recursive(self, row, col):
        self.grid[row][col] = 1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            new_row = row + dx
            new_col = col + dy
            if self._is_valid(new_row, new_col) and self.grid[new_row][new_col] == 0:
                self.grid[row + dx // 2][col + dy // 2] = 1
                self._generate_maze_recursive(new_row, new_col)
    def _is_valid(self, row, col):
        return 0 <= row < self.height and 0 <= col < self.width