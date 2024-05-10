class Settings:
    """A class to store all settings for the game"""

    def __init__(self):
        """Initialize the game's settings"""
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        self.framerate = 120
        self.ship_speed_factor = 1.5

        # Use a dictionary here? For code clarity
        self.fly_border = {
            'top': 400,
            'bottom' : self.screen_height - 50,
            'left' : 50,
            'right' : self.screen_width - 50
        }