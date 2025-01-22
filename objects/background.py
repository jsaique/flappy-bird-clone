import pygame.sprite

import assets


class Background(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self.image = assets.get_sprites("background")
        self.rect = self.image.get_rect(topleft=(0, 0))

        super().__init__(*groups)

    def update(self):
        self.rect.x -= 1
