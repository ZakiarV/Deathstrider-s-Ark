import pygame
from LevelGeneration.level_generation import LevelGeneragtion


class GameLoop:
    def __init__(self):
        self.display_screen = pygame.display.set_mode((1200, 750))
        pygame.display.set_caption("Deathstrider's Ark")
        self.clock = pygame.time.Clock()
        self.level = LevelGeneragtion()

    def run(self):
        running = True
        while running:
            dt = self.clock.tick()/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.display_screen.fill('black')
            self.level.update(dt)
            pygame.display.flip()
            self.clock.tick(60)