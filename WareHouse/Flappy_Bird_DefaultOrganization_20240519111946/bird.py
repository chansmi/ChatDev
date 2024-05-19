'''
This file contains the Bird class which represents the player-controlled bird.
'''
import pygame
class Bird:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = 100
        self.y = screen_height // 2
        self.velocity = 0
        self.gravity = 0.5
    def jump(self):
        self.velocity = -10
    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity
        if self.y < 0:
            self.y = 0
        elif self.y > self.screen_height:
            self.y = self.screen_height
    def render(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, int(self.y)), 20)