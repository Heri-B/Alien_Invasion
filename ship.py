import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game, start_position="left"):
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/ship.bmp')

        if start_position == "left":
            self.image = pygame.transform.rotate(self.image, 270)

        self.rect = self.image.get_rect()

        self.screen_rect = self.screen.get_rect()

        if start_position == "left":
            self.rect.midleft = self.screen_rect.midleft

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
