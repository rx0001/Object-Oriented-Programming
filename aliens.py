#####
#The roadster class was created with help from Practical Exercise 6, and practical Exercise 9 from CS1527 Object Oriented Programming Course.
# Relevant files looked at to create this class include components.py from Practical 6 Pong Game.

import pygame
import random

pygame.font.init()
WHITE = (255, 255, 255)
WIDTH = 1200


class Roadster(pygame.sprite.Sprite):
    def __init__(self, screen, settings):
        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.image.load('media/roadster.png') # Load image of roadster
        self.rect = self.image.get_rect()

        self.rect.centerx = random.randint(700, settings.screen_width + 700) #Random posistion of roadster given.
        self.rect.centery = random.randint(200, 500) # Random Posistion of roadster given.



    def update(self):
        self.rect.x -= random.randrange(5, 8) # Moves the roadster to the left randomly.
        if self.rect.left<= (WIDTH / 20): #This code detects when the roadster has reached the end of the screen.
            self.rect.centerx = WIDTH #Reloads the roadster back to the right of the screen.
            self.rect.centery = random.randint(200, 500) # Random y - value.




       
        
    




  
   
            



 




