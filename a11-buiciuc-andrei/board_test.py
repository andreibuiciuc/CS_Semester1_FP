import unittest
from unittest import TestCase

from Board import Board


class TestBoard(TestCase):
    def test_board(self):
        board = Board()

        self.assertEqual(6, board.get_rows)
        self.assertEqual(7, board.get_columns)

        row = []
        for i in range(7):
            row.append(' ')
        self.assertEqual(row, board.get_row(1))

        col = []
        for j in range(6):
            col.append(' ')
        self.assertEqual(col, board.get_column(1))

        moves = []
        for i in range(7):
            moves.append(i)
        self.assertEqual(moves, board.get_available_moves())

        board.drop_piece(5, 0, 'X')
        self.assertEqual(board.get_board[5][0], 'X')

        board.drop_piece(4, 0, 'X')
        self.assertEqual(board.get_board[5][0], 'X')

        board.drop_piece(3, 0, 'X')
        self.assertEqual(board.get_board[3][0], 'X')

        board.drop_piece(2, 0, 'X')
        self.assertEqual(board.get_board[2][0], 'X')

        self.assertEqual(board.is_winning_move('X'), True)

        board.drop_piece(5, 2, 'O')
        self.assertEqual(board.get_board[5][2], 'O')

        board.drop_piece(5, 3, 'O')
        self.assertEqual(board.get_board[5][3], 'O')

        board.drop_piece(5, 4, 'O')
        self.assertEqual(board.get_board[5][4], 'O')

        board.drop_piece(5, 5, 'O')
        self.assertEqual(board.get_board[5][5], 'O')

        self.assertEqual(board.is_winning_move('O'), True)

        row = board.get_open_row(0)
        self.assertEqual(row, 1)

        row2 = board.get_open_row(4)
        self.assertEqual(row2, 4)

    def test_eval(self):
        board = Board()
        eval1 = ['X', 'X', 'X', 'X']
        self.assertEqual(board.evaluate(eval1, 'X'), 100)

        eval2 = ['X', 'X', 'X', ' ']
        self.assertEqual(board.evaluate(eval2, 'X'), 7)

        eval3 = ['X', 'X', ' ', ' ']
        self.assertEqual(board.evaluate(eval3, 'X'), 3)

        eval4 = [' ', 'O', 'O', 'O']
        self.assertEqual(board.evaluate(eval4, 'X'), -5)


unittest.main()
