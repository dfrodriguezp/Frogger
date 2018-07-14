from rectangle import *
from frog import *
from lane import *
from params import *
import numpy
import sys
import pygame
pygame.init()

canvas = pygame.display.set_mode(size)
pygame.display.set_caption("Frogger")
clock = pygame.time.Clock()

frog = Frog((width - grid) * 0.5, height - grid, grid)

# Obstacles
nLanes = int(height / grid)
lanes = [None for i in range(nLanes)]
index = 0

lanes[0] = Lane(SAFETY, 0*grid, 0, 0, 0, 0, purple)
lanes[1] = Lane(LOG, 1*grid, 3, 3, 1.5, 300, oColor=brown)
lanes[2] = Lane(LOG, 2*grid, 2, 3, -3.5, 300, oColor=brown)
lanes[3] = Lane(LOG, 3*grid, 2, 5, 2, 300, oColor=brown)
lanes[4] = Lane(LOG, 4*grid, 3, 4, -2.5, 300, oColor=brown)
lanes[5] = Lane(SAFETY, 5*grid, 0, 0, 0, 0, purple)
lanes[6] = Lane(CAR, 6*grid, 3, 1, 2.5, 300)
lanes[7] = Lane(CAR, 7*grid, 3, 2, -2, 300)
lanes[8] = Lane(CAR, 8*grid, 2, 2, 3.5, 300)
lanes[9] = Lane(CAR, 9*grid, 3, 2, -1.5, 300)
lanes[10] = Lane(SAFETY, 10*grid, 0, 0, 0, 0, purple)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # UP
                if event.key == 273: 
                    frog.move(0, -1, grid)

                # DOWN
                elif event.key == 274:
                    frog.move(0, 1, grid)

                # RIGHT
                elif event.key == 275:
                    frog.move(1, 0, grid)

                # LEFT
                elif event.key == 276:
                    frog.move(-1, 0, grid)

        canvas.fill((0, 0, 0))
        for lane in lanes:
            lane.run(canvas)

        laneIndex = int(frog.y / grid)
        lanes[laneIndex].check(frog)
        frog.show(canvas)
        frog.update()
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()