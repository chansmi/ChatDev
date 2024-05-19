'''
ColorSelector class to select different colors
'''
import tkinter as tk
class ColorSelector(tk.Frame):
    def __init__(self, root, canvas):
        super().__init__(root)
        self.canvas = canvas
        self.colors = ["Red", "Green", "Blue", "Yellow", "Black", "White"]
        self.selected_color = tk.StringVar()
        self.selected_color.set(self.colors[0])
        self.color_label = tk.Label(self, text="Color:")
        self.color_option = tk.OptionMenu(self, self.selected_color, *self.colors, command=self.draw)
        self.color_label.pack(side=tk.LEFT)
        self.color_option.pack(side=tk.LEFT)
    def draw(self, *args):
        color = self.selected_color.get()
        self.canvas.set_color(color)