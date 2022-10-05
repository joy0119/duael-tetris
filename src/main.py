import pygame, sys
from configs import *
from game import Jooj

class Menu:
	def __init__(self):
		self.display_surface = pygame.display.get_surface()

		# FONTES e renderização
		button_font = pygame.font.Font(MENU_FONT, BUTTON_FONT_SIZE)
		title_font = pygame.font.Font(MENU_FONT, TITLE_FONT_SIZE)
		self.title = title_font.render('DUÆL TETRIS', False, (0,255,0))
		self.title_rect = self.title.get_rect(center = (int(WIDTH / 2), int(HEIGHT / 4)))
		
		self.solo = button_font.render('SOLO', False, (0,255,0))
		self.solo_rect = self.solo.get_rect(center = (int(WIDTH / 3), int(HEIGHT / 1.75)))

		self.mult = button_font.render('MULT', False, (0,255,0))
		self.mult_rect = self.mult.get_rect(center = ((WIDTH - int(WIDTH / 3), int(HEIGHT / 1.75))))

		self.help = button_font.render('?', False, (0,255,0))
		self.help_rect = self.help.get_rect(center = (WIDTH - 50, HEIGHT - 50))

		self.selecionado = 1

	def show(self):
		self.display_surface.fill('black')
		self.display_surface.blit(self.title, self.title_rect)
		self.display_surface.blit(self.solo, self.solo_rect)
		self.display_surface.blit(self.mult, self.mult_rect)
		self.display_surface.blit(self.help, self.help_rect)
		if self.selecionado == 1: pygame.draw.rect(self.display_surface, (0,255,0), self.solo_rect.inflate(int(HEIGHT/15),0), 5)
		elif self.selecionado ==  2: pygame.draw.rect(self.display_surface, (0,255,0), self.mult_rect.inflate(int(HEIGHT/15),0), 5)
		elif self.selecionado == 3: pygame.draw.rect(self.display_surface, (0,255,0), self.help_rect.inflate(int(HEIGHT/15),0), 5)

	def selec_input(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT: self.selecionado -= 1
				if event.key == pygame.K_RIGHT: self.selecionado += 1
				#if event.key == pygame.K_SPACE and self.selecionado == 3: return 'help'

	def run(self):
		if self.selecionado < 1: self.selecionado = 3
		if self.selecionado > 3: self.selecionado = 1

		self.show()
		return self.selec_input()

class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		self.clock = pygame.time.Clock()
		self.menu = Menu()
		self.jooj = Jooj()
		self.tela = 'game'

	def run(self):
		self.clock.tick(FPS)
		while True:
			self.screen.fill('black')
			if self.tela == 'menu': self.menu.run()
			elif self.tela == 'game': self.jooj.run()
			pygame.display.update()

if __name__ == '__main__':
	game = Game()
	game.run()