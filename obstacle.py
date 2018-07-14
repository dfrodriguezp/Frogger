from rectangle import *
from params import *
import pygame
pygame.init()

class Obstacle(Rectangle):
    def __init__(self, x, y, w, h, speed, color):
        Rectangle.__init__(self, x, y, w, h)
        self.speed = speed
        self.color = color

    def update(self):
        self.x += self.speed
        if self.speed > 0 and self.x >= width:
            self.x = -self.w
        elif self.x < -self.w:
            self.x = width

    def show(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.w, self.h), 1)