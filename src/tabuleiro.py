from bloco import Bloco
import pygame
from configs import *

class Tabuleiro:
	def __init__(self, surface):
		self.display_surface = surface
		self.matriz = tabuleiro
		self.rect = pygame.Rect((50,50),(TAM_CELULA * 10, TAM_CELULA * 20))

	def desenhar(self):
		pygame.draw.rect(self.display_surface, (0,200,0), self.rect, 5)
		for i in self.matriz:
			for _ in i:
				celula = Bloco((_,i)) 
				celula.desenhar(self.display_surface)