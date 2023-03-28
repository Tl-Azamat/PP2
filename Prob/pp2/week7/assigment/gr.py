import pygame
import sys

pygame.init()
WHITE = (255, 255, 255)
RED = (255, 0, 0)
clock = pygame.time.Clock()

size = [800, 600]
x , y = 800 // 2 , 600//2
speed = 20
r = 25

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ball game")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y-r > 0:
        y-=speed
    if keys[pygame.K_DOWN] and y+r < 600:
        y+=speed
    if keys[pygame.K_LEFT] and x-r > 0:
        x-=speed
    if keys[pygame.K_RIGHT] and x+r < 800:
        x+=speed

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), r)
    clock.tick(30)

    pygame.display.update()
    pygame.display.flip()