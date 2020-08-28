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
ant_starts = [(19, 19), (19, 22), (22, 22), (22, 19)]
directions = [UP, RIGHT, DOWN, LEFT]
test_board = Board()
ant_list = []

for index, ant_pos in enumerate(ant_starts):
    test_ant = Ant(pos=ant_pos, direction = directions[index])
    ant_list.append(test_ant)
    pos = test_ant.get_pos()
    r, c = pos
    test_board_positions[r][c].add_ant(test_ant, ALIVE)
    test_board.occupied_pos += [test_ant.get_pos()]

test_board.positions = test_board_positions


displayObj = ScreenDisplay(test_board_positions)
displayObj.render(test_board_positions)
while True:
    # sleep(.1)
    print(f"\033[2J\033[H")
    test_board.move_all_ants()
    displayObj.render(test_board_positions)
    sleep(.25)
        # sleep(.1)

input()
