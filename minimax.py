# A minimax alogrithm to find the next best move in TicTacToe
import math
import numpy as np
player = 'X'
computer = 'O'

def find_best_move(board):
    best_move = None
    best_val = 1000

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                board[i][j] = computer

                val = __minimax(board, 0,  False)

                board[i][j] = 0

                if val < best_val:
                    best_val = val
                    best_move = (i, j)

    return best_move


def __minimax(board, depth, isMax):
    score = evaluate(board)

    if score == 10 or score == -10:
        return score

    if not move_left(board):
        return 0

    if isMax:
        best_val = -math.inf

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    board[i][j] = computer
                    val = __minimax(board, depth + 1, False)
                    best_val = max(val, best_val)
                    board[i][j] = 0
        return best_val
    else:
        best_val = math.inf
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    board[i][j] = player
                    val = __minimax(board,  depth + 1, True)
                    best_val = min(val, best_val)
                    board[i][j] = 0
        return best_val


def evaluate(board):
    global player
    global computer
    for i in range(3):
        # Checking horizontally
        if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            if board[i][0] == player:
                return +10
            elif board[i][0] == computer:
                return -10

        # Checking vertically
        if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            if board[0][i] == player:
                return +10
            elif board[0][i] == computer:
                return -10

    # Checking diagonally
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        if board[0][0] == player:
            return +10
        elif board[0][0] == computer:
            return -10

    if board[0][2] == board[1][1] and board[0][0] == board[2][0]:
        if board[0][2] == player:
            return +10
        elif board[0][2] == computer:
            return -10

    return 0


def move_left(board):
    for row in board:
        for item in row:
            if item == 0:
                return True
    return False
