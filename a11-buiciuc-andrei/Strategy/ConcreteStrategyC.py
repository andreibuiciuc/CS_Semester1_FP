import copy
import math
import random

from Strategy.Strategy import Strategy


class ConcreteStrategyC(Strategy):
    """
    Computer makes calculated moves and tries to maximise its chances to win
    Minimax Algorithm with alpha - beta pruning
    Here we also have the methods corresponding to all calculation for the ai algorithm
    """

    @staticmethod
    def terminal_node(board, piece):
        computer_piece = 'O'
        if piece == 'O':
            computer_piece = 'X'
        return board.is_winning_move(piece) or board.is_winning_move(computer_piece) \
            or len(board.get_available_moves()) == 0

    def minimax(self, board, piece, depth, alpha, beta, maximizing_player):
        computer_piece = 'O'
        if piece == 'O':
            computer_piece = 'X'

        available_moves = board.get_available_moves()
        is_terminal_node = self.terminal_node(board, piece)

        if depth == 0 or is_terminal_node:
            if is_terminal_node:
                if board.is_winning_move(computer_piece):
                    return None, math.inf
                elif board.is_winning_move(piece):
                    return None, -math.inf
                else:
                    return None, 0
            else:
                return None, board.score_position(computer_piece)

        if maximizing_player:
            value = -math.inf
            column = random.choice(available_moves)
            for c in available_moves:
                row = board.get_open_row(c)
                board_copy = copy.deepcopy(board)
                board_copy.drop_piece(row, c, computer_piece)
                new_score = self.minimax(board_copy, piece, depth-1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = c
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value
        else:
            value = math.inf
            column = random.choice(available_moves)
            for c in available_moves:
                row = board.get_open_row(c)
                board_copy = copy.deepcopy(board)
                board_copy.drop_piece(row, c, piece)
                new_score = self.minimax(board_copy, piece, depth-1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    column = c
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value

    def make_move(self, board, computer_piece):
        piece = 'O'
        if computer_piece == 'O':
            piece = 'X'

        column, score = self.minimax(board, piece, 5, -math.inf, math.inf, True)
        row = board.get_open_row(column)
        board.drop_piece(row, column, computer_piece)



