from rectangle import *
from params import *
import pygame
pygame.init()

class Frog(Rectangle):
    def __init__(self, x, y, w):
        Rectangle.__init__(self, x, y, w, w)
        self.attached = None

    def show(self, screen):
        pygame.draw.rect(screen, green, (self.x, self.y, self.w, self.w))

    def move(self, xdir, ydir, grid):
        self.x += xdir * grid
        self.y += ydir * grid
        self.attach(None)
    
    def attach(self, log):
        self.attached = log

    def update(self):
        if not (self.attached == None):
            self.x += self.attached.speed
        self.x = constrain(self.x, 0, width-self.w)
        self.y = constrain(self.y, 0, height-self.w)


