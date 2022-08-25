###
#####
#The bitcoin class was created with help from Practical Exercise 6, and practical Exercise 9 from CS1527 Object Oriented Programming Course.
#Relevant files looked at to create this class include components.py from Practical 6 Pong Game.


import random 
import pygame
from ship import my_ship

WIDTH = 1200
HEIGHT = 750
RED = (255, 0, 0) #### https://www.pygame.org/docs/ref/color.html
pygame.mixer.init()
pygame.font.init()


class Bitcoin(pygame.sprite.Sprite):
	def __init__(self, screen,settings, player_score, player):
		pygame.sprite.Sprite.__init__(self)

		self.screen = screen
		self.player_score = 0 ## Starting value of player score.

		self.center_classic = settings.screen_width ## This posistion is used for player score.

		self.top_classic = settings.screen_height # This posistion is used for player score.

		self.image = pygame.image.load('media/bitcoin.png')
		self.rect =  self.image.get_rect()

		self.bitcoin_sound = pygame.mixer.Sound('media/boom.wav') ## Help taken from https://www.pygame.org/docs/ to initizalise mixer and create sound.
		self.fontx = pygame.font.SysFont('Comic Sans MS', 15)


		self.rect.centerx = 0 #Starting posistion of bitcoin, this posistion is not used however, it is required.
		self.rect.top = 0 # Starting posistion of bitcoin, this posistion is not used however, it is required.

		self.message_00 = self.fontx.render('{}'.format('000'), True, RED)  # These messages represent the player score. 
		self.message_10 = self.fontx.render('{}'.format('010'), True, RED) 
		self.message_20 = self.fontx.render('{}'.format('020'), True, RED) 
		self.message_30 = self.fontx.render('{}'.format('030'), True, RED) 
		self.message_40 = self.fontx.render('{}'.format('040'), True, RED)
		self.message_50 = self.fontx.render('{}'.format('050'), True, RED) 
		self.message_60 = self.fontx.render('{}'.format('060'), True, RED) 
		self.message_70 = self.fontx.render('{}'.format('070'), True, RED) 
		self.message_80 = self.fontx.render('{}'.format('080'), True, RED)
		self.message_90 = self.fontx.render('{}'.format('090'), True, RED) 
		self.message_100 = self.fontx.render('{}'.format('100'), True, RED)
		self.message_110 = self.fontx.render('{}'.format('110'), True, RED)
		self.message_120 = self.fontx.render('{}'.format('120'), True, RED) # these messages represent the player score.


	def bit_position(self, player):
		self.rect.centerx = player.rect.centerx + 55 # This is the posistion we use to fire the bitcoin. the player represents the ship so the bitcoin will fire in front of the ship.
		self.rect.top = player.rect.top + 15	# This is the posistion we use to fire the bitcoin. the player represents the ship so the bitcoin will fire in front of the ship.


	def update(self):
		self.rect.x += 5 #Moves bitcoin to the right when fired. 


	def collision_roadster_bitcoin(self):

		self.player_score += 10 # When bitcoin collides with roadster the player score increases by 10.
		self.bitcoin_sound.play()  # When bitcoin collides with roadster the boom sound is played.



	def score_reading(self): #This method is responisble for showing the player score on scoreboard. 
		if self.player_score == 0:
			self.screen.blit(self.message_00, (self.center_classic - 1100, self.top_classic / 20))

		elif self.player_score == 10:
			self.screen.blit(self.message_10, (self.center_classic - 1100, self.top_classic / 20))	

		elif self.player_score == 20:
			self.screen.blit(self.message_20, (self.center_classic - 1100, self.top_classic / 20))	

		elif self.player_score == 30:
			self.screen.blit(self.message_30, (self.center_classic - 1100, self.top_classic / 20))	
			
		elif self.player_score == 40:
			self.screen.blit(self.message_40, (self.center_classic - 1100, self.top_classic / 20))	
			
		elif self.player_score == 50:
			self.screen.blit(self.message_50, (self.center_classic - 1100, self.top_classic / 20))

		elif self.player_score == 60:
			self.screen.blit(self.message_60, (self.center_classic - 1100, self.top_classic / 20))
		
		elif self.player_score == 70:
			self.screen.blit(self.message_70, (self.center_classic - 1100, self.top_classic / 20))
		
		elif self.player_score == 80:
			self.screen.blit(self.message_80, (self.center_classic - 1100, self.top_classic / 20))
		
		elif self.player_score == 90:
			self.screen.blit(self.message_90, (self.center_classic - 1100, self.top_classic / 20))
		
		elif self.player_score == 100:
			self.screen.blit(self.message_100, (self.center_classic - 1100, self.top_classic / 20))
		
		elif self.player_score == 110:
			self.screen.blit(self.message_110, (self.center_classic - 1100, self.top_classic / 20))
		
		elif self.player_score == 120:
			self.screen.blit(self.message_120, (self.center_classic - 1100, self.top_classic / 20))


		


