import math
HUMAN = 'O'
AI = 'X'
EMPTY = ' '
board = [EMPTY] * 9
def print_board(board):
    for row in [board[i:i + 3] for i in range(0, 9, 3)]:
        print('|'.join(row))
        print("-" * 5)
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6] 
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False
def is_draw(board):
    return EMPTY not in board
def get_available_moves(board):
    return [i for i, spot in enumerate(board) if spot == EMPTY]
def minimax(board, depth, is_maximizing):
    if check_winner(board, AI):
        return 10 - depth
    if check_winner(board, HUMAN):
        return depth - 10
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(board):
            board[move] = AI
            score = minimax(board, depth + 1, False)
            board[move] = EMPTY
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(board):
            board[move] = HUMAN
            score = minimax(board, depth + 1, True)
            board[move] = EMPTY
            best_score = min(score, best_score)
        return best_score
    
def ai_move(board):
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move] = AI
        score = minimax(board, 0, False)
        board[move] = EMPTY
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move] = AI

def human_move(board):
    while True:
        move = int(input("Enter your move (1-9): ")) - 1
        if move in get_available_moves(board):
            board[move] = HUMAN
            break
        else:
            print("Invalid move! Try again.")

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        human_move(board)
        print_board(board)
        
        if check_winner(board, HUMAN):
            print("You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        ai_move(board)
        print("AI's move:")
        print_board(board)

        if check_winner(board, AI):
            print("AI wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break
if __name__ == "__main__":
    play_game()
