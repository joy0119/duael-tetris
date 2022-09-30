# Bibliotecas
import sys, pygame as pg
# Classes
import buttons
pg.init()

# DEFINITIONS
RES = [1366, 768]
COR = (0,255,0)
CLOCK = pg.time.Clock()
QNTD_BOTOES = 2

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

screen = 'menu'

if __name__ == "__main__":
	select = ''
	botao_selecionado = 1  # Usado como referência para mapear qual o botão está sendo selecionado
	while 1:
		SCREEN.fill((0,0,0))
		if screen == 'menu':
			# Controle de eventos
			for event in pg.event.get(): 
				if event.type == pg.QUIT: sys.exit()

				# Controle dos comandos do menu
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_LEFT: botao_selecionado -= 1
					if event.key == pg.K_RIGHT: botao_selecionado += 1

			# Desenha o cursor de seleção
			if botao_selecionado == 1: pg.draw.rect(SCREEN, COR, solo_rect.inflate(int(RES[1] / 15.3),0), 5)
			if botao_selecionado == 2: pg.draw.rect(SCREEN, COR, dual_rect.inflate(int(RES[1] / 15.3),0), 5)
			if botao_selecionado > 2: botao_selecionado = 1
			elif botao_selecionado < 1: botao_selecionado = 2

			# Coloca os objetos na tela
			SCREEN.blit(titulo_surf, titulo_rect)
			SCREEN.blit(solo_surf, solo_rect)
			SCREEN.blit(dual_surf, dual_rect)

		pg.display.flip()
		CLOCK.tick(60)