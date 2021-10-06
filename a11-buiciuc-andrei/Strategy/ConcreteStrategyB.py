import copy
import math
import random

from Strategy.Strategy import Strategy


class ConcreteStrategyB(Strategy):
    """
    Computer makes random moves, but blocks the player from winning whenever possible, and also moves to win
    when it is in a winning position, whenever possible
    """
    def make_move(self, board, computer_piece):
        # Store all possible moves here
        available_moves = board.get_available_moves()

        player_piece = 'O'
        if computer_piece == 'O':
            player_piece = 'X'

        column = random.choice(available_moves)

        for col in available_moves:
            board_copy = copy.deepcopy(board)
            row = board_copy.get_open_row(col)
            board_copy.drop_piece(row, col, player_piece)
            if board_copy.is_winning_move(player_piece):
                column = col
            board_copy_2 = copy.deepcopy(board)
            row2 = board_copy.get_open_row(col)
            board_copy_2.drop_piece(row, col, computer_piece)
            if board_copy_2.is_winning_move(computer_piece):
                column = col

        board.drop_piece(board.get_open_row(column), column, computer_piece)




