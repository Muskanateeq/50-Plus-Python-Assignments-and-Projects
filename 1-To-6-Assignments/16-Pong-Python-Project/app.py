import pygame

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = [5, 5]
PADDLE_SPEED = 7
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WINNING_SCORE = 5

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Paddle Settings
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)
left_paddle = pygame.Rect(10, HEIGHT // 2 - 50, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 25, HEIGHT // 2 - 50, PADDLE_WIDTH, PADDLE_HEIGHT)

# Score Tracking
left_score = 0
right_score = 0
font = pygame.font.Font(None, 50)

# Game Loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_SPEED

    # Ball Movement
    ball.x += BALL_SPEED[0]
    ball.y += BALL_SPEED[1]

    # Ball Collision with Walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_SPEED[1] = -BALL_SPEED[1]

    # Ball Collision with Paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        BALL_SPEED[0] = -BALL_SPEED[0]

    # Ball Reset on Score
    if ball.left <= 0:  # Right player scores
        right_score += 1
        ball.x, ball.y = WIDTH // 2 - 10, HEIGHT // 2 - 10
        BALL_SPEED[0] = -BALL_SPEED[0]
    if ball.right >= WIDTH:  # Left player scores
        left_score += 1
        ball.x, ball.y = WIDTH // 2 - 10, HEIGHT // 2 - 10
        BALL_SPEED[0] = -BALL_SPEED[0]

    # Draw Elements
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Display Scores
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (WIDTH // 4, 20))
    screen.blit(right_text, (WIDTH * 3 // 4, 20))

    # Check for Game Over
    if left_score >= WINNING_SCORE or right_score >= WINNING_SCORE:
        winner = "Left Player Wins!" if left_score > right_score else "Right Player Wins!"
        win_text = font.render(winner, True, WHITE)
        screen.blit(win_text, (WIDTH // 2 - 100, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(3000)  # Show message for 3 seconds
        running = False

    # Refresh Screen
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()

