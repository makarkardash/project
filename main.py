import pygame
import sys

pygame.init()
size_block = 100
margin = 15
width = height = size_block*3 + margin*4

size_window = (width,height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Крестики-нолики")

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
mas = [[0]*3 for i in range(3)]

while True:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN :
            x_mouse, y_mouse = pygame.mouse.get_pos()
            x_b =x_mouse // (size_block + margin)
            x_a = x_mouse // (size_block + margin)
            mas [a] [b] = 'x'

    for a in range (3) :
        for b in range (3) :
            if mas [a] [b] == 'x' :
           x = b * size_block + (b + 1) * margin
           y = a * size_block + (a + 1) * margin
           pygame.draw.rect(screen, , (x,y,size_block,size_block))
    pygame.display.update()


