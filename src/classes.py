import main

class Botao(main.pg.sprite.Sprite):
	def __init__(self, text: str, pos: tuple, selecionado: bool = False):
		super().__init__()
		self.image = main.FONTS[1].render(text, False, main.COR)
		self.rect = self.image.get_rect(center = pos)
		self.selecionado = selecionado

class Player:
	points: int
	
	def __init__(self):
		self.points = 0

	def pontuar(self, points):
		self.points += points

class Bloco(main.pg.sprite.Sprite):
	def __init__(self):
		super().__init__()