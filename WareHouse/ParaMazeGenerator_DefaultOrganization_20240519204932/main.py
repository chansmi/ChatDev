import tkinter as tk
from maze_generator import MazeGenerator
class MazeGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Generator")
        self.width_label = tk.Label(root, text="Width:")
        self.width_label.pack()
        self.width_entry = tk.Entry(root)
        self.width_entry.pack()
        self.height_label = tk.Label(root, text="Height:")
        self.height_label.pack()
        self.height_entry = tk.Entry(root)
        self.height_entry.pack()
        self.generate_button = tk.Button(root, text="Generate Maze", command=self.generate_maze)
        self.generate_button.pack()
        self.maze_canvas = tk.Canvas(root, width=500, height=500)
        self.maze_canvas.pack()
    def generate_maze(self):
        width = int(self.width_entry.get())
        height = int(self.height_entry.get())
        maze_generator = MazeGenerator(width, height)
        maze_generator.generate_maze()
        self.draw_maze(maze_generator.maze)
    def draw_maze(self, maze):
        self.maze_canvas.delete("all")
        cell_width = self.maze_canvas.winfo_width() // len(maze[0])
        cell_height = self.maze_canvas.winfo_height() // len(maze)
        for row in range(len(maze)):
            for col in range(len(maze[row])):
                x1 = col * cell_width
                y1 = row * cell_height
                x2 = (col + 1) * cell_width
                y2 = (row + 1) * cell_height
                if maze[row][col]:
                    self.maze_canvas.create_rectangle(x1, y1, x2, y2, fill="black")
def main():
    root = tk.Tk()
    maze_generator_gui = MazeGeneratorGUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()