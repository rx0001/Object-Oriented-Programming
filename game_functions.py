import sys
import pygame
from bitcoin import Bitcoin


pygame.font.init() 


def update_screen(ai_settings, screen, wall, Ship,bitcoins, enemy_sprites, bitcoin_sprites):

    """Update sprites & messages on the screen.""" 



    wall.blitmedia() #Blits wall to screen.
    Ship.blitmedia() # Blits ship to screen.
    Ship.damage_reading() # Shows the damage the Starship has occured in screen scoreboard.
    bitcoins.score_reading() # Shows the player scores reading.



    #Updating sprite groups

    enemy_sprites.update()
    bitcoin_sprites.update()


    
    # Update the background region.
    pygame.display.update()



        