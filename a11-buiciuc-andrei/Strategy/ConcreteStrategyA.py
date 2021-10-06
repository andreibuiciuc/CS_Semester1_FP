import random

from Strategy.Strategy import Strategy


class ConcreteStrategyA(Strategy):
    """
    Computer makes a random but valid move
    """

    def make_move(self, board, computer_piece):
        # Store all possible moves here.
        available_move = board.get_available_moves()

        # Pick one of the available moves
        column = random.choice(available_move)
        row = board.get_open_row(column)
        return board.drop_piece(row, column, computer_piece)
