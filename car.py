from rectangle import *
import pygame
pygame.init()

class Car(Rectangle):
    def __init__(self, x, y, w, h, speed):
        Rectangle.__init__(self, x, y, w, h)
        self.speed = speed

    def update(self, screen):
        width = screen.get_size()[0]
        self.x += self.speed
        if self.speed > 0 and self.x >= width:
            self.x = -self.w
        elif self.x < -self.w:
            self.x = width

    def show(self, screen):
        pygame.draw.rect(screen, (200, 200, 200), (self.x, self.y, self.w, self.h))