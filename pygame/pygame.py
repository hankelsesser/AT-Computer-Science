import pygame


def draw_design():
  for x in range(0, 400, 50):
    for y in range(0, 400, 50):
      pygame.draw.circle(screen, (60, 60, 60), (x, y), 75)

pygame.init()
size = (400,400)
screen = pygame.display.set_mode(size)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    draw_design()
    pygame.display.flip()
pygame.quit()
