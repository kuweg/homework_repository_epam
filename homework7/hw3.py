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
from typing import List


def get_column(matrix: List[list], index: int) -> list:
    """Function which returns columns by index."""
    return [row[index] for row in matrix]


def get_diagonal(matrix: List[list], main: bool = True):
    """Returns a diagonals of matrix."""
    matrix_size = len(matrix)
    if main:
        diagonal = [sublist[pos] for pos, sublist in enumerate(matrix)]
    else:
        diagonal = [
            sublist[matrix_size - pos - 1]
            for pos, sublist in enumerate(matrix)
        ]
    return diagonal


def make_combinations(board: List[list]) -> list:
    combinations = []
    for pos, line in enumerate(board):
        combinations.append(line)
        combinations.append(get_column(board, pos))
    combinations.append(get_diagonal(board))
    combinations.append(get_diagonal(board, main=False))

    return combinations


def is_complete(board: List[list], empty_symbol: str = "-") -> bool:
    """Checking does board completed by finding corresponding empty symbols."""
    for _, sublist in enumerate(board):
        if empty_symbol in sublist:
            return False
    return True


def tic_tac_toe_checker(board: List[list]) -> str:
    """Checking board accroding game's rules"""
    combinations = make_combinations(board)
    for comb in combinations:
        if len(set(comb)) == 1:
            return f"{comb[0]} wins!"
    if not is_complete(board):
        return "unfinished!"
    return "draw!"


if __name__ == "__main__":
    board = [["o", "o", "x"], ["-", "x", "o"], ["x", "o", "-"]]

    # x wins!
    tic_tac_toe_checker(board)
