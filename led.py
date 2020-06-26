
class rgb:
    r = 0
    g = 0
    b = 0
    def __init__(self, red=0, green=0, blue=0):
        self.r = int(round(red))
        self.g = int(round(green))
        self.b = int(round(blue))
        if(self.r == 256):
            self.r -= 1
        if(self.g == 256):
            self.g -= 1
        if(self.b == 256):
            self.b -= 1
        
    def get(self):
        return [self.r, self.g, self.b]

    def getHex(self):
        return [hex(self.r), hex(self.g), hex(self.b)]
        
    def getHexAsStr(self):
        return "%s%s%s" %(hex(self.r)[2:].zfill(2), hex(self.g)[2:].zfill(2), hex(self.b)[2:].zfill(2))
    def __repr__(self):
        return (
            "red   = %d\ngreen = %d\nblue  = %d\n" % (self.r, self.g, self.b)
        )