"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Count the number of X's and O's on the board
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    
    # X goes first, so if the counts are equal, it's X's turn
    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] != EMPTY:
        raise Exception("Invalid action")
    
    # Create a deep copy of the board
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    # No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Game is over if there is a winner or the board is full
    if winner(board) is not None:
        return True
    # Check if all cells are filled
    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    current_player = player(board)
    
    if current_player == X:
        # Maximize the value for X
        value, move = max_value(board)
    else:
        # Minimize the value for O
        value, move = min_value(board)
    
    return move


def max_value(board):
    """
    Helper function for Minimax: Maximizes the value for X.
    """
    if terminal(board):
        return utility(board), None
    
    v = float('-inf')
    best_move = None
    for action in actions(board):
        new_value, _ = min_value(result(board, action))
        if new_value > v:
            v = new_value
            best_move = action
        # Alpha-beta pruning optimization (optional)
        if v == 1:
            break
    return v, best_move


def min_value(board):
    """
    Helper function for Minimax: Minimizes the value for O.
    """
    if terminal(board):
        return utility(board), None
    
    v = float('inf')
    best_move = None
    for action in actions(board):
        new_value, _ = max_value(result(board, action))
        if new_value < v:
            v = new_value
            best_move = action
        # Alpha-beta pruning optimization (optional)
        if v == -1:
            break
    return v, best_move