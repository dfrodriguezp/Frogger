from rectangle import *
import pygame
pygame.init()

def constrain(val, minVal, maxVal):
    return min(maxVal, max(minVal, val))

class Frog(Rectangle):
    def __init__(self, x, y, w):
        Rectangle.__init__(self, x, y, w, w)
        self.attached = None

    def show(self, screen):
        pygame.draw.rect(screen, (0, 255, 50), (self.x, self.y, self.w, self.w))

    def move(self, xdir, ydir, grid):
        self.x += xdir * grid
        self.y += ydir * grid
    
    def attach(self, log):
        self.attached = log

    def update(self, screen):
        width = screen.get_size()[0]
        height = screen.get_size()[1]
        if not (self.attached == None):
            self.x += self.attached.speed
        self.x = constrain(self.x, 0, width-self.w)
        self.y = constrain(self.y, 0, height-self.w)


