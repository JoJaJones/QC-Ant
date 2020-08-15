from ColorChangeBehavior import ColorChangeBehavior
from Ant import Ant
from constants import *


class Position:
    def __init__(self, color="white", swap_rule = ColorChangeBehavior()): # todo (assign ant color to ants or to position)
        self.color = color
        self.old_ants = []
        self.new_ants = []
        self.dead_ants = []
        self.color_swapper = swap_rule

    def add_ant(self, ant: Ant, which_list: str):
        if which_list == DEAD:
            self.dead_ants.append(ant)
        elif which_list == NEW:
            self.new_ants.append(ant)
        else:
            self.new_ants.append(ant)

    def move_ant(self):
        cur_ant = self.old_ants[0]
        self.old_ants = self.old_ants[1:]
        move_res = cur_ant.move_ant(self.color)
        if move_res is not None:
            return cur_ant

        return None

    def is_occupied(self):
        return len(self.old_ants) > 0

    def change_color(self):
        self.color = self.color_swapper.handle_swap(self.color)

    def finalize_pos(self):
        self.old_ants =self.new_ants
        self.new_ants = []

    def get_color(self): # todo (modify so it returns ant color if ant present instead of position color)
        return self.color
