import pygame
import random
import math

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Player (Spaceship) properties
player_img = pygame.Surface((60, 40))
player_img.fill(GREEN)
player_x = WIDTH // 2 - 30
player_y = HEIGHT - 60
player_speed = 5

# Bullet properties
bullet_img = pygame.Surface((5, 15))
bullet_img.fill(RED)
bullet_speed = 7
bullet_state = "ready"  # "ready" means bullet is not visible, "fire" means bullet is moving
bullet_x = 0
bullet_y = player_y

# Alien (Invader) properties
alien_img = pygame.Surface((40, 30))
alien_img.fill(WHITE)
alien_speed = 2
aliens = []  # List of [x, y, x_speed]
alien_rows = 3
alien_cols = 8

for row in range(alien_rows):
    for col in range(alien_cols):
        alien_x = col * 80 + 50
        alien_y = row * 60 + 50
        aliens.append([alien_x, alien_y, alien_speed])

# Score
score = 0
font = pygame.font.Font(None, 36)

def show_score():
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

def fire_bullet(x, y):
    global bullet_state, bullet_x, bullet_y
    bullet_state = "fire"
    bullet_x = x + 27  # Center bullet relative to player (60/2 - bullet_width/2)
    bullet_y = y

def is_collision(bullet_x, bullet_y, alien_x, alien_y):
    distance = math.sqrt((bullet_x - (alien_x + 20)) ** 2 + (bullet_y - (alien_y + 15)) ** 2)
    return distance < 30

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)
    
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 60:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        if bullet_state == "ready":
            fire_bullet(player_x, player_y)
    
    # Bullet Movement
    if bullet_state == "fire":
        screen.blit(bullet_img, (bullet_x, bullet_y))
        bullet_y -= bullet_speed
        if bullet_y < 0:
            bullet_state = "ready"
            bullet_y = player_y
    
    # Alien Movement and Collision
    for alien in aliens[:]:
        alien[0] += alien[2]  # Move alien horizontally
        
        # Reverse direction and move down if hitting wall
        if alien[0] <= 0 or alien[0] >= WIDTH - 40:
            alien[2] *= -1
            alien[1] += 40
        
        # Check collision with bullet
        if bullet_state == "fire" and is_collision(bullet_x, bullet_y, alien[0], alien[1]):
            bullet_state = "ready"
            bullet_y = player_y
            score += 1
            aliens.remove(alien)
        
        # Draw alien
        screen.blit(alien_img, (alien[0], alien[1]))
    
    # Draw player
    screen.blit(player_img, (player_x, player_y))
    
    # Display Score
    show_score()
    
    # Check for game over (if an alien reaches near the player)
    for alien in aliens:
        if alien[1] + 30 >= player_y:
            running = False
    
    pygame.display.flip()
    clock.tick(60)

# Game Over screen
screen.fill(BLACK)
game_over_text = font.render("GAME OVER", True, WHITE)
screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 20))
pygame.display.flip()
pygame.time.delay(3000)
pygame.quit()
