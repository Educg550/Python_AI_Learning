"""
Tic Tac Toe Player
"""

import math

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
    xAmount = 0
    oAmount = 0
    for i in board:
        if i == X:
            xAmount += 1
        elif i == O:
            oAmount += 1
    if oAmount < xAmount:
        return O
    return X
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionsSet = set()
    for i in range(3):
        for j in range(3):
            if (board[i][j] == EMPTY):
                actionsSet.add((i, j))
    return actionsSet
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = board[:]
    newBoard[action[0]][action[1]] = player(board)
    return newBoard
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        # Linhas
        if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            if board[i][0] == X:
                return X
            elif board[i][0] == O:
                return O
        
        # Colunas
        if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            if board[0][i] == X:
                return X
            elif board[0][i] == O:
                return O
                
    # Diagonal principal
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        if board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O

    # Diagonal secundária
    if board[2][0] == board[1][1] and board[2][0] == board[0][2]:
        if board[2][0] == X:
            return X
        elif board[2][0] == O:
            return O
    return EMPTY
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if EMPTY not in board:
        return True
    return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winnerPlayer = winner(board)
    if winnerPlayer == X:
        return 1
    elif winnerPlayer == O:
        return -1
    return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    hipoBoard = board[:]
    possibleActions = actions(board)
    for action in possibleActions:
        hipoBoard[action[0]][action[1]] = player(board)
        if winner(hipoBoard) == player(board):
            return action
        return minimax(hipoBoard)
    raise NotImplementedError
