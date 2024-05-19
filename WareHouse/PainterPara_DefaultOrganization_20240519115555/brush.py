'''
Brush class to select different brushes
'''
import tkinter as tk
class Brush(tk.Frame):
    def __init__(self, root, canvas):
        super().__init__(root)
        self.canvas = canvas
        self.brushes = ["Pencil", "Marker", "Eraser"]
        self.selected_brush = tk.StringVar()
        self.selected_brush.set(self.brushes[0])
        self.brush_label = tk.Label(self, text="Brush:")
        self.brush_option = tk.OptionMenu(self, self.selected_brush, *self.brushes, command=self.draw)
        self.brush_label.pack(side=tk.LEFT)
        self.brush_option.pack(side=tk.LEFT)
    def draw(self, *args):
        brush = self.selected_brush.get()
        self.canvas.set_brush(brush)
        # Add any additional logic or actions related to brush selection if needed