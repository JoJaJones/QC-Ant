from Board import Board
from Display import ScreenDisplay
from random import randint, choice
from constants import *

class Menu:
    def __init__(self):
        self.board = Board()
        self.display = ScreenDisplay(self.board.get_positions())
        self.settings_funct_dict = {
            "1": self.get_pos,
            "2": self.get_dir,
            "3": self.get_ant_color
        }

    def get_pos(self, ant_settings, random_select: bool = False):
        row = self.get_valid_int(PROMPT_DICT[POS][0], 0, NUM_ROWS - 1, random_select)
        col = self.get_valid_int(PROMPT_DICT[POS][1], 0, NUM_COLS - 1, random_select)
        ant_settings[POS] = row, col

    def get_dir(self, ant_settings, random_select: bool = False):
        prompt = self.generate_prompt_from_dictionary(PROMPT_DICT[DIR], list(DIR_OPTIONS.keys()))
        ant_settings[DIR] = self.get_valid_from_list(prompt, dict(DIR_OPTIONS.items()), random_select)

    # TODO add functionality for limited color choices (maybe)
    def get_ant_color(self, ant_settings, random_select: bool = False, color_options = None):
        prompt = self.generate_prompt_from_dictionary(PROMPT_DICT[COLOR], list(ANT_COLOR_OPTIONS.keys()))
        ant_settings[COLOR] = self.get_valid_from_list(prompt, dict(ANT_COLOR_OPTIONS.items()), random_select)

    def main_menu(self):
        run = True
        while run:
            choice = input("1 - Run Langston's Ant Simulation\n"
                           "0 - Quit")
            try:
                choice = int(choice)
            except:
                print("Invalid entry please try again")

            if choice == 1:
                self.ant_menu()
            elif choice == 0:
                run = False

    def ant_menu(self):
        invalid = True
        while invalid:
            invalid = False

            num_steps = input("How many steps would you like the simulation to run for (0 for endless)? ")
            try:
                num_steps = int(num_steps)
            except:
                print("Invalid selection please input a whole number")
                invalid = True

        self.setup_ant_sim()

        self.run_ant_run(num_steps)

    def run_ant_run(self, num_steps):
        while num_steps != 0:
            self.board.move_all_ants()
            self.display.render(self.board.get_positions())

            num_steps -= 1

    def setup_ant_sim(self):
        raise NotImplementedError

    def make_ant(self, settings: dict = None):
        if settings is None:
            settings = self.generate_default_ant_dict()
        new_ant = Ant(pos=settings[POS], direction=settings[DIR], color=settings[COLOR])
        self.board.add_ant(new_ant)

    def get_ant_settings(self, default_color: str = None) -> dict:
        ant_settings = self.generate_default_ant_dict()
        if default_color:
            ant_settings[COLOR] = default_color

        choice = None
        remaining_settings_to_choose = dict(ANT_SETTING_CHOICE.items())
        while len(remaining_settings_to_choose) > 2 and choice != "R" and choice != "D":
            prompt = self.generate_prompt_from_dictionary(PROMPT_DICT[SETTING_CHOICE], remaining_settings_to_choose)
            choice = self.get_valid_from_list(prompt, remaining_settings_to_choose)

            if choice == "R":
                self.generate_random_settings(ant_settings, PROMPT_DICT, remaining_settings_to_choose)
            elif choice != "D":
                self.settings_funct_dict[choice](ant_settings)
                del remaining_settings_to_choose[choice]
            elif choice == "3":
                # TODO add limited color options functionality
                self.settings_funct_dict[choice](ant_settings)
            else:
                self.settings_funct_dict[choice](ant_settings)

        return ant_settings

    def generate_prompt_from_dictionary(self, prompt_header: dict, list_of_keys: list = None) -> str:
        prompt = prompt_header[PROMPT]

        if list_of_keys is not None:
            options_to_add = list_of_keys
        else:
            options_to_add = list(prompt_header[OPTIONS].keys())

        for option in options_to_add:
            prompt += f"{option} - {prompt_header[OPTIONS][option]}\n"

        return prompt

    def get_valid_int(self, prompt: str, min_val: int = None, max_val: int = None, random_choice: bool = False) -> int:
        if not random_choice:
            is_valid = False
            while not is_valid:
                is_valid = True
                try:
                    selection = int(input(prompt))
                except:
                    is_valid = False

                if is_valid:
                    is_valid = self.is_num_valid(selection, min_val, max_val)
        else:
            selection = randint(min_val, max_val)

        return selection

    def is_num_valid(self, num, min_val = None, max_val = None):
        if min_val is not None and num < min_val:
            return False

        if max_val is not None and num < max_val:
            return False

        if type(num) != int and type(num) != float:
            return False

        return True

    def get_valid_char(self, prompt: str, valid_choices) -> str:
        res = ""
        while len(res) < 1 or not res[0].upper() not in valid_choices:
            res = input(prompt)

        return res[0]

    def get_valid_from_list(self, prompt: str, valid_options: dict, random_choice: bool = False):
        # get list of options from dict, call get_valid_char
        valid_choices = list(valid_options.keys())
        choice = self.get_valid_char(prompt, valid_choices)
        return choice

    def design_menu(self):
        # present the options
        invalid = True
        while invalid:
            invalid = False
            try:
                design_type = int(input("1 - radial symmetry\n"
                                        "2 - choose specific design\n"))
            except:
                invalid = True

            if (design_type != 1 and design_type != 2) or invalid:
                print("Invalid selection please choose from the options listed")
        if design_type == 1:
            invalid = True
            num_sym_axes = num_ants_to_pick = None
            while invalid:
                invalid = False
                num_sym_axes = input("How many axes of symmetry do you want (2 or 4)?")
                num_ants_to_pick = input("How many ants would you like to set per axis?")
                try:
                    num_sym_axes = int(num_sym_axes)
                    num_ants_to_pick = int(num_ants_to_pick)
                except:
                    invalid = True

                if (num_sym_axes != 2 and num_sym_axes != 4) or invalid:
                    print("Invalid selection please input valid whole number choices")
            # get option for user selected ants
            ant_options = []
            while len(ant_options) < num_ants_to_pick:
                ant_options += self.get_ant_settings()

            for option in ant_options:
                ant_options += self.generate_symmetrical_ants(option, num_sym_axes)

            for settings in ant_options:
                self.make_ant(settings)
        else:
            invalid = True
            while invalid:
                invalid = False
                prompt = ""
                for num, pattern in DESIGN_DICT.items():
                    prompt += f"{num} - {pattern[0]}\n"
                try:
                    which_pattern = int(input(prompt))
                except:
                    invalid = True

                if invalid or which_pattern not in DESIGN_DICT:
                    print("Invalid selection please choose from the options listed")

            # logic for setting up design
        # use chosen options to setup the sim
        raise NotImplementedError

    def generate_random_settings(self, settings_dict: dict, remaining_settings: dict):
        for key in remaining_settings:
            self.settings_funct_dict[key](settings_dict, True)

    def generate_symmetrical_ants(self, option: dict, num_axes: int) -> list:
        raise NotImplementedError

    def generate_default_ant_dict(self) -> dict:
        ant_dict = {}
        ant_dict[DIR] = RIGHT
        ant_dict[POS] = NUM_ROWS//2, NUM_COLS//2
        ant_dict[COLOR] = "blue"

        return ant_dict

if __name__ == "__main__":
    menu = Menu()
    menu.main_menu()