'''
This file contains the Game class which manages the game logic and rendering.
'''
import pygame
from bird import Bird
from pipe import Pipe
class Game:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.bird = Bird(self.screen_width, self.screen_height)
        self.pipes = [Pipe(self.screen_width)]
        self.score = 0
        self.font = pygame.font.Font(None, 36)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.jump()
    def update(self):
        self.bird.update()
        for pipe in self.pipes:
            pipe.update()
            if pipe.collides_with_bird(self.bird) or self.bird.y < 0 or self.bird.y > self.screen_height:
                self.game_over()
            if pipe.passed_bird(self.bird):
                self.score += 1
        if self.bird.y > self.screen_height:
            self.game_over()
    def render(self):
        self.screen.fill((0, 0, 0))
        self.bird.render(self.screen)
        for pipe in self.pipes:
            pipe.render(self.screen)
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        pygame.display.update()
    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)
    def game_over(self):
        # Game over logic
        pygame.quit()
        quit()