from abc import ABC, abstractmethod


class Strategy(ABC):
    """
    The Strategy Interface declares operations common to all versions of some algorithm
    """
    @abstractmethod
    def make_move(self, board, computer_piece):
        pass


class Context:
    """
    The Context defines the interface if interest for players
    It directs to the desired algorithm based on a given strategy

    The algorithms are called Concrete Strategies and are all inherited from a general, abstract class named
    Strategy. 
    """
    def __init__(self, strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, value):
        self._strategy = value

    def make_move_logic(self, board, computer_piece):
        self._strategy.make_move(board, computer_piece)
