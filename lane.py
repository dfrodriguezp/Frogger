from rectangle import *
from obstacle import *
from params import *
import numpy
import pygame
pygame.init()

class Lane(Rectangle):
    def __init__(self, t, y, n, size, speed, spacing, laneColor=black, oColor=grey):
        Rectangle.__init__(self, 0, y, width, grid)
        self.color = laneColor
        self.obstacles = [None for i in range(n)]
        self.type = t

        offset = numpy.random.randint(0, 200)
        for i in range(n):
            self.obstacles[i] = Obstacle(offset + spacing * i, y, grid*size, grid, speed, oColor)

    def run(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))
        for o in self.obstacles:
            o.show(screen)
            o.update()

    def check(self, frog):
        if self.type == CAR:
            for o in self.obstacles:
                if frog.intersects(o):
                    resetGame(frog)
        
        elif self.type == LOG:
            ok = False
            for o in self.obstacles:
                if frog.intersects(o):
                    ok = True
                    frog.attach(o)
            if not ok:
                resetGame(frog)
