import pygame
import sys
import random
from pygame.locals import *

pygame.init()


WINDOW_WIDTH, WINDOW_HEIGHT = 400, 400
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Snake')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

snake = [(100, 100), (90, 100), (80, 100)]
snake_length = len(snake)
snake_direction = 'right'
snake_speed = 10  

food = (random.randint(0, WINDOW_WIDTH//10 - 1) * 10, random.randint(0, WINDOW_HEIGHT//10 - 1) * 10)

level = 1
score = 0
level_threshold = 3 

font = pygame.font.SysFont(None, 24)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_UP and snake_direction != 'down':
                snake_direction = 'up'
            elif event.key == K_DOWN and snake_direction != 'up':
                snake_direction = 'down'
            elif event.key == K_LEFT and snake_direction != 'right':
                snake_direction = 'left'
            elif event.key == K_RIGHT and snake_direction != 'left':
                snake_direction = 'right'

    if snake_direction == 'up':
        snake.insert(0, (snake[0][0], snake[0][1] - 10))
    elif snake_direction == 'down':
        snake.insert(0, (snake[0][0], snake[0][1] + 10))
    elif snake_direction == 'left':
        snake.insert(0, (snake[0][0] - 10, snake[0][1]))
    elif snake_direction == 'right':
        snake.insert(0, (snake[0][0] + 10, snake[0][1]))

    if snake[0] == food:
        score += 1
        food = (random.randint(0, WINDOW_WIDTH//10 - 1) * 10, random.randint(0, WINDOW_HEIGHT//10 - 1) * 10)
        while food in snake:  
            food = (random.randint(0, WINDOW_WIDTH//10 - 1) * 10, random.randint(0, WINDOW_HEIGHT//10 - 1) * 10)
    else:
        snake.pop() 
    
    if (snake[0][0] < 0 or snake[0][0] >= WINDOW_WIDTH or
            snake[0][1] < 0 or snake[0][1] >= WINDOW_HEIGHT):
        running = False  

    if snake[0] in snake[1:]:
        running = False  

    if score >= level_threshold * level:
        level += 1
        snake_speed += 2 

    windowSurface.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(windowSurface, WHITE, (segment[0], segment[1], 10, 10))
    pygame.draw.rect(windowSurface, RED, (food[0], food[1], 10, 10))

    score_text = font.render(f'Score: {score}', True, GREEN)
    level_text = font.render(f'Level: {level}', True, GREEN)
    windowSurface.blit(score_text, (10, 10))
    windowSurface.blit(level_text, (10, 30))

    pygame.display.update()

    pygame.time.Clock().tick(snake_speed)

pygame.quit()
sys.exit()
