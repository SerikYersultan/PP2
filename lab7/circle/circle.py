import pygame
import sys

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400

BALL_RADIUS = 25
BALL_DIAMETER = BALL_RADIUS * 2

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ball Movement")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y = max(BALL_RADIUS, ball_y - 20)
            elif event.key == pygame.K_DOWN:
                ball_y = min(SCREEN_HEIGHT - BALL_RADIUS, ball_y + 20)
            elif event.key == pygame.K_LEFT:
                ball_x = max(BALL_RADIUS, ball_x - 20)
            elif event.key == pygame.K_RIGHT:
                ball_x = min(SCREEN_WIDTH - BALL_RADIUS, ball_x + 20)

    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
