import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    
    # Check for draw
    for row in board:
        if ' ' in row:
            return None  # Game still ongoing
    return 'Draw'

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return -10 + depth
    if winner == 'O':
        return 10 - depth
    if winner == 'Draw':
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(best_score, score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Tic-Tac-Toe AI (You: X, AI: O)")
    print_board(board)
    
    while True:
        # Human Player (X)
        row, col = map(int, input("Enter row and column betweeen(0-2, space-separated): ").split())
        if board[row][col] != ' ':
            print("Invalid input! Enter two numbers between 0-2.")
            continue
        board[row][col] = 'X'
        print_board(board)
        if check_winner(board):
            break
        
        # AI Player (O)
        print("AI is making a move...")
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = 'O'
        print_board(board)
        if check_winner(board):
            break
    
    winner = check_winner(board)
    if winner == 'Draw':
        print("It's a draw!")
    else:
        print(f"{winner} wins!")

if __name__ == "__main__":
    play_game()
