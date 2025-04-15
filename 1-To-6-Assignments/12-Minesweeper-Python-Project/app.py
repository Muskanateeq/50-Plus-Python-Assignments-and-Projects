import tkinter as tk
import random

# Game settings
GRID_SIZE = 10  # Grid is 10x10
MINES_COUNT = 15  # Number of mines

class Minesweeper:
    def __init__(self, root):
        self.root = root
        self.root.title("Minesweeper")
        self.grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.buttons = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.revealed = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.mines = set()
        
        self.create_widgets()
        self.place_mines()
        self.calculate_numbers()
        
    def create_widgets(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                btn = tk.Button(self.root, width=3, height=1, command=lambda r=row, c=col: self.reveal(r, c))
                btn.grid(row=row, column=col)
                self.buttons[row][col] = btn
    
    def place_mines(self):
        while len(self.mines) < MINES_COUNT:
            row, col = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
            if (row, col) not in self.mines:
                self.mines.add((row, col))
                self.grid[row][col] = -1  # -1 represents a mine
    
    def calculate_numbers(self):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if self.grid[row][col] == -1:
                    continue
                count = 0
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE and self.grid[nr][nc] == -1:
                        count += 1
                self.grid[row][col] = count
    
    def reveal(self, row, col):
        if self.revealed[row][col]:
            return
        
        self.revealed[row][col] = True
        if self.grid[row][col] == -1:
            self.buttons[row][col].config(text="*", bg="red")
            self.game_over()
            return
        
        self.buttons[row][col].config(text=str(self.grid[row][col]) if self.grid[row][col] > 0 else "", state="disabled", relief=tk.SUNKEN)
        
        if self.grid[row][col] == 0:
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE:
                    self.reveal(nr, nc)
        
        if self.check_win():
            self.show_message("You won!")
    
    def game_over(self):
        for row, col in self.mines:
            self.buttons[row][col].config(text="*", bg="red")
        self.show_message("Game Over! You hit a mine.")
    
    def check_win(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if self.grid[row][col] != -1 and not self.revealed[row][col]:
                    return False
        return True
    
    def show_message(self, message):
        win = tk.Toplevel(self.root)
        win.title("Game Over")
        tk.Label(win, text=message, font=("Arial", 14)).pack(pady=10)
        tk.Button(win, text="OK", command=self.root.quit).pack()

if __name__ == "__main__":
    root = tk.Tk()
    game = Minesweeper(root)
    root.mainloop()
