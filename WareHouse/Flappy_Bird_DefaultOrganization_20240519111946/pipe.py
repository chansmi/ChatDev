'''
This file contains the Pipe class which represents the obstacles in the game.
'''
import pygame
import random
class Pipe:
    def __init__(self, screen_width):
        self.screen_width = screen_width
        self.x = screen_width
        self.gap = 200
        self.top_height = random.randint(50, 300)
        self.bottom_height = self.screen_width - self.top_height - self.gap
        self.speed = 5
    def update(self):
        self.x -= self.speed
    def render(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, 0, 50, self.top_height))
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.screen_width - self.bottom_height, 50, self.bottom_height))
    def collides_with_bird(self, bird):
        if bird.x + 20 > self.x and bird.x - 20 < self.x + 50:
            if bird.y - 20 < self.top_height or bird.y + 20 > self.screen_width - self.bottom_height:
                return True
        return False
    def passed_bird(self, bird):
        if bird.x > self.x + 50:
            return True
        return False