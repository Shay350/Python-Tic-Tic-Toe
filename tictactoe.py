import random

# Define constants to represent the player markers
X = 'X'
O = 'O'
EMPTY = None

def print_board(board):
#Prints the tictactoe board
    for row in board:
        print(' '.join(row))

def evaluate(board):
#Evaluates the board and returns current player's score.
#350 means the AI player wins and -350 means the human wins
    for i in range(3):
        # Checks rows
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == 'X':
                return 350
            elif board[i][0] == 'O':
                return -350
        # Checks columns
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == 'X':
                return 350
            elif board[0][i] == 'O':
                return -350
    # Checks diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 350
        elif board[0][0] == 'O':
            return -350
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 350
        elif board[0][2] == 'O':
            return -350
    # No winner
    return 0

def minimax(board, depth, is_maximizing):
#Uses the minimax algorithm to determine the best move for the AI
    score = evaluate(board)

    if score == 350:
        return score - depth
    elif score == -350:
        return score + depth
    elif not any('-' in row for row in board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    score = minimax(board, depth+1, False)
                    board[i][j] = '-'
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    score = minimax(board, depth+1, True)
                    board[i][j] = '-'
                    best_score = min(best_score, score)
        return best_score

def get_best_move(board):
#Gets the best move using minimax algorithm
    best_score = float('-inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = 'X'
                score = minimax(board, 0, False)
                board[i][j] = '-'
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

def play_game():
# Plays a game of Tic-Tac-Toe between a human player and an unbeatable AI player.
    board = [['-' for _ in range(3)] for _ in range(3)]
    print_board(board)
    while True:
        try:
            row, col = input("Enter row and column numbers (0-2) for your move: ").split()
            row = int(row)
            col = int(col)
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")
            continue
        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue
        if board[row][col] != '-':
            print("That position is already taken. Try again.")
            continue
        board[row][col] = 'O'
        print_board(board)
        if evaluate(board) == -350:
            print("You win!")
            break
        if not any('-' in row for row in board):
            print("The game is a tie.")
            break
        print("Thinking...")
        row, col = get_best_move(board)
        board[row][col] = 'X'
        print_board(board)
        if evaluate(board) == 350:
            print("You lose!")
            break
        if not any('-' in row for row in board):
            print("The game is a tie.")
            break


play_game() #runs the game
