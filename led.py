
class rgb:
    r = 0
    g = 0
    b = 0
    def __init__(self, red=0, green=0, blue=0):
        r = red
        g = green
        b = blue
    def get(self):
        return [r, g, b]
    def __repr__(self):
        return (
            "red   = %d\n" +
            "green = %d\n" +
            "blue  = %d\n" % (r, g, b)
        )