import tkinter as tk
from tkinter.colorchooser import askcolor
class ColorPicker:
    def __init__(self, root, brush):
        self.brush = brush
        self.color_button = tk.Button(root, text="Pick Color", command=self.pick_color)
        self.color_button.pack()
    def pick_color(self):
        color = askcolor()
        if color:
            self.brush.change_color(color[1])