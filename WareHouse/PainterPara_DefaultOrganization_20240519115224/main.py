'''
This is the main file of the maze generation app.
'''
import tkinter as tk
from maze import Maze
class MazeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Maze Generation App")
        self.canvas = tk.Canvas(self.master, width=500, height=500)
        self.canvas.pack()
        self.generate_button = tk.Button(self.master, text="Generate Maze", command=self.generate_maze)
        self.generate_button.pack()
        self.maze = None
    def generate_maze(self):
        self.maze = Maze(10, 10)  # Change the dimensions as per your requirement
        self.maze.generate()
        self.draw_maze()
    def draw_maze(self):
        self.canvas.delete("all")
        cell_width = 500 / self.maze.width
        cell_height = 500 / self.maze.height
        for row in range(self.maze.height):
            for col in range(self.maze.width):
                x1 = col * cell_width
                y1 = row * cell_height
                x2 = x1 + cell_width
                y2 = y1 + cell_height
                if self.maze.grid[row][col] == 1:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")
        # Draw starting and ending points
        start_x = self.maze.start_col * cell_width
        start_y = self.maze.start_row * cell_height
        end_x = self.maze.end_col * cell_width
        end_y = self.maze.end_row * cell_height
        self.canvas.create_oval(start_x, start_y, start_x + cell_width, start_y + cell_height, fill="green")
        self.canvas.create_oval(end_x, end_y, end_x + cell_width, end_y + cell_height, fill="red")
if __name__ == "__main__":
    root = tk.Tk()
    app = MazeApp(root)
    root.mainloop()