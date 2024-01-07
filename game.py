import pygame

pygame.init()

window_size = (600, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Joc cu Fundal")

# Încarcă imaginea de fundal
background_image = pygame.image.load("assets/background.jpg")

running = True
while running:
    # Desenează fundalul
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
