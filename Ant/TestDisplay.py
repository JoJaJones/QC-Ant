from constants import *
from Display import ScreenDisplay
from Position import Position
from ColorChangeBehavior import ColorChangeBehavior
from random import choice


colors = [color for color in SCREEN_COLOR_DICT]


test_board = []
for row in range(NUM_ROWS):
    test_board.append([])
    for col in range(NUM_COLS):
        test_board[row].append(Position(choice(colors), ColorChangeBehavior(colors, 3)))

displayObj = ScreenDisplay(test_board)
displayObj.render(test_board)
for row in test_board:
    for col in row:
        col.change_color()
print("\n\n\n\n")
displayObj.render(test_board)