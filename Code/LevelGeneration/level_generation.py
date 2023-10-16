import pygame
from ..Characters.Player.player import Player


class LevelGeneragtion:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.player_sprite = pygame.sprite.GroupSingle()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.setup()

    def setup(self):
        self.player = Player((600, 375), [self.player_sprite, self.visible_sprites])

    def update(self, dt):
        self.display_surface.fill('black')
        self.visible_sprites.update(dt)
        self.visible_sprites.draw(self.display_surface)