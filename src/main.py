# Bibliotecas
import sys, pygame as pg
# Classes
import buttons
pg.init()

# DEFINITIONS
RES = [1366, 768]
COR = (0,255,0)
CLOCK = pg.time.Clock()

#configs
SCREEN = pg.display.set_mode((RES[0], RES[1]))
font_t = pg.font.Font('duael-tetris/assets/font/Alkalami-Regular.ttf', int(RES[0] / 18))
font_b = pg.font.Font('duael-tetris/assets/font/Alkalami-Regular.ttf', int(RES[0] / 24))

posx_b_s = RES[0] / 3
posx_b_d = RES[0] - posx_b_s	# Mantém simetria com o outro botao
posy_b = RES[1] / 1.75

titulo_surf = font_t.render('DUÆL TETRIS', False, COR)
titulo_rect = titulo_surf.get_rect(center = (RES[0] / 2, RES[1] / 4))

solo_surf = font_b.render('SOLO', False, COR)
solo_rect = solo_surf.get_rect(center = (posx_b_s, posy_b))

dual_surf = font_b.render('DUAL', False, COR)
dual_rect = dual_surf.get_rect(center = (posx_b_d, posy_b))

title_screen = True

if __name__ == "__main__":
	select = ''
	while 1:
		SCREEN.fill((0,0,0))
		if title_screen:
			for event in pg.event.get(): 
				if event.type == pg.QUIT: sys.exit()
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_LEFT: select = '<'
					if event.key == pg.K_RIGHT: select = '>'
			if select == '<': pg.draw.rect(SCREEN, COR, solo_rect.inflate(50,0), 5)
			if select == '>': pg.draw.rect(SCREEN, COR, dual_rect.inflate(50,0), 5)

			SCREEN.blit(titulo_surf, titulo_rect)
			SCREEN.blit(solo_surf, solo_rect)
			SCREEN.blit(dual_surf, dual_rect)

		pg.display.flip()
		CLOCK.tick(60)