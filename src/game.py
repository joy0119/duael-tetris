
import main

class WritingBox:
	def __init__(self, font: main.pg.font.Font):
		self.text_buffer = []  # Armazena oq esta sendo escrito e oq sera enviado
		self.font = font
		self.rect = main.pg.Rect()

	def write(self, event):
		if event.type == main.pg.KEYDOWN:
			if event.key in (main.pg.K_KP_ENTER):
				return self.text_buffer
			elif event.key == main.pg.K_BACKSPACE:
				self.text_buffer.pop()
			else: self.text_buffer.append(event.key.unicode)

	def print(self, cor) -> main.pg.Surface:
		return self.font.render(self.text_buffer, False, cor)
#(self.rect.width / 1.5, font.size)
class ChatBox:
	def __init__(self, font: main.pg.font.Font, outline_color, resolution: tuple, pos: tuple):
		self.historico = []    # Mensagens recebidas e enviadas 
		self.font = font
		self.my_surface = main.pg.Surface(resolution)
		self.rect = self.my_surface.get_rect(center = pos)
		self.outline_color = outline_color
		self.chat = WritingBox(font)

	def draw(self, surface):
		main.pg.draw.rect(surface, self.outline_color, self.rect)  # Caixa inteira
		main.pg.draw.rect(surface, self.outline_color, self.chat.rect)  # Caixa de escrita
		self.my_surface.blit(self.chat.print(self.outline_color), self.chat.rect)

	def get_input(self):
		self.chat.write()

# def desenhar_tela_conexao():
# 	SCREEN.fill((0,0,0))


# def conexao():
# 	while True:
# 		desenhar_tela_conexao()


def mult():
	# conexao()
	conversa = ChatBox(main.FONTS[2], main.COR, (400, 600), (10,10))
	while True:
		for event in main.pg.event.get():
			conversa.chat.write(event)

		conversa.draw(main.SCREEN)
		main.SCREEN.fill((0,0,0))
		main.pg.display.flip()