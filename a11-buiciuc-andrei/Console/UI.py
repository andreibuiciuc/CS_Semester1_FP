from Game import Game


class GameException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return str(self._msg)


class UI:
    def __init__(self, context):
        self._context = context
        self._game = Game(self._context)

    @staticmethod
    def welcome():
        print("\nHello and welcome to Connect4. Let's play!")

    @staticmethod
    def read_human_move():
        column = int(input("Make a move (0 - 6): "))
        if column < 0 or column > 6:
            raise GameException("Invalid input!")
        return column

    @staticmethod
    def read_human_piece():
        human_piece = input("Choose your piece (X or O) : ")
        if human_piece not in ['X', 'O']:
            raise GameException("Invalid input!")
        return human_piece

    def start(self):
        self.welcome()

        done_s = False
        done = False
        human_turn = True

        computer_piece = None
        human_piece = None

        while not done_s:
            try:
                human_piece = self.read_human_piece()
                if human_piece == 'X':
                    computer_piece = 'O'
                    done_s = True
                elif human_piece == 'O':
                    computer_piece = 'X'
                    done_s = True
            except GameException as error:
                print(str(error))

        while not done:
            print(str(self._game.board))
            column = None
            if human_turn:
                done_c = False
                while not done_c:
                    try:
                        column = self.read_human_move()
                        if 0 <= column <= 6:
                            done_c = True
                    except (GameException, ValueError) as error:
                        print(str(error))

                if self._game.board.is_valid(column):
                    row = self._game.board.get_open_row(column)
                    self._game.human_move(row, column, human_piece)

                    if self._game.board.is_winning_move(human_piece):
                        print(str(self._game.board))
                        print("You win!!")
                        done = True

            else:
                self._game.computer_move(computer_piece)
                if self._game.board.is_winning_move(computer_piece):
                    print(str(self._game.board))
                    print("Computer wins!!")
                    done = True

            human_turn = not human_turn
