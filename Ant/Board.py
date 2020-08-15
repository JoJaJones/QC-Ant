from Ant import Ant
from Position import Position
from constants import *

class Board:
    def __init__(self):
        self.occupied_pos = []
        self.positions = []

    def move_all_ants(self):
        new_pos = set()
        for pos in self.occupied_pos:
            r, c = pos
            self.positions[r][c].change_color()
            while self.positions[r][c].is_occupied():
                ant = self.positions[r][c].move_ant()
                if ant is not None:
                    ant_r, ant_c = ant.get_pos()
                    if ant.is_dead():
                        self.positions[ant_r][ant_c].add_ant(ant, DEAD)
                    else:
                        self.positions[ant_r][ant_c].add_ant(ant, ALIVE)
                        new_pos.add((ant_r, ant_c))

        for pos in new_pos:
            r, c = pos
            self.positions[r][c].finalize_pos()

        self. occupied_pos = list(new_pos)

