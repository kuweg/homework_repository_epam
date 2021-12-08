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

import numpy as np


def print_debugger(func) -> Callable:
    """Small decorator for debugging purposes."""
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f'{func.__name__} : {res}')
        return res
    return wrapper


def check_winner(board: np.array, player: str) -> bool:
    """
    Checking horizontal, vertical and diagonal combinations
    for winner.
    """
    board_size = board.shape[0]
    for i in range(board_size):
        if all([move == player for move in board[i, :]]):
            return True
        if all([move == player for move in board[:, i]]):
            return True
    if all([move == player for move in board.diagonal()]):
        return True
    if all([move == player for move in np.fliplr(board).diagonal()]):
        return True
    return False


def check_completeness(board: np.array, empty_symbol: str = '-') -> bool:
    """Checking does board completed by finding corresponding empty symbols."""
    for _, sublist in enumerate(board):
        if empty_symbol in sublist:
            return True
    return False


# @print_debugger
def tic_tac_toe_checker(board: list) -> str:
    """Checking board accroding game's rules"""
    players = ['x', 'o']
    board = np.array(board)
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
             ['-', '-', 'x'],
             ['o', 'o', 'x']]

    # x wins!
    print(tic_tac_toe_checker(board))
