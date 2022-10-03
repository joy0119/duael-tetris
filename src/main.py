# Bibliotecas
import sys, pygame as pg
import webbrowser, os
import game

# Classes
import menu
pg.init()

# CONFIGS
RES = [1024, 640]
COR = (0,255,0)
CLOCK = pg.time.Clock()
TAM_CELL = RES[1] / 30
SCREEN = pg.display.set_mode((RES[0], RES[1]))

tabuleiro = [[0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0]]

tittle = pg.font.Font('assets/font/Alkalami-Regular.ttf', int(RES[0] / 18))
button = pg.font.Font('assets/font/Alkalami-Regular.ttf', int(RES[0] / 24))
chat = pg.font.Font('assets/font/LemonTea.otf', int(RES[1] / 45))
FONTS = [tittle, button, chat]

#abrir arquivo txt
# arq = open("tutorial.txt")

# LOOP
if __name__ == "__main__":
	while True: # big loop
		CLOCK.tick(60)
		decisao = menu.menu()
		if decisao == 'solo': pass #game.solo()
		elif decisao == 'mult': game.mult()
		# elif decisao == 'help': print(arq.readlines())