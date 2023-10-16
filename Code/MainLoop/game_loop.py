import pygame


class GameLoop:
    def __init__(self):
        self.display_screen = pygame.display.set_mode((1200, 750))
        pygame.display.set_caption("Deathstrider's Ark")
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.display_screen.fill('black')
            pygame.display.flip()