'''
Canvas class to create a digital canvas
'''
import tkinter as tk
class Canvas(tk.Canvas):
    def __init__(self, root):
        super().__init__(root, bg="white", width=800, height=600)
        self.bind("<B1-Motion>", self.draw)
        self.brush = 1
        self.color = "black"
    def draw(self, event):
        x, y = event.x, event.y
        brush = self.get_brush()
        color = self.get_color()
        self.create_oval(x-5, y-5, x+5, y+5, fill=color, outline=color, width=brush)
    def set_brush(self, brush):
        self.brush = brush
    def get_brush(self):
        return self.brush
    def set_color(self, color):
        self.color = color
    def get_color(self):
        return self.color