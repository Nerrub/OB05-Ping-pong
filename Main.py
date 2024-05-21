import pygame

import sys

pygame.init()

screen_width, screen_height = 600, 400

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Пин-понг")

# Цвета

BLACK = (0, 0, 0)

WHITE = (255, 255, 255)

BLUE = (0, 0, 255)

# FPS

clock = pygame.time.Clock()
fps = 60

# Параметры платформы
paddle_width, paddle_height = 100, 10
paddle_x = (screen_width - paddle_width) // 2
paddle_y = screen_height - paddle_height - 20
paddle_speed = 6

# Параметры мяча
ball_radius = 8
ball_x = screen_width // 2
ball_y = paddle_y - ball_radius
ball_speed_x = 4
ball_speed_y = -4

# Запуск основного цикла игры
running = True
while running:
    # Обработка событий

    for event in pygame.event.get():
    if event.type == pygame.QUIT:
    running = False

    # Движение платформы

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
        paddle_x += paddle_speed
    # Движение мяча
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Столкновение с краями экрана

    if ball_x <= 0 or ball_x >= screen_width:
    ball_speed_x = -ball_speed_x
    if ball_y <= 0:
    ball_speed_y = -ball_speed_y
    if ball_y >= screen_height:

