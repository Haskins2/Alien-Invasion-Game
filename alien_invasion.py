import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Alien Invasion")

        self.screen = pygame.display.set_mode((
            self.settings.screen_width, self.settings.screen_height))

        self.ship = Ship(self)

    def _check_events(self):
        """Respond to user inputs"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # Checking for key presses
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_UP:
                    self.ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True

            ## Checking for key releases
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                elif event.key == pygame.K_UP:
                    self.ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False
                elif event.key == pygame.K_q:
                    sys.exit()

    def _update_screen(self):
        """Draw screen and update"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


    def run_game(self):
        """Contains game logic"""
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            self.clock.tick(self.settings.framerate)

    # Refactoring


if __name__ == "__main__":
    # Make a game instance & run the game
    ai = AlienInvasion()
    ai.run_game()

