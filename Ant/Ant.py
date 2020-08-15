from MoveBehavior import MoveBehavior
from EdgeBehavior import EdgeBehavior
from TurnBehavior import TurnBehavior
from constants import *

class Ant:
    def __init__(self, speed = 1, edge_type = "T", turn_type = 1, pos = (0,1), direction = UP, num_colors = 2):
        self.direction = direction
        self.pos = pos
        self.turn_behavior = TurnBehavior(turn_type, num_colors)
        self.move_behavior = MoveBehavior(speed)
        self.edge_behavior = EdgeBehavior(self.turn_behavior, self.move_behavior, NUM_ROWS, NUM_COLS)

    def move_ant(self, color):
        # move logic
        next_r, next_c = self.move_behavior.move(self.pos, self.direction)
        signal = None
        if min(next_r, next_c) < 0 or next_r >= NUM_ROWS or next_c >= NUM_COLS:
            # edge bx
            edge_res = self.edge_behavior(self.pos, self.direction)
            if edge_res is None:
                signal = None
            else:
                signal = edge_res
                self.pos = edge_res
        else:
            signal = next_r, next_c
            self.pos = signal

        return

    def get_pos(self):
        return self.pos

    def is_dead(self):
        return self.move_behavior.get_move_distance() == 0

