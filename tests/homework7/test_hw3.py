from homework7.hw3 import tic_tac_toe_checker


x_win_board = [['o', 'o', 'x'],
               ['-', '-', 'x'],
               ['o', 'o', 'x']]

o_win_board = [['o', 'o', 'x'],
               ['-', 'o', '-'],
               ['o', 'o', 'x']]

draw_board = [['o', 'o', 'x'],
              ['x', 'x', 'o'],
              ['o', 'o', 'x']]

unfinished_board = [['o', 'o', 'x'],
                    ['-', '-', 'o'],
                    ['o', 'o', 'x']]


def test_x_wins():
    assert tic_tac_toe_checker(x_win_board) == "x wins!"


def test_o_wins():
    assert tic_tac_toe_checker(o_win_board) == "o wins!"


def test_draw():
    assert tic_tac_toe_checker(draw_board) == "draw!"


def test_unfinished_board():
    assert tic_tac_toe_checker(unfinished_board) == "unfinished!"
