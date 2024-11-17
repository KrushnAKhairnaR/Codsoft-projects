import math

EMPTY = '-'
AI_PLAYER = 'X'
HUMAN_PLAYER = 'O'


def check_winner(board, player):
    return any(all(cell == player for cell in row) for row in board) \
        or any(all(board[i][j] == player for i in range(3)) for j in range(3)) \
        or all(board[i][i] == player for i in range(3)) \
        or all(board[i][2 - i] == player for i in range(3))


def is_board_full(board):
    return all(cell != EMPTY for row in board for cell in row)


def evaluate(board):
    if check_winner(board, AI_PLAYER):
        return 1
    elif check_winner(board, HUMAN_PLAYER):
        return -1
    else:
        return 0

def minimax(board, depth, alpha, beta, is_maximizing):
    score = evaluate(board)
    if score != 0 or is_board_full(board):
        return score
    
    if is_maximizing:
        max_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI_PLAYER
                    max_score = max(max_score, minimax(board, depth + 1, alpha, beta, False))
                    board[i][j] = EMPTY
                    alpha = max(alpha, max_score)
                    if beta <= alpha:
                        break
        return max_score
    else:
        min_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN_PLAYER
                    min_score = min(min_score, minimax(board, depth + 1, alpha, beta, True))
                    board[i][j] = EMPTY
                    beta = min(beta, min_score)
                    if beta <= alpha:
                        break
        return min_score


def ai_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI_PLAYER
                score = minimax(board, 0, -math.inf, math.inf, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move


def print_board(board):
    for row in board:
        print(" | ".join(row))
    print()


def play_tic_tac_toe():
    board = [[EMPTY] * 3 for _ in range(3)]
    print("Welcome to Jidnesh's Tic-Tac-Toe Game!")
    print("The board is represented as follows: The AI plays as  X and you play as O.")
    print_board(board)
    while not is_board_full(board):
        # AI's move
        ai_row, ai_col = ai_move(board)
        board[ai_row][ai_col] = AI_PLAYER
        print("AI's move:")
        print_board(board)
        if check_winner(board, AI_PLAYER):
            print("AI wins!")
            return
        elif is_board_full(board):
            print("It's a draw!")
            return
        
        while True:
            try:
                human_row = int(input("Enter row (0, 1, or 2): "))
                human_col = int(input("Enter column (0, 1, or 2): "))
                if board[human_row][human_col] != EMPTY:
                    print("Cell already occupied! Try again.")
                else:
                    break
            except ValueError:
                print("Invalid input! Please enter integers.")
        board[human_row][human_col] = HUMAN_PLAYER
        print("Your move:")
        print_board(board)
        if check_winner(board, HUMAN_PLAYER):
            print("You win!")
            return
    print("It's a draw!")

# Start the game
play_tic_tac_toe()
