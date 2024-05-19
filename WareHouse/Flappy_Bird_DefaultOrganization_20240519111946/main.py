'''
This is the main file of the Flappy Bird game. It initializes the game and starts the game loop.
'''
import pygame
from game import Game
from bird import Bird
from pipe import Pipe
def main():
    pygame.init()
    game = Game()
    game.run()
if __name__ == "__main__":
    main()