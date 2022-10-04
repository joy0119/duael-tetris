import pygame
from configs import *

class Grid:
	def __init__(self, coordenadas):
		x = POS_TABULEIRO[0] + (coordenadas[0] * TAM_CELULA)
		y = POS_TABULEIRO[1] + (coordenadas[1] * TAM_CELULA)
		self.real_pos = (x, y)
		self.size = (TAM_CELULA, TAM_CELULA)
		self.rect = pygame.Rect(self.real_pos, self.size)

	def desenhar(self, screen, cor):
		pygame.draw.rect(screen, cor, self.rect, 1)

class Peca():
	def __init__(self, type):
		# j,l,o,z,s,i
		self.size = (TAM_CELULA,TAM_CELULA)
		self.type = type
		self.blocos = []
		for _ in range(4): self.blocos.append(Grid((5, 0)))
		self.gravity = 0


	def spawn(self):
		if self.type == 'i':
			self.blocos[0].rect.midright = self.blocos[1].rect.midleft
			self.blocos[2].rect.midleft = self.blocos[1].rect.midright
			self.blocos[3].rect.midleft = self.blocos[2].rect.midright
		elif self.type == 'j':
			self.blocos[0].rect.midright = self.blocos[1].rect.midleft
			self.blocos[2].rect.midbottom = self.blocos[1].rect.midtop
			self.blocos[3].rect.midbottom = self.blocos[2].rect.midtop
		elif self.type == 'l':
			self.blocos[0].rect.midleft = self.blocos[1].rect.midright
			self.blocos[1].rect.midtop = self.blocos[2].rect.midbottom
			self.blocos[3].rect.midbottom = self.blocos[2].rect.midtop
		elif self.type == 'o':
			self.blocos[0].rect.midright = self.blocos[1].rect.midleft
			self.blocos[2].rect.midtop = self.blocos[0].rect.midbottom
			self.blocos[3].rect.midleft = self.blocos[2].rect.midright
		elif self.type == 's':
			self.blocos[0].rect.midleft = self.blocos[1].rect.midright
			self.blocos[1].rect.midbottom = self.blocos[2].rect.midtop
			self.blocos[3].rect.midright = self.blocos[2].rect.midleft
		elif self.type == 'z':
			self.blocos[0].rect.midright = self.blocos[1].rect.midleft
			self.blocos[2].rect.midtop = self.blocos[1].rect.midbottom
			self.blocos[3].rect.midleft = self.blocos[2].rect.midright

	def desenhar(self, screen, cor):
		for bloco in self.blocos: bloco.desenhar(screen, cor)
