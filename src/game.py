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
		self.peca_pos = 0
		self.nivel = 1  # velocidade da peça

	def show(self):
		self.display_surface.fill('black')
		self.tabuleiro.desenhar()
		self.peca.desenhar(self.display_surface, (0,255,0))
		

	def player_input(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_k: self.peca = self.create_peca()
				if event.key == pygame.K_j: self.peca = self.create_peca_definido('j')
				if event.key == pygame.K_l: self.peca = self.create_peca_definido('l')
				if event.key == pygame.K_i: self.peca = self.create_peca_definido('i')
				if event.key == pygame.K_z: self.peca = self.create_peca_definido('z')
				if event.key == pygame.K_s: self.peca = self.create_peca_definido('s')
				if event.key == pygame.K_o: self.peca = self.create_peca_definido('o')
				if event.key == pygame.K_LEFT: 
					self.peca.move_esq()
					self.show()
				if event.key == pygame.K_RIGHT: 
					self.peca.move_dir()
					self.show()
				if event.key == pygame.K_UP: 
					self.peca.girar()
					self.show()
				

	def create_peca(self):
		tipo = random.choice(['j','l','i','z','s','o'])
		return Peca(tipo)
	
	def create_peca_definido(self, tipo):
		return Peca(tipo)
	
	def run(self):
		self.peca.spawn()
		if pygame.time.get_ticks() % 1000 == self.nivel:
			for i in range(self.nivel): 
				self.peca.gravidade()
				self.show()
		self.player_input()
		self.show()