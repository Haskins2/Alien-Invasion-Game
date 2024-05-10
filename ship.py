import pygame
from settings import Settings
class Ship:
    def __init__(self, ai_game):
        """Initialise the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = Settings()

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.speed = self.settings.ship_speed_factor

        # Load ship image
        self.image = pygame.image.load('Assets/AI_Spaceship.bmp')
        self.rect = self.image.get_rect()

        # Initial ship positioning
        self.rect.x = self.screen_rect.centerx
        self.rect.y = self.screen_rect.bottom - 150
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Update the ships movement based on movement flag"""
        if (self.moving_right and (self.rect.x < self.settings.fly_border['right'])):
            self.x += self.speed
        if (self.moving_left and (self.rect.x > self.settings.fly_border['left'])):
            self.x -= self.speed
        if (self.moving_up and (self.rect.y > self.settings.fly_border['top'])) :
            self.y -= self.speed
        if (self.moving_down and (self.rect.y < self.settings.fly_border['bottom'])):
            self.y += self.speed
        # Update rect object from self.x.
        self.rect.x = self.x
        self.rect.y = self.y
    def blitme(self):
        """Draw the ship on the screen"""
        self.screen.blit(self.image, self.rect)
