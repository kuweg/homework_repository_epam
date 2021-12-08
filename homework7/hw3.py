"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from typing import Callable


def print_debugger(func) -> Callable:
    """Small decorator for debugging purposes."""
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f'{func.__name__} : {res}')
        return res
    return wrapper


# @print_debugger
def get_column(matrix: list, index: int) -> list:
    """Function which returns columns by index."""
    return [row[index] for row in matrix]


# @print_debugger
def get_diagonal(matrix: list, main: bool = True):
    """Returns a diagonals of matrix."""
    matrix_size = len(matrix)
    if main:
        diagonal = [matrix[i][i] for i in range(matrix_size)]
    else:
        diagonal = [matrix[matrix_size-i-1][i]
                    for i in range(matrix_size)]
    return diagonal


def check_winner(board: list, player: str) -> bool:
    """
    Checking horizontal, vertical and diagonal combinations
    for winner.
    """
    board_size = len(board)
    for i in range(board_size):
        if all([move == player for move in board[i][:]]):
            return True
        if all([move == player for move in get_column(board, i)]):
            return True
    if all([move == player for move in get_diagonal(board)]):
        return True
    if all([move == player for move in get_diagonal(board, main=False)]):
        return True
    return False


def check_completeness(board: list, empty_symbol: str = '-') -> bool:
    """Checking does board completed by finding corresponding empty symbols."""
    for _, sublist in enumerate(board):
        if empty_symbol in sublist:
            return True
    return False


# @print_debugger
def tic_tac_toe_checker(board: list) -> str:
    """Checking board accroding game's rules"""
    players = ['x', 'o']
    if check_winner(board, players[0]):
        return "x wins!"
    elif check_winner(board, players[1]):
        return "o wins!"
    elif check_completeness(board):
        return "unfinished!"
    else:
        return "draw!"


if __name__ == '__main__':
    board = [['o', 'o', 'x'],
             ['-', 'x', 'o'],
             ['x', 'o', '-']]

    # x wins!
    print(tic_tac_toe_checker(board))
