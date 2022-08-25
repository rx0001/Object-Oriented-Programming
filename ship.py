#####
#This ship class was created with help from Practical Exercise 6, and practical Exercise 9 from CS1527 Object Oriented Programming Course.
# Relevant files looked at to create this class include components.py from Practical 6 Pong Game.

import pygame
import random
import sys


pygame.font.init()
WHITE = (255, 255, 255)
RED = (255, 0, 0) #### I was able to get this with the help of: https://www.pygame.org/docs/ref/color.html.





class my_ship(pygame.sprite.Sprite):
	def __init__(self, screen, settings, damage_incured, lives):
		pygame.sprite.Sprite.__init__(self)

		self.screen = screen
		self.damage_incured = 0
		self.lives = 3
		self.image = pygame.image.load('media/starship.png')
		self.rect = self.image.get_rect()

		self.center_classic = settings.screen_width # Posistion used for damage readings.

		self.top_classic = settings.screen_height # Posistion used for damage readings.
		self.rect.centerx = settings.screen_width - 1000 # This is the ships position 200 pixels away from the left edge.
		self.rect.top = settings.screen_height / 2 # This is the ships posistion at the center of the screen.
		
		self.font = pygame.font.SysFont('Comic Sans MS', 50) # Font used for you have crashed message
		self.fontx = pygame.font.SysFont('Comic Sans MS', 15) # Font used for damage radings.
		
		self.message_crashed = self.font.render('{}'.format('You Have Crashed!'), True, RED)

		self.boom_sound = pygame.mixer.Sound('media/boom.wav')
		
		self.message_00 = self.fontx.render('{}'.format('0%'), True, RED)  # These messages represent the amount of damage the spaceship incurs
		self.message_10 = self.fontx.render('{}'.format('10%'), True, RED) 
		self.message_20 = self.fontx.render('{}'.format('20%'), True, RED) 
		self.message_30 = self.fontx.render('{}'.format('30%'), True, RED) 
		self.message_40 = self.fontx.render('{}'.format('40%'), True, RED)
		self.message_50 = self.fontx.render('{}'.format('50%'), True, RED) 
		self.message_60 = self.fontx.render('{}'.format('60%'), True, RED) 
		self.message_70 = self.fontx.render('{}'.format('70%'), True, RED) 
		self.message_80 = self.fontx.render('{}'.format('80%'), True, RED)
		self.message_90 = self.fontx.render('{}'.format('90%'), True, RED) #These messages represent the amount of damage the spaceship incurs


			



	def left(self): #Moves the spaceship 5 pixels to the left.
		if self.rect.centerx > 70:  #Code taken and edited from practical 6 pong game components.py, the code looked at was for functions for moving the bat
			self.rect.centerx -= 5

	def right(self): #Moves the spaceship 5 pixels to the right.
		if self.rect.centerx <= 1130:  #Code taken and edited from practical 6 pong game components.py, the code looked at was for functions for moving the bat
			self.rect.centerx += 5		
		
	def up(self): # Moves the spacehip up 5 pixels.
		if self.rect.top >70:  #Code taken and edited from practical 6 pong game components.py, the code looked at was for functions for moving the bat
			self.rect.top -= 5


	def down(self): # Moves the spaceship down 5 pixels.
		if self.rect.top <=680: #Code taken and edited from practical 6 pong game components.py, the code looked at was for functions for moving the bat
			self.rect.top += 5


	

	def collision_with_roadster(self, screen): #This method is resposible for detecting the collision between the starship and roadster.

		self.damage_incured += 10 # When starship collides with the roadster it recieves +10 damage.
		self.boom_sound.play() ### Code was created using the help of: https://www.pygame.org/docs/ref/mixer.html, #This plays the explosion sound.

		if self.damage_incured >= 100: #When damages reaches 100, 1 life is lost, and the message appears on the screen.
			self.lives -= 1
			screen.blit(self.message_crashed, (self.center_classic - 800, self.top_classic / 2.1))
			return False



	def damage_reading(self): #This method is responisble for showing the amount of damage inflicted on the starship on the scoreboard. 
		if self.damage_incured == 0:
			self.screen.blit(self.message_00, (self.center_classic - 1100, self.top_classic / 55))

		elif self.damage_incured == 10:
			self.screen.blit(self.message_10, (self.center_classic - 1100, self.top_classic / 55 ))


		elif self.damage_incured == 20:
			self.screen.blit(self.message_20, (self.center_classic - 1100, self.top_classic / 55 ))

		elif self.damage_incured == 30:
			self.screen.blit(self.message_30, (self.center_classic - 1100, self.top_classic / 55 ))

		elif self.damage_incured == 40:
			self.screen.blit(self.message_40, (self.center_classic - 1100, self.top_classic / 55 ))
	
		elif self.damage_incured == 50:
			self.screen.blit(self.message_50, (self.center_classic - 1100, self.top_classic / 55 ))
		
		elif self.damage_incured == 60:
			self.screen.blit(self.message_60, (self.center_classic - 1100, self.top_classic / 55 ))
		
		elif self.damage_incured == 70:
			self.screen.blit(self.message_70, (self.center_classic - 1100, self.top_classic / 55 ))
		
		elif self.damage_incured == 80:
			self.screen.blit(self.message_80, (self.center_classic - 1100, self.top_classic / 55 ))
		
		elif self.damage_incured == 90:
			self.screen.blit(self.message_90, (self.center_classic - 1100, self.top_classic / 55 ))

	def blitmedia(self): # This method causes the starship to appear on the pygame screen.
		self.screen.blit(self.image, self.rect)    	


class Background(my_ship): #I have also created a class for my background, I have done this as it allows me to use the scoreboard in a manner that helps me to develop and complete my code.
	def __init__(self, screen):
		self.screen = screen
		
		self.media = pygame.image.load('media/mars_background.png')
		self.rect = self.media.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx
		self.rect.top = self.screen_rect.top

		self.font = pygame.font.SysFont('Comic Sans MS', 20)
		self.message_lives_3 = self.font.render('{}'.format('3'), True, RED)
		self.message_lives_2 = self.font.render('{}'.format('2'), True, RED)
		self.message_lives_1 = self.font.render('{}'.format('1'), True, RED)



	def lives_remaining_3(self, screen): ### These lines of code starting here: These lines of code represent the amount of lives the starship is on, and shows the number on the pygame screen. 
		screen.blit(self.message_lives_3,(self.rect.centerx - 350, self.rect.top + 5))

	def lives_remaining_2(self, screen):
		screen.blit(self.message_lives_2,(self.rect.centerx - 350, self.rect.top + 5))

	def lives_remaining_1(self, screen):
		screen.blit(self.message_lives_1,(self.rect.centerx - 350, self.rect.top + 5))# Ending here	

	def blitmedia(self):
		self.screen.blit(self.media, self.rect) ##Creates background and blits to screen. 










			

    	









        
 




