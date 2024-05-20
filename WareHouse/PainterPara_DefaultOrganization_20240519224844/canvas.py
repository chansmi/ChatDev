import tkinter as tk
class Canvas:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()
    def draw(self, x, y):
        # Implement the logic to draw on the canvas
        pass
    def clear(self):
        # Implement the logic to clear the canvas
        pass