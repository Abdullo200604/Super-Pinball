import pygame
import random
import sys

# Pygame boshlanishi
pygame.init()

# Oyna o'lchamlari
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pinball")

# Ranglar
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Flipper parametrlar
FLIPPER_WIDTH = 100
FLIPPER_HEIGHT = 20
flipper_speed = 12

# To‘p parametrlar
BALL_RADIUS = 10
ball_speed_x = 5
ball_speed_y = -5

# Flippers boshlang'ich joylari
left_flipper_x = WIDTH // 2 - FLIPPER_WIDTH - 50
right_flipper_x = WIDTH // 2 + 50
flipper_y = HEIGHT - 60

# To‘p boshlang‘ich joyi
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = random.choice([5, -5])
ball_dy = -5

# FPS va Clock
clock = pygame.time.Clock()
FPS = 60

# Flipperni boshqarish uchun holatlar
left_flipper_up = False
right_flipper_up = False

# O'yin asosiy tsikli
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # O‘yin olayotgan asosiy tsikl
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Klaviaturadan boshqarish
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        left_flipper_up = True
    else:
        left_flipper_up = False

    if keys[pygame.K_RIGHT]:
        right_flipper_up = True
    else:
        right_flipper_up = False

    # To‘p harakati
    ball_x += ball_dx
    ball_y += ball_dy

    # To‘pni yuqoriga yoki pastga qaytarish
    if ball_y - BALL_RADIUS <= 0:
        ball_dy *= -1
    if ball_x - BALL_RADIUS <= 0 or ball_x + BALL_RADIUS >= WIDTH:
        ball_dx *= -1

    # To‘p flipper bilan to‘qnashuvi
    if (left_flipper_up and left_flipper_x < ball_x < left_flipper_x + FLIPPER_WIDTH and
            flipper_y < ball_y + BALL_RADIUS < flipper_y + FLIPPER_HEIGHT):
        ball_dy *= -1

    if (right_flipper_up and right_flipper_x < ball_x < right_flipper_x + FLIPPER_WIDTH and
            flipper_y < ball_y + BALL_RADIUS < flipper_y + FLIPPER_HEIGHT):
        ball_dy *= -1

    # Flipperlarni chizish
    if left_flipper_up:
        pygame.draw.rect(screen, RED, (left_flipper_x, flipper_y, FLIPPER_WIDTH, FLIPPER_HEIGHT))
    else:
        pygame.draw.rect(screen, WHITE, (left_flipper_x, flipper_y, FLIPPER_WIDTH, FLIPPER_HEIGHT))

    if right_flipper_up:
        pygame.draw.rect(screen, RED, (right_flipper_x, flipper_y, FLIPPER_WIDTH, FLIPPER_HEIGHT))
    else:
        pygame.draw.rect(screen, WHITE, (right_flipper_x, flipper_y, FLIPPER_WIDTH, FLIPPER_HEIGHT))

    # To‘pni chizish
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)

    # Ekranni yangilash
    pygame.display.flip()

pygame.quit()
sys.exit()
