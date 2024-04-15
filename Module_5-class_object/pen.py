class Pen:
    pencolor = None
    def __init__(self, color):
        self.color = color
    
    def set_color(self, new_color):
        self.pencolor = new_color

    def what_color(self):
        return self.pencolor

matador = Pen('red')
matador.set_color("blue")
print(matador.what_color())