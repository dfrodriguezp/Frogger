grid = 50
size = width, height = 750, 550
black = (0, 0, 0)
white = (255, 255, 255)
purple = (150, 0, 255)
green = (0, 255, 0)
river = (0, 80, 255)
brown = (134, 152, 2)
grey = (200, 200, 200)
SAFETY = 0
CAR = 1
LOG = 2

def resetGame(frog):
    frog.x = (width - grid) * 0.5
    frog.y = height - grid
    frog.w = grid

def constrain(val, minVal, maxVal):
    return min(maxVal, max(minVal, val))
