#!/usr/local/bin/python3
import pygame
from pygame.locals import *

def main():
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255

    n = 5
    size = (32*n + 4, 32*n + 4)

    spaceHeight = 32
    spaceWidth = 32

    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("BitSweeper")
    clock = pygame.time.Clock()

    screen.fill(BLACK)

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        screen.fill(BLACK)

        pygame.display.flip()

        clock.tick(60)
    
    pygame.quit()

if __name__ == '__main__': main()

    

