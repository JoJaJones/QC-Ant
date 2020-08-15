class ColorTransmitter:
    def __init__(self):
        pass

    def transmit_colors(self, board):
        raise NotImplementedError


class ScreenColorTransmitter(ColorTransmitter):
    def transmit_colors(self, board):
        for row in board:
            for col in row:
                print(f"\033[{col}m   ", end="\033[m")
            print()