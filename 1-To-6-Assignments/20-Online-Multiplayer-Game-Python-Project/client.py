import pygame
import socketio

# Connect to the game server
sio = socketio.Client()
sio.connect("http://localhost:5000")

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100

# Game variables
paddle_y = 250
player_id = None
players = {}

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multiplayer Pong")

@sio.on("player_id")
def set_player_id(id):
    global player_id
    player_id = id

@sio.on("update_players")
def update_players(data):
    global players
    players = data

running = True
while running:
    screen.fill(BLACK)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and paddle_y > 0:
        paddle_y -= 5
    if keys[pygame.K_DOWN] and paddle_y < HEIGHT - PADDLE_HEIGHT:
        paddle_y += 5

    # Send paddle position to server
    sio.emit("move_paddle", {"y": paddle_y})

    # Draw paddles
    for i, player in enumerate(players.values()):
        x = 50 if i == 0 else WIDTH - 70
        pygame.draw.rect(screen, WHITE, (x, player["y"], PADDLE_WIDTH, PADDLE_HEIGHT))

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
sio.disconnect()
