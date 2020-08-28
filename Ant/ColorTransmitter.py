class ColorTransmitter:
    def __init__(self):
        pass

    def transmit_colors(self, board):
        raise NotImplementedError


class ScreenColorTransmitter(ColorTransmitter):
    def transmit_colors(self, board):
        print("╔═", end = "")
        for col in board[0]:
            print("═══", end = "")
        print("═╗")
        for row in board:
            print("║ ", end="")
            for col in row:
                print(f"\033[{col}m   ", end="\033[m")
            print(" ║")
        print("╚═", end="")
        for col in board[0]:
            print("═══", end="")
        print("═╝")
