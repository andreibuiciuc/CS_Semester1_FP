from Board import Board


class Game:
    def __init__(self, context):
        self._board = Board()
        self._context = context

    @property
    def board(self):
        return self._board

    def human_move(self, row, column, human_piece):
        self._board.drop_piece(row, column, human_piece)

    def computer_move(self, computer_piece):
        self._context.make_move_logic(self._board, computer_piece)
