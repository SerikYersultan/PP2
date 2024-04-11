import pygame
import sys
from pygame.locals import *
import os
os.chdir("C:/pp2/lab7/music")

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 200

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Music Player")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

music= ["C:\pp2\lab7\music\music\mus.mp3", "C:\pp2\lab7\music\music\mus1.mp3"]
current_track = 0

pygame.mixer.music.load(music[current_track])

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_p:  
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.play()
            elif event.key == K_s:  
                pygame.mixer.music.stop()
            elif event.key == K_n:  
                current_track = (current_track + 1) % len(music)
                pygame.mixer.music.load(music[current_track])
                pygame.mixer.music.play()
            elif event.key == K_b:  
                current_track = (current_track - 1) % len(music)
                pygame.mixer.music.load(music[current_track])
                pygame.mixer.music.play()

    
    screen.fill(BLACK)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
