from constants import *
from Display import ScreenDisplay
from Position import Position
from Ant import Ant
from Board import Board
from time import sleep
from ColorChangeBehavior import ColorChangeBehavior
from random import choice


colors = [color for color in SCREEN_COLOR_DICT]


test_board_positions = []
for row in range(NUM_ROWS):
    test_board_positions.append([])
    for col in range(NUM_COLS):
        test_board_positions[row].append(Position())
test_ant = Ant(pos=(25, 25), direction=LEFT)
pos = test_ant.get_pos()
r, c = pos
test_board_positions[r][c].add_ant(test_ant, ALIVE)
test_board = Board()
test_board.positions = test_board_positions
test_board.occupied_pos = [test_ant.get_pos()]

displayObj = ScreenDisplay(test_board_positions)
displayObj.render(test_board_positions)
for i in range(15000):
    # sleep(.1)
    print("\033[2J\033[H")
    test_board.move_all_ants()
    if i % 10 == 0 and i > 10000:
        displayObj.render(test_board_positions)
        sleep(.1)
        # sleep(.1)

input()