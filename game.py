# Название: Холодный след
# Жанр: детективный top-down квест с расследованием
# Идея в одном предложении: Детектив ходит по локациям 1970-х, ищет улики и опрашивает свидетелей, чтобы вычислить убийцу.
# Размер окна: 960 x 640
# Цветовая гамма: тёмная, приглушённая (тёмно-серо-синий фон)

import pygame

WIDTH = 960
HEIGHT = 640
FPS = 60
BG_COLOR = (24, 26, 33)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Холодный след")
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)
    pygame.display.update()

pygame.quit()