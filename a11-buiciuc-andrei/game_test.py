import unittest

from Game import Game
from Strategy.ConcreteStrategyA import ConcreteStrategyA
from Strategy.ConcreteStrategyB import ConcreteStrategyB
from Strategy.ConcreteStrategyC import ConcreteStrategyC
from Strategy.Strategy import Context


class TestGame(unittest.TestCase):
    def test_game_a(self):
        context = Context(ConcreteStrategyA())
        game = Game(context)
        board = game.board

        game.human_move(5, 0, 'X')
        self.assertEqual(game.board.get_board[5][0], 'X')

        game.computer_move('O')
        print(str(board))

        okay = False
        for i in range(6):
            for j in range(7):
                if game.board.get_board[i][j] == 'O':
                    okay = True
                    break

        self.assertEqual(okay, True)

    def test_game_b(self):
        context = Context(ConcreteStrategyB())
        game = Game(context)
        board = game.board

        game.human_move(5, 0, 'X')
        self.assertEqual(game.board.get_board[5][0], 'X')

        game.computer_move('O')
        print(str(board))

        okay = False
        for i in range(6):
            for j in range(7):
                if game.board.get_board[i][j] == 'O':
                    okay = True
                    break

        self.assertEqual(okay, True)

    def test_game_c(self):
        context = Context(ConcreteStrategyC())
        game = Game(context)
        board = game.board

        game.human_move(5, 0, 'X')
        self.assertEqual(game.board.get_board[5][0], 'X')

        game.computer_move('O')
        print(str(board))

        okay = False
        for i in range(6):
            for j in range(7):
                if game.board.get_board[i][j] == 'O':
                    okay = True
                    break

        self.assertEqual(okay, True)
