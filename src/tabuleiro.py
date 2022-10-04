from bloco import Grid
import pygame
from configs import *

class Tabuleiro:
	def __init__(self, surface):
		self.display_surface = surface
		self.matriz = tabuleiro
		self.rect = pygame.Rect(POS_TABULEIRO,(TAM_CELULA * 10, TAM_CELULA * 20))

	def desenhar(self):
		pygame.draw.rect(self.display_surface, (0,200,0), self.rect, 5)
		for i in range(len(self.matriz)):
			for j in range(len(self.matriz[0])):
				celula = Grid([j, i])
				if self.matriz[i][j] == '0':
					celula.desenhar(self.display_surface, (100,0,0))
				elif self.matriz[i][j] == '1':
					celula.desenhar(self.display_surface, (0,255,0))
				elif self.matriz[i][j] == '2':
					celula.desenhar(self.display_surface, (200,200,0))
