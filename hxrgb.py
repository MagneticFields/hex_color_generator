class Rgb():

    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b
        self.h_red = None
        self.h_green = None
        self.h_blue = None
    
    def convert(self):
       self.h_red = hex(self.red)
       self.h_green = hex(self.green)
       self.h_blue = hex(self.blue) 

       return f"#{self.h_red[2:]}{self.h_green[2:]}{self.h_blue[2:]}"

    def __str__(self):
        return self.convert()

def color_randomizer():
    import random
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    print(Rgb(r,g,b))

