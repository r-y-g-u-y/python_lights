
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

    def getHex(self):
        return [hex(r), hex(g), hex(b)]
        
    def getHexAsStr(self):
        return "%s%s%s" %(hex(r)[2:], hex(g)[2:], hex(b)[2:])
    def __repr__(self):
        return (
            "red   = %d\n" +
            "green = %d\n" +
            "blue  = %d\n" % (r, g, b)
        )