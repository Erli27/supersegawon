# main.py
import pygame
import sys
import random

# Import modul lokal
import config
from src.player import Segawon

# Inisialisasi Game
pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Super Segawon: Petualangan Mencari Tulang")
clock = pygame.time.Clock()

# Setup Objek Game
player = Segawon()
player_group = pygame.sprite.GroupSingle(player)

score = 0
font = pygame.font.SysFont("Arial", 30)

# 🔄 SIKLUS UTAMA GAME (GAME LOOP)
running = True
while running:
    
    # 1. Mendeteksi Input Tombol
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_SPACE, pygame.K_UP, pygame.K_w]:
                player.jump()

    # 2. Update Logika Game
    player_group.update()

    # 3. Menggambar Semuanya ke Layar (Rendering)
    screen.fill(config.SKY_BLUE) # Langit
    pygame.draw.rect(screen, config.GRASS_GREEN, (0, 500, config.SCREEN_WIDTH, 100)) # Tanah
    
    player_group.draw(screen) # Karakter Segawon

    # Tampilan UI Skor
    score_text = font.render(f"Skor Tulang: {score}", True, config.TEXT_WHITE)
    screen.blit(score_text, (20, 20))

    pygame.display.flip()
    clock.tick(config.FPS)

pygame.quit()
sys.exit()
