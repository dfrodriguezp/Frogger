class Rectangle(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def intersects(self, other):
        left = self.x
        right = self.x + self.w
        top = self.y
        bottom = self.y + self.h

        oleft = other.x
        oright = other.x + other.w
        otop = other.y
        obottom = other.y + other.h

        return not (left >= oright or 
            right <= oleft or
            top >= obottom or
            bottom <= otop)
