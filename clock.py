import pygame
import time
import datetime
pygame.init()
window = pygame.display.set_mode((500, 300))
window.fill((10, 10, 10))
clock = pygame.time.Clock()
def text_objects(text, font):
	textSurface = font.render(text, True, (250, 250, 0))
	return textSurface, textSurface.get_rect()
def message_display(text, width, height):
	smallText = pygame.font.Font('anquietas.ttf', 60)
	TextSurf, TextRect = text_objects(text, smallText)
	TextRect.center = (width, height)
	window.blit(TextSurf, TextRect)
while True:
	clock.tick(15)
	text = datetime.datetime.now().time().strftime('%H . %M . %S . %f')[:-3]
	print(text)
	message_display(text, 250, 150)
	pygame.display.update()
	window.fill((0,0,0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()



		
