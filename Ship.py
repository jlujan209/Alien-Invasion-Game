import pygame


class ship:
    """A class to manage the ship"""
   
    def __init__(self, ai_game):
        """Initialize the ship and its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()


        #load the ship image and get its rectangle
        self.image = pygame.image.load('ship1.png')
        self.rect = self.image.get_rect()


        #start each new ship at the bottom of the center at the screen
        self.rect.midbottom = self.screen_rect.midbottom


        #start a decimal value of the ship's horizontal position
        self.x = float(self.rect.x)


        #movement flags
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Update the ship's position based on the movement flags"""
        #update the ship's x value, not the rect. Make sure the ship will remain in the field of view of the screen.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed


        #update the rect from self x
        self.rect.x = self.x


    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image,self.rect)


    def center_ship(self):
        #Center the ship on the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)