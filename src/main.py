# Bibliotecas
import sys, pygame as pg
# Classes
import menu
pg.init()

# CONFIGS
RES = [1366, 768]
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

tittle = pg.font.Font('duael-tetris/assets/font/Alkalami-Regular.ttf', int(RES[0] / 18))
button = pg.font.Font('duael-tetris/assets/font/Alkalami-Regular.ttf', int(RES[0] / 24))

FONTS = [tittle, button]

# LOOP
if __name__ == "__main__":
	while True: # big loop
		for event in pg.event.get(): 
			if event.type == pg.QUIT: sys.exit()
		CLOCK.tick(60)
		menu.menu()