# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from import constants *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

if __name__ == "__main__":
    main()

