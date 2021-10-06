from texttable import Texttable


class Board:
    def __init__(self):
        self._rows = 6
        self._columns = 7
        self._data = [[' ' for j in range(self._columns)] for i in range(self._rows)]

    @property
    def get_rows(self):
        return self._rows

    @property
    def get_columns(self):
        return self._columns

    @property
    def get_board(self):
        return self._data

    def get_row(self, row):
        """
        Get the row array for a given row
        """
        row_list = []
        for column in range(self._columns):
            row_list.append(self._data[row][column])
        return row_list

    def get_column(self, column):
        """
        Get the column array for a given column
        """
        column_list = []
        for row in range(self._rows):
            column_list.append(self._data[row][column])
        return column_list

    def drop_piece(self, row, column, piece):
        """
        Drop the piece in the chosen position
        """
        self._data[row][column] = piece

    def is_valid(self, column):
        """
        Check whether a column is fully occupied or not
        """
        return self._data[0][column] == ' '

    def get_open_row(self, column):
        """
        Get the open row in order to place the piece in the desired column
        """
        for row in range(self._rows - 1, -1, -1):
            if self._data[row][column] == ' ':
                return row

    def get_available_moves(self):
        """
        Get a list of available moves = columns that are not fully occupied
        """
        available_moves = []
        for column in range(self._columns):
            if self.is_valid(column):
                available_moves.append(column)
        return available_moves

    def is_winning_move(self, piece):
        """
        We check all the possibilities for a winning move
        """

        # Check the horizontal wining position
        for column in range(self._columns-3):
            for row in range(self._rows):
                if self._data[row][column] == piece and self._data[row][column+1] == piece and \
                        self._data[row][column+2] == piece and self._data[row][column+3] == piece:
                    return True

        # Check the vertical wining position
        for column in range(self._columns):
            for row in range(self._rows-3):
                if self._data[row][column] == piece and self._data[row+1][column] == piece and \
                        self._data[row+2][column] == piece and self._data[row+3][column] == piece:
                    return True

        # Check the first diagonal wining position
        for column in range(self._columns-3):
            for row in range(self._rows-3):
                if self._data[row][column] == piece and self._data[row+1][column+1] == piece and \
                        self._data[row+2][column+2] == piece and self._data[row+3][column+3] == piece:
                    return True

        # Check the second diagonal wining position
        for column in range(self._columns-3):
            for row in range(3, self._rows):
                if self._data[row][column] == piece and self._data[row-1][column+1] == piece and \
                        self._data[row-2][column+2] == piece and self._data[row-3][column+3] == piece:
                    return True

    def score_position(self, piece):
        """
        We calculate the score of the board for the heuristic value (needed for AI implementation)
        For each winning case we create a list of possible outcomes that will be evaluated and scored.
        """
        score = 0

        # Score horizontal wining position
        for row in range(self._rows):
            row_list = self.get_row(row)
            for column in range(self._columns - 3):
                win_list = row_list[column:column + 4]
                score = score + self.evaluate(win_list, piece)

        # Score vertical wining position
        for column in range(self._columns):
            column_list = self.get_column(column)
            for row in range(self._rows - 3):
                win_list = column_list[row:row+4]
                score = score + self.evaluate(win_list, piece)

        # Score first diagonal wining position
        for row in range(self._rows-3):
            for column in range(self._columns-3):
                win_list = [self._data[row+index][column+index] for index in range(4)]
                score = score + self.evaluate(win_list, piece)

        # Score second diagonal wining position
        for row in range(self._rows-3):
            for column in range(self._columns-3):
                win_list = [self._data[row+3-index][column-index] for index in range(4)]
                score = score + self.evaluate(win_list, piece)

        # Score center column
        center_list = self.get_column(self._columns//2)
        count = center_list.count(piece)
        score = count * 3
        return score

    @staticmethod
    def evaluate(win_list, piece):
        """
        We evaluate a possible winning position by giving them a score.
        """
        score = 0
        opponent = 'O'
        if piece == 'O':
            opponent = 'X'

        count = win_list.count(piece)
        count_free = win_list.count(' ')
        count_opponent = win_list.count(opponent)
        if count == 4:
            score += 100
        elif count == 3 and count_free == 1:
            score += 7
        elif count == 2 and count_free == 2:
            score += 3

        if count_opponent == 3 and count_free == 1:
            score = score - 5

        return score

    def __str__(self):
        t = Texttable()
        t.header(['0', '1', '2', '3', '4', '5', '6'])
        for row in range(6):
            row_data = []

            for index in self._data[row]:
                row_data.append(index)
            t.add_row(row_data)

        return t.draw()


b = Board()
print(str(b))
