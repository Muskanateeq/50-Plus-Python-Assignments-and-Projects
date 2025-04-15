def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """Checks if there's a winner."""
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]  # Row win
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]  # Column win
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]  # Main diagonal win
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]  # Anti-diagonal win

    return None  # No winner yet

def is_full(board):
    """Checks if the board is full (draw)."""
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    """Main game function."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        print(f"Player {players[turn]}'s turn.")
        
        # Get user input
        try:
            row, col = map(int, input("Enter row and column (0-2, space-separated): ").split())
            if board[row][col] != " ":
                print("Cell already occupied! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Enter two numbers between 0-2.")
            continue

        # Make the move
        board[row][col] = players[turn]

        # Check for a winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins! 🎉")
            break

        # Check for a draw
        if is_full(board):
            print_board(board)
            print("It's a draw! 🤝")
            break

        # Switch turns
        turn = 1 - turn

if __name__ == "__main__":
    tic_tac_toe()
