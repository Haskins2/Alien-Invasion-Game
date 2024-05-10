import sys
import pygame
from settings import Settings

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Alien Invasion")

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))


    def run_game(self):
        """Contains game logic"""
        while True:
            # Watch for keyboard & mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Render most recently drawn screen
            pygame.display.flip()
            self.screen.fill(self.settings.bg_color);

            # Set game framerate to 120hz
            self.clock.tick(self.settings.framerate)

if __name__ == "__main__":
    # Make a game instance & run the game
    ai = AlienInvasion()
    ai.run_game()