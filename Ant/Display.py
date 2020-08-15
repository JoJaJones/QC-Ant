from ShapeConverter import *
from ColorProcessor import *
from ColorTransmitter import *

class Display:
    def __init__(self, board, num_displays, display_config = None):
        self._board = None
        self._shape_converter = None
        self._color_processor = None
        self._color_transmitter = None

    def render(self, board):
        self._board = self._shape_converter.convert_shape(board)
        self._color_processor.process_colors(self._board)
        self._color_transmitter.transmit_colors(self._board)


class ScreenDisplay(Display):
    def __init__(self, board):
        self._board = [row[:] for row in board]
        self._shape_converter = BasicShapeConverter(len(board), len(board[0]))
        self._color_processor = ScreenColorProcessor()
        self._color_transmitter = ScreenColorTransmitter()