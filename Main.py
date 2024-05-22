import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение размеров экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ping Pong')

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)

# Координаты и размеры объектов
ball_radius = 15
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_dx = 3
ball_dy = 3

paddle_width = 10
paddle_height = 100
paddle_speed = 6

left_paddle_x = 30
left_paddle_y = (screen_height - paddle_height) // 2

right_paddle_x = screen_width - 40
right_paddle_y = (screen_height - paddle_height) // 2

# Основной игровой цикл
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= paddle_speed
    if keys[pygame.K_s] and left_paddle_y < screen_height - paddle_height:
        left_paddle_y += paddle_speed
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle_y < screen_height - paddle_height:
        right_paddle_y += paddle_speed

    ball_x += ball_dx
    ball_y += ball_dy

    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= screen_height:
        ball_dy = -ball_dy

    if (ball_x - ball_radius <= left_paddle_x + paddle_width and
        left_paddle_y <= ball_y <= left_paddle_y + paddle_height):
        ball_dx = -ball_dx

    if (ball_x + ball_radius >= right_paddle_x and
        right_paddle_y <= ball_y <= right_paddle_y + paddle_height):
        ball_dx = -ball_dx

    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= screen_width:
        ball_x = screen_width // 2
        ball_y = screen_height // 2
        ball_dx = -ball_dx

    screen.fill(black)
    pygame.draw.rect(screen, white, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, white, (ball_x, ball_y), ball_radius)

    pygame.display.flip()
    clock.tick(60)