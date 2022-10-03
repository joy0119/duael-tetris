import pygame
from configs import *

class Bloco:
	def __init__(self, coordenadas: tuple):
		self.coordenadas = tuple(TAM_CELULA * elem for elem in coordenadas)
		# self.rect = pygame.Rect((TAM_CELULA * coordenadas[0],TAM_CELULA * coordenadas[1]),(TAM_CELULA,TAM_CELULA))  # quebrado
		# self.rect = pygame.Rect((10,10),(10,10))
	def desenhar(self, screen):
		pygame.draw.rect(screen, (0,255,0), ((self.coordenadas),(TAM_CELULA, TAM_CELULA)), 5)
