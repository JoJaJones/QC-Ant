from constants import *
from Display import ScreenDisplay
from Position import Position
from Ant import Ant
from Board import Board
from time import sleep
from ColorChangeBehavior import ColorChangeBehavior
from random import choice


colors = [color for color in SCREEN_COLOR_DICT]


colors = ["white", "blue"]

# mid_row = NUM_ROWS // 2
# mid_col = NUM_COLS // 2
# ant_starts = [(mid_row - 2, mid_col - 2), (mid_row - 2, mid_col + 1), (mid_row + 1, mid_col + 1),
#               (mid_row + 1, mid_col - 2), (mid_row - 2, mid_col + 1), (mid_row + 1, mid_col + 1),
#               (mid_row + 1, mid_col - 2), (mid_row - 2, mid_col - 2)]
# """, (6, 6), (6, NUM_COLS - 7),
#               (NUM_ROWS - 7, NUM_COLS - 7), (NUM_ROWS - 7, 6), (6, NUM_COLS - 7),
#               (NUM_ROWS - 7, NUM_COLS - 7), (NUM_ROWS - 7, 6), (6, 6)]"""
# directions = [UP, RIGHT, DOWN, LEFT]
test_board = Board()
# ant_list = []
test_board.add_ant(Ant(pos=(16, 16), direction=UP))
# for index, ant_pos in enumerate(ant_starts):
#     test_ant = Ant(pos=ant_pos, direction = directions[index%4])
#     ant_list.append(test_ant)
#     pos = test_ant.get_pos()
#     r, c = pos
#     test_board.add_ant(test_ant)

displayObj = ScreenDisplay(test_board.get_positions())
displayObj.render(test_board.get_positions())
i = 0
while True:
    # sleep(.1)
    print(f"\033[2J\033[H")
    test_board.move_all_ants()
    # if i > 20000:
    displayObj.render(test_board.get_positions())
    sleep(.1)
    i += 1
        # sleep(.1)

input()
