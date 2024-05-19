'''
Virtual Painting Studio Application
'''
import tkinter as tk
from canvas import Canvas
from brush import Brush
from color import ColorSelector
class PaintingStudioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Painting Studio")
        self.canvas = Canvas(self.root)
        self.brush = Brush(self.root, self.canvas)
        self.color = ColorSelector(self.root, self.canvas)
        self.canvas.pack()
        self.brush.pack()
        self.color.pack()
if __name__ == "__main__":
    root = tk.Tk()
    app = PaintingStudioApp(root)
    root.mainloop()