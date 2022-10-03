#from classes import Botao
from msilib.schema import Font
import classes
#from main import RES, SCREEN, pg
import main

def menu():
	posx_b_s = main.RES[0] / 3
	posx_b_d = main.RES[0] - posx_b_s	# Mantém simetria com o outro botao
	posy_b = main.RES[1] / 1.75

	botao_selecionado = 1  # Usado como referência para mapear qual o botão está sendo selecionado
	solo = classes.Botao('SOLO', (posx_b_s, posy_b))
	mult = classes.Botao('MULT', (posx_b_d, posy_b))
	help = classes.Botao('?', (main.RES[0] / 1.2, main.RES[1] / 30))

	# COLOCAR OS GRUPOS
	botoes = [solo, mult, help]
	botao_group = main.pg.sprite.Group()
	for botao in botoes: botao_group.add(botao)
	
	title = main.FONTS[1].render("DUÆL TETRIS", False, main.COR)
	title_rect = title.get_rect(center = (main.RES[0]/2, main.RES[1]/4))

	MIN_B = 1
	MAX_B = 3

	while True:
		for event in main.pg.event.get(): 
			if event.type == main.pg.QUIT: main.sys.exit()
			if event.type == main.pg.KEYDOWN:
				if event.key == main.pg.K_LEFT: botao_selecionado += 1
				elif event.key == main.pg.K_RIGHT: botao_selecionado -= 1
				elif event.key == main.pg.K_SPACE and botao_selecionado == 1: return 'solo'  # leva para o jogo solo
				elif event.key == main.pg.K_SPACE and botao_selecionado == 2: return 'mult'  # leva para a tela de conexão
				elif event.key == main.pg.K_SPACE and botao_selecionado == 3: return 'help'  # leva para uma pagina html

		main.SCREEN.fill((0,0,0))

		# # Desenha o cursor de seleção
		if botao_selecionado == 1: main.pg.draw.rect(main.SCREEN, main.COR, botoes[0].rect.inflate(int(main.RES[1] / 15.3),0), 5)
		elif botao_selecionado == 2: main.pg.draw.rect(main.SCREEN, main.COR, botoes[1].rect.inflate(int(main.RES[1] / 15.3),0), 5)
		elif botao_selecionado == 3: main.pg.draw.rect(main.SCREEN, main.COR, botoes[2].rect.inflate(int(main.RES[1] / 15.3),0), 5)
		if botao_selecionado > MAX_B: botao_selecionado = 1
		elif botao_selecionado < MIN_B: botao_selecionado = MAX_B

		main.SCREEN.blit(title, title_rect)

		# Desenha botões
		for botao in botoes: botao_group.draw(main.SCREEN)

		main.pg.display.flip()
