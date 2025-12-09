import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = ai_game.screen.get_rect()

        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False 
        self.moving_right = False 

    def update(self):
        """Update the ship's position."""

        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)