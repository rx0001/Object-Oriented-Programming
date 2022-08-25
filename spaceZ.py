#The main game code was created with help from Practical Exercise 6, and practical Exercise 9 from CS1527 Object Oriented Programming Course.
# Relevant files looked at to create this class include pong.py from Practical 6 Pong Game and sprite-move.py from Practical 9, in which the collisions detection was looked at thoroughly and used/edited from.

import pygame
import sys
import random

# COMPLETE FILE PROVIDED IN STARTER CODE
from settings import Settings
# PARTIAL FILE PROVIDED IN STARTER CODE
import game_functions as gf
# IMPORT OTHER FILES/CLASSES HERE AS REQUIRED
from ship import my_ship, Background
from aliens import Roadster
from bitcoin import Bitcoin



def run_game():
	# Initialize pygame, settings and scrqeen object.
	pygame.init()
	# Set keys to repeat if held down.
	pygame.key.set_repeat(10,10)
	# Create settings object containing game settings
	ai_settings = Settings()
	# Create the main game screen
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	screen.blit(ai_settings.screen_backgrnd, [0, 0])
	# Create a main window caption
	pygame.display.set_caption("Space Z - Mars Flight")



	#Necessary Information
	damage_incured = 0
	lives = 3
	bitcoin_mining = 0
	player_score = 0
	ai_settings.lives = 3






	while ai_settings.lives > 0: 

		wall = Background(screen) #Creating Wall
		Ship = my_ship(screen, ai_settings, damage_incured, lives) #Creating Ship
		bitcoins = Bitcoin(screen, ai_settings, player_score, Ship) # Creating Bitcoin




		

		
		####Creating Sprite Groups
		enemy_sprites = pygame.sprite.Group()
		bitcoin_sprites = pygame.sprite.Group()

		

		

		for i in range(20): 
			roadster = Roadster(screen, ai_settings)
			enemy_sprites.add(roadster) #Creates 20 roadsters to the screen. 

		#Refresh the Background
		enemy_sprites.clear(screen, ai_settings.screen_backgrnd)
		bitcoin_sprites.clear(screen, ai_settings.screen_backgrnd)

		while Ship.damage_incured < 100:



			
			
			if bitcoin_mining < 100: # Watch for keyboard events.
				bitcoin_mining += 1 ## Adds 1 Bitcoin mine every time we pass through the main game loop.








			
			# Waatch for Keyboard Events.
			for event in pygame.event.get():  ## I have changed the posistion of the keyboard events from game_functions to main code because this allowed me to make my bitcoins and create them into the screen.
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN: ## This code is the exact same as the game_functions starting code, the posistion has been changed only. 
					if event.key == pygame.K_RIGHT:
						Ship.right() 
					elif event.key == pygame.K_LEFT:
						Ship.left()
					elif event.key == pygame.K_q:
						Ship.up()
					elif event.key == pygame.K_a:
						Ship.down()
					elif event.key == pygame.K_SPACE: ## New event key created to fire bitcoins if spacebar is pressed.

						if bitcoin_mining == 100: ## Fires bitcoin only if bitcoin mining reaches 100%.
							Bitcoin.bit_position(bitcoins, Ship) #This creates the bitcoins, bit_posistion is where the bitcoins will be positioned ie in front of the spaceship.
							bitcoin_sprites.add(bitcoins)
							bitcoin_mining = 0 ## Resets Bitcoin mining back to 0.




			# Now update the sprites, etc. on the screen
			gf.update_screen(ai_settings, screen, wall, Ship,bitcoins, enemy_sprites, bitcoin_sprites)


			spaceship_destroys = pygame.sprite.spritecollide(Ship, enemy_sprites, True) #This code detects collision between the ship and enemy roadster.
			bitcoin_destroys = pygame.sprite.spritecollide(bitcoins, enemy_sprites, True) # This code detects the collision between the bitcoin and enemy roadster. Help taken from practical 9 Ghost sprite collisons to create collision.


			if spaceship_destroys: ## If there is a collision
				Ship.collision_with_roadster(screen) #All neccesary requirements fullfilled with this method.
				roadster_x = Roadster(screen, ai_settings) ## Creates a new roadster when, collision has been detected.
				enemy_sprites.add(roadster_x) ## Adds to group.

			if bitcoin_destroys:
				Bitcoin.collision_roadster_bitcoin(bitcoins)
				bitcoin_sprites.remove(bitcoins)## Removes the bitcoin from screen when roadster and bitcoin collides. 






			if ai_settings.lives == 3:
				wall.lives_remaining_3(screen) ## Shows lives remaining on screen.

			if ai_settings.lives == 2:
				wall.lives_remaining_2(screen) # Shows lives remaining on screen.

			if ai_settings.lives == 1:
				wall.lives_remaining_1(screen) #Shows lives remaining on screen.		

			if ai_settings.lives == 0:
				pygame.quit()	


			#Draw Sprites to screen.
			enemy_sprites.draw(screen)
			bitcoin_sprites.draw(screen) # Help taken from practical 6 and 9 pong game and sprites.py to draw to screen.  
		

			pygame.display.update()

		null_event = pygame.event.wait()
		ai_settings.lives -=1

run_game()			
## Just a Note
#The bitcoin functionality works, the bitcoin is only released when bitcoin mining = 100, however i was unable to show this on the scorecard.

    

