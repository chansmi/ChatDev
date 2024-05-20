class Canvas:
    def __init__(self, width=800, height=600, background_color="white"):
        self.width = width
        self.height = height
        self.background_color = background_color
        self.layers = []
    def draw_pixel(self, x, y, color):
        # Implement drawing single pixel logic here
        pass
    def draw_line(self, x1, y1, x2, y2, color):
        # Implement drawing line logic here
        pass
    def draw_shape(self, shape, color):
        # Implement drawing shape logic here
        pass
    def clear_canvas(self):
        # Implement clearing canvas logic here
        pass
    def save_canvas(self, filename):
        # Implement saving canvas logic here
        pass
    def load_canvas(self, filename):
        # Implement loading canvas logic here
        pass