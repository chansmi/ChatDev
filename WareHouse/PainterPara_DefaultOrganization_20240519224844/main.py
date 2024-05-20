import tkinter as tk
from canvas import Canvas
from brush import Brush
from color_picker import ColorPicker
class PaintingStudioApp:
    def __init__(self, root):
        self.root = root
        self.canvas = Canvas(root)
        self.brush = Brush(root, self.canvas)
        self.color_picker = ColorPicker(root, self.brush)
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    root = tk.Tk()
    app = PaintingStudioApp(root)
    app.run()