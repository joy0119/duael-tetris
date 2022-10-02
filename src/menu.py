from classes import Botao
from main import RES, SCREEN, pg
def menu():
	posx_b_s = RES[0] / 3
	posx_b_d = RES[0] - posx_b_s	# Mantém simetria com o outro botao
	posy_b = RES[1] / 1.75

	botao_selecionado = 1  # Usado como referência para mapear qual o botão está sendo selecionado
	solo = Botao('SOLO', (posx_b_s, posy_b))
	mult = Botao('MULT', (posx_b_d, posy_b))

	# COLOCAR OS GRUPOS

	botoes = [solo, mult]
	while True:
		SCREEN.fill((0,0,0))

		# # Desenha o cursor de seleção
		# if botao_selecionado == 1: pg.draw.rect(SCREEN, COR, solo_rect.inflate(int(RES[1] / 15.3),0), 5)
		# if botao_selecionado == 2: pg.draw.rect(SCREEN, COR, dual_rect.inflate(int(RES[1] / 15.3),0), 5)
		# if botao_selecionado > 2: botao_selecionado = 1
		# elif botao_selecionado < 1: botao_selecionado = 2

		# Desenha botões
		for botao in botoes: botao.draw(SCREEN)

		pg.display.flip()
