class Settings():
    """ a class to store all settings for Py eating snake."""

    def __init__(self):
        """Initialize the game's settings. """
        # Screen Settings
        self.screen_width =500
        self.screen_height = 500
        self.bg_color = (230, 230, 230)

        # Snake settings
        self.snake_width = 10
        self.snake_height = 10
        self.space_snake_members = 42
        self.snake_color = 60, 60, 60
        self.snake_speed_factor = 11

        # Food settings
        self.food_width = 10
        self.food_height = 10
        self.space_food_members = 42
        self.food_color = (255, 000, 000)
        self.food_speed_factor = 20
