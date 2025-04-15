import pygame
import random

pygame.init()

# Game Constants
WIDTH, HEIGHT = 300, 600
GRID_SIZE = 30
COLS, ROWS = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
WHITE, BLACK, BLUE, RED, GREEN = (255, 255, 255), (0, 0, 0), (0, 0, 255), (255, 0, 0), (0, 255, 0)

# Tetromino Shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]]  # J
]

class Tetromino:
    def __init__(self, shape):
        self.shape = shape
        self.color = random.choice([RED, BLUE, GREEN])
        self.x, self.y = COLS // 2 - len(shape[0]) // 2, 0

    def rotate(self):
        rotated = [list(row) for row in zip(*self.shape[::-1])]
        if self.can_move(grid, rotated, 0, 0):
            self.shape = rotated

    def can_move(self, grid, shape, dx, dy):
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x, new_y = self.x + x + dx, self.y + y + dy
                    if new_x < 0 or new_x >= COLS or new_y >= ROWS or (new_y >= 0 and grid[new_y][new_x]):
                        return False
        return True

    def place(self, grid):
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    grid[self.y + y][self.x + x] = self.color

def clear_lines(grid):
    new_grid = [row for row in grid if any(cell == BLACK for cell in row)]
    lines_cleared = ROWS - len(new_grid)
    while len(new_grid) < ROWS:
        new_grid.insert(0, [BLACK] * COLS)
    return new_grid, lines_cleared

# Initialize game
grid = [[BLACK] * COLS for _ in range(ROWS)]
current_piece = Tetromino(random.choice(SHAPES))
clock = pygame.time.Clock()
game_over = False
score = 0
speed = 5  # Initial speed

# Create Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

# Game Loop
while not game_over:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and current_piece.can_move(grid, current_piece.shape, -1, 0):
                current_piece.x -= 1
            if event.key == pygame.K_RIGHT and current_piece.can_move(grid, current_piece.shape, 1, 0):
                current_piece.x += 1
            if event.key == pygame.K_DOWN and current_piece.can_move(grid, current_piece.shape, 0, 1):
                current_piece.y += 1
            if event.key == pygame.K_UP:
                current_piece.rotate()

    # Move piece down automatically
    if current_piece.can_move(grid, current_piece.shape, 0, 1):
        current_piece.y += 1
    else:
        current_piece.place(grid)
        grid, lines_cleared = clear_lines(grid)
        score += lines_cleared * 10  # Update score
        speed = min(10, speed + lines_cleared)  # Increase speed
        current_piece = Tetromino(random.choice(SHAPES))
        
        # **Fix:** Check if new piece can move, otherwise game over
        if not current_piece.can_move(grid, current_piece.shape, 0, 0):
            print("Game Over!")
            game_over = True

    # Draw grid
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            pygame.draw.rect(screen, cell, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)
            pygame.draw.rect(screen, BLACK, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

    # Draw current piece
    for y, row in enumerate(current_piece.shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, current_piece.color, ((current_piece.x + x) * GRID_SIZE, (current_piece.y + y) * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)
                pygame.draw.rect(screen, BLACK, ((current_piece.x + x) * GRID_SIZE, (current_piece.y + y) * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

    pygame.display.flip()
    clock.tick(speed)  # Dynamic speed adjustment

# Keep the game window open after game over
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


