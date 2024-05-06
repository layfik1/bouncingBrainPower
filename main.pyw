import pygame

pygame.mixer.init()

sc = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
pygame.display.set_caption("github.com/layfik1")
pygame.display.set_icon(pygame.image.load("resources/icon.png"))
pygame.mixer.music.load("resources/audio.ogg")

pygame.mixer.music.play()

pygame.mixer.music.set_volume(0.5)
height = 720
clock.tick(31)

while True:
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			pygame.quit()

	for i in range(841):
		if i > 188:		
			if height >= 720:
				s = -128
			if height <= 128:
				s = 128
			height += s
			pygame.display.set_mode((1280,height))

		if i >= 840:
			pygame.quit()

		clock.tick(31)
		image = pygame.image.load("resources/"+str(i+1)+".png")

		w,h = pygame.display.get_surface().get_size()
		image = pygame.transform.scale(image,(w,h))

		sc.blit(image,(0,0))
		pygame.display.update()

		
