import pygame, sys
from configs import *
from bloco import Bloco
from tabuleiro import Tabuleiro

class Jooj:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()
		self.tabuleiro = Tabuleiro(self.display_surface)

	def show(self):
		self.display_surface.fill('black')
		self.tabuleiro.desenhar()

	def player_input(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
