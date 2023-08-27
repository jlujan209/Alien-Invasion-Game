class settings:
    """A class to store all settings for Alien Invasion"""


    def __init__(self):
        """Intializs the game settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,51,102)
        self.hit_screen_color = (236,62,62)


        #ship settings
        self.ship_speed = 4
        self.ship_limit = 3


        #Bullet settings - dark gray bullets that are 3 pixels wide and 15 pixels high. Bullets travel slower than the ship
        self.bullet_speed = 2
        self.bullet_width = 6
        self.bullet_height = 20
        self.bullet_color = (255,0,0)
        self.bullets_allowed = 3




        self.alien_speed = 1.0
        self.fleet_drop_speed = 10


        self.fleet_direction = 1
