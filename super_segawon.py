import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# 🖥️ SCREEN SETTINGS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Super Segawon: Petualangan Mencari Tulang")

# 🎨 COLORS (RGB)
SKY_BLUE = (135, 206, 235)
GRASS_GREEN = (34, 139, 34)
DOG_BROWN = (139, 69, 19)
BONE_YELLOW = (255, 215, 0)
TEXT_WHITE = (255, 255, 255)

# ⏱️ CLOCK & FPS
clock = pygame.time.Clock()
FPS = 60

# 🐾 PLAYER (SUPER SEGAWON) CLASS
class Segawon(pygame.sprite.Sprite):
    def _init_(self):
        super()._init_()
        self.image = pygame.Surface((50, 40))
        self.image.fill(DOG_BROWN) # Representasi Segawon (Kotak Cokelat)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 450
        
        # Physics variables
        self.vel_y = 0
        self.jump_power = -15
        self.gravity = 0.8
        self.speed = 6
        self.is_jumping = False

    def update(self):
        # Apply Gravity
        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        # Floor Collision (Batasan Tanah)
        if self.rect.bottom >= 500:
            self.rect.bottom = 500
            self.vel_y = 0
            self.is_jumping = False

        # Handle Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed

        # Screen Boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def jump(self):
        if not self.is_jumping:
            self.vel_y = self.jump_power
            self.is_jumping = True

# 🦴 COIN TULANG CLASS
class BoneCoin(pygame.sprite.Sprite):
    def _init_(self):
        super()._init_()
        self.image = pygame.Surface((20, 20))
        self.image.fill(BONE_YELLOW) # Representasi Koin Tulang
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(200, SCREEN_WIDTH - 50)
        self.rect.y = random.randint(300, 450)

# 🎮 GAME SETUP
player = Segawon()
player_group = pygame.sprite.GroupSingle(player)

bone_group = pygame.sprite.Group()
for _ in range(5): # Memunculkan 5 koin awal
    bone_group.add(BoneCoin())

score = 0
font = pygame.font.SysFont("Arial", 30)

# 🔄 MAIN GAME LOOP
running = True
while running:
    # 1. Event Handling (Input Pemain)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w:
                player.jump()

    # 2. Update Game State
    player_group.update()

    # Cek tabrakan antara Segawon dan Koin Tulang
    collisions = pygame.sprite.spritecollide(player, bone_group, True)
    for hit in collisions:
        score += 1
        bone_group.add(BoneCoin()) # Munculkan koin baru jika ada yang termakan

    # 3. Drawing / Rendering (Menggambar ke Layar)
    screen.fill(SKY_BLUE) # Gambar Langit

    # Gambar Tanah (Ground)
    pygame.draw.rect(screen, GRASS_GREEN, (0, 500, SCREEN_WIDTH, 100))

    # Gambar Karakter dan Item
    player_group.draw(screen)
    bone_group.draw(screen)

    # Tampilkan Skor Tulang
    score_text = font.render(f"Tulang Dikumpulkan: {score}", True, TEXT_WHITE)
    screen.blit(score_text, (20, 20))

    # Refresh Screen
    pygame.display.flip()
    clock.tick(FPS)

# Quit Game
pygame.quit()
sys.exit()import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# 🖥️ SCREEN SETTINGS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Super Segawon: Petualangan Mencari Tulang")

# 🎨 COLORS (RGB)
SKY_BLUE = (135, 206, 235)
GRASS_GREEN = (34, 139, 34)
DOG_BROWN = (139, 69, 19)
BONE_YELLOW = (255, 215, 0)
TEXT_WHITE = (255, 255, 255)

# ⏱️ CLOCK & FPS
clock = pygame.time.Clock()
FPS = 60

# 🐾 PLAYER (SUPER SEGAWON) CLASS
class Segawon(pygame.sprite.Sprite):
    def _init_(self):
        super()._init_()
        self.image = pygame.Surface((50, 40))
        self.image.fill(DOG_BROWN) # Representasi Segawon (Kotak Cokelat)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 450
        
        # Physics variables
        self.vel_y = 0
        self.jump_power = -15
        self.gravity = 0.8
        self.speed = 6
        self.is_jumping = False

    def update(self):
        # Apply Gravity
        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        # Floor Collision (Batasan Tanah)
        if self.rect.bottom >= 500:
            self.rect.bottom = 500
            self.vel_y = 0
            self.is_jumping = False

        # Handle Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed

        # Screen Boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def jump(self):
        if not self.is_jumping:
            self.vel_y = self.jump_power
            self.is_jumping = True

# 🦴 COIN TULANG CLASS
class BoneCoin(pygame.sprite.Sprite):
    def _init_(self):
        super()._init_()
        self.image = pygame.Surface((20, 20))
        self.image.fill(BONE_YELLOW) # Representasi Koin Tulang
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(200, SCREEN_WIDTH - 50)
        self.rect.y = random.randint(300, 450)

# 🎮 GAME SETUP
player = Segawon()
player_group = pygame.sprite.GroupSingle(player)

bone_group = pygame.sprite.Group()
for _ in range(5): # Memunculkan 5 koin awal
    bone_group.add(BoneCoin())

score = 0
font = pygame.font.SysFont("Arial", 30)

# 🔄 MAIN GAME LOOP
running = True
while running:
    # 1. Event Handling (Input Pemain)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w:
                player.jump()

    # 2. Update Game State
    player_group.update()

    # Cek tabrakan antara Segawon dan Koin Tulang
    collisions = pygame.sprite.spritecollide(player, bone_group, True)
    for hit in collisions:
        score += 1
        bone_group.add(BoneCoin()) # Munculkan koin baru jika ada yang termakan

    # 3. Drawing / Rendering (Menggambar ke Layar)
    screen.fill(SKY_BLUE) # Gambar Langit

    # Gambar Tanah (Ground)
    pygame.draw.rect(screen, GRASS_GREEN, (0, 500, SCREEN_WIDTH, 100))

    # Gambar Karakter dan Item
    player_group.draw(screen)
    bone_group.draw(screen)

    # Tampilkan Skor Tulang
    score_text = font.render(f"Tulang Dikumpulkan: {score}", True, TEXT_WHITE)
    screen.blit(score_text, (20, 20))

    # Refresh Screen
    pygame.display.flip()
    clock.tick(FPS)

# Quit Game
pygame.quit()
sys.exit()
