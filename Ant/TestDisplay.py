from constants import *
from Display import ScreenDisplay
from Position import Position
from Ant import Ant
from Board import Board
from time import sleep
from ColorChangeBehavior import ColorChangeBehavior
from random import choice


colors = [color for color in SCREEN_COLOR_DICT]


colors = ["cyan", "purple"]

test_board_positions = []
for row in range(NUM_ROWS):
    test_board_positions.append([])
    for col in range(NUM_COLS):
        test_board_positions[row].append(Position(swap_rule=ColorChangeBehavior(colors), color=colors[1], ant_color="red"))

mid_row = NUM_ROWS // 2
mid_col = NUM_COLS // 2
ant_starts = [(mid_row - 2, mid_col - 2), (mid_row - 2, mid_col + 1), (mid_row + 1, mid_col + 1),
              (mid_row + 1, mid_col - 2), (mid_row - 2, mid_col + 1), (mid_row + 1, mid_col + 1),
              (mid_row + 1, mid_col - 2), (mid_row - 2, mid_col - 2)] #, (6, 6), (6, NUM_COLS - 7), (NUM_ROWS - 7, NUM_COLS - 7), (NUM_ROWS - 7, 6)]
directions = [UP, RIGHT, DOWN, LEFT]
test_board = Board()
ant_list = []

for index, ant_pos in enumerate(ant_starts):
    test_ant = Ant(pos=ant_pos, direction = directions[index%4], color_list=colors)
    ant_list.append(test_ant)
    pos = test_ant.get_pos()
    r, c = pos
    test_board_positions[r][c].add_ant(test_ant, ALIVE)
    test_board.occupied_pos += [test_ant.get_pos()]

test_board.positions = test_board_positions


displayObj = ScreenDisplay(test_board_positions)
displayObj.render(test_board_positions)
i = 0
while True:
    # sleep(.1)
    print(f"\033[2J\033[H")
    test_board.move_all_ants()
    # if i > 20000:
    displayObj.render(test_board_positions)
    sleep(.1)
    i += 1
        # sleep(.1)

input()
