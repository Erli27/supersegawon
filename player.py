# src/player.py
import pygame
import config

class Segawon(pygame.sprite.Sprite):
    def _init_(self):
        super()._init_()
        # Membuat kotak cokelat mewakili Segawon
        self.image = pygame.Surface((50, 40))
        self.image.fill(config.DOG_BROWN) 
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 450
        
        # Physics variables
        self.vel_y = 0
        self.is_jumping = False

    def update(self):
        # Efek Gravitasi
        self.vel_y += config.GRAVITY
        self.rect.y += self.vel_y

        # Batasan Tanah (Floor Collision)
        if self.rect.bottom >= 500:
            self.rect.bottom = 500
            self.vel_y = 0
            self.is_jumping = False

        # Input Gerakan Kiri/Kanan
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= config.PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += config.PLAYER_SPEED

        # Batasan Batas Layar
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.right > config.SCREEN_WIDTH: self.rect.right = config.SCREEN_WIDTH

    def jump(self):
        if not self.is_jumping:
            self.vel_y = config.JUMP_POWER
            self.is_jumping = True
