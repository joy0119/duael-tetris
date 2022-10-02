from main import pg, FONTS, COR
class Botao(pg.sprite.Sprite):
	def __init__(self, text: str, pos: tuple, selecionado: bool = False):
		super().__init__()
		self.image = FONTS[1].render(text, False, COR)
		self.rect = self.image.get_rect(center = pos)
		self.selecionado = selecionado

class Player:
	points: int
	
	def __init__(self):
		self.points = 0

	def pontuar(self, points):
		self.points += points

class Bloco(pg.sprite.Sprite):
	def __init__(self):
		super().__init__()