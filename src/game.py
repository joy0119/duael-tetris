from venv import create
import pygame, sys, random
from configs import *
from bloco import Grid, Peca
from tabuleiro import Tabuleiro

class Jooj:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()
		self.tabuleiro = Tabuleiro(self.display_surface)
		self.peca = self.create_peca()

	def show(self):
		self.display_surface.fill('black')
		self.tabuleiro.desenhar()
		self.peca.spawn()
		self.peca.desenhar(self.display_surface, (0,255,0))

	def player_input(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_k:
					self.create_peca()

	def create_peca(self):
		tipo = random.choice(['j','l','i','z','s','o'])
		return Peca(tipo)

	def run(self):
		self.player_input()
		self.show()