from rectangle import *
from frog import *
from car import *
from log import *
import sys
import pygame
pygame.init()

def resetGame(frog):
    frog.x = (width - grid) * 0.5
    frog.y = height - grid
    frog.w = grid

grid = 50

size = width, height = 850, 450
canvas = pygame.display.set_mode(size)
pygame.display.set_caption("Frogger")
clock = pygame.time.Clock()

frog = Frog((width - grid) * 0.5, height - grid, grid)

# Cars
nCars = 10
cars = [None for i in range(nCars)]
index = 0

# Row 2
for i in range(3):
    x = i * 300
    cars[index] = Car(x, height - grid*2, grid * 2, grid, 2)
    index += 1

# Row 3
for i in range(3):
    x = i * 300
    cars[index] = Car(x, height - grid*3, grid, grid, -3.5)
    index += 1

# Row 4
for i in range(4):
    x = i * 200 + 150
    cars[index] = Car(x, height - grid*4, grid, grid, 2.5)
    index += 1

# Logs
nLogs = 8
logs = [None for i in range(nLogs)]
index = 0

# Row 6
for i in range(2):
    x = i * 500 + 150
    logs[index] = Log(x, height - grid*6, grid*3, grid, 2.5)
    index += 1

# Row 7
for i in range(3):
    x = i * 250 + 200
    logs[index] = Log(x, height - grid*7, grid*1.5, grid, -3.5)
    index += 1

# Row 8
for i in range(3):
    x = i * 500 + 300
    logs[index] = Log(x, height - grid*8, grid*5, grid, 1.2)
    index += 1

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
        pygame.draw.rect(canvas, (104, 0, 170), (0, height-grid, width, grid)) # Row 1
        pygame.draw.rect(canvas, (104, 0, 170), (0, height-grid*5, width, grid)) # Row 5
        pygame.draw.rect(canvas, (152, 116, 0), (0, height-grid*9, width, grid)) # Row 5
        
        for car in cars:
            car.show(canvas)
            car.update(canvas)
            if frog.intersects(car):
                resetGame(frog)
        for log in logs:
            log.show(canvas)
            log.update(canvas)

        if frog.y < height-grid*5 and frog.y >= height-grid*8:
            ok = False
            for log in logs:
                if frog.intersects(log):
                    ok = True
                    frog.attach(log)
            if not ok:
                resetGame(frog)

        else:
            frog.attach(None)
        frog.show(canvas)
        frog.update(canvas)
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()