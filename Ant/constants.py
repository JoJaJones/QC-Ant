UP = "UP"
RIGHT = "RIGHT"
DOWN = "DOWN"
LEFT = "LEFT"

POS = "position"
DIR = "direction"
COLOR = "color"
SETTING_CHOICE = "ant setting choice"
PROMPT = "prompt"
OPTIONS = "options"

SIZE_OF_BOARD = 64
NUM_ROWS = 34
NUM_COLS = 40

DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

DIR_DICT = {UP: (-1, 0), DOWN: (1, 0), LEFT: (0, -1), RIGHT: (0, 1)}

ALIVE = "alive"
DEAD = "dead"
NEW = "new"

SCREEN_COLOR_DICT = {"white": 40, "red": 41, "green": 42, "blue": 44, "purple": 45, "teal": 46,
                     "dark gray": 100, "light red": 101, "yellow": 103,
                     "cyan": 106, "black": 107}

ANT_COLOR_OPTIONS = {x + 1: color for x, color in enumerate(SCREEN_COLOR_DICT.keys())}
DIR_OPTIONS = {idx + 1: direction for idx, direction in enumerate(DIRECTIONS)}
ANT_SETTING_CHOICES = {"1": "Position", "2": "Direction", "3": "Ant color", "D": "Use defaults", "R": "Generate random selections"}

PROMPT_DICT = {
    POS: [f"Which row number would you like the ant in (0-{NUM_ROWS})?", f"Which col number would you like the ant in (0-{NUM_COLS})?"],
    DIR: {PROMPT: "Which direction would you like?\n",
          OPTIONS: DIR_OPTIONS},
    COLOR: {PROMPT: "Which color for the ant?\n",
            OPTIONS: ANT_COLOR_OPTIONS},
    SETTING_CHOICE: {PROMPT: "Which setting for the ant would you like to set?\n",
                     OPTIONS: ANT_SETTING_CHOICES}
}

DESIGN_DICT = {1: ["cyclic flower"], 2: ["star"], 3: ["flower"]}