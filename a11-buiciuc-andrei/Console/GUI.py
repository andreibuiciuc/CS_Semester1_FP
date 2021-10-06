import math
import sys

import pygame

from Game import Game


class GUI:
    def __init__(self, context):
        self._context = context
        self._game = Game(self._context)

    def draw_board(self, screen, screen_size):
        """
        For drawing the board, we will draw for each cell in the matrix a blue rectangle (square), and if the cell is
        occupied by a piece, we will draw for that cell a red / yellow circle depending on the nature of the piece
        """

        # We initialize pygame colors - given as r-g-b
        blue = pygame.Color(0, 0, 250)
        red = pygame.Color(255, 0, 0)
        yellow = pygame.Color(255, 255, 0)
        # We initialize the size of a square on the board
        size = 100

        # We initialize the radius for a circle representing a piece
        radius = size // 2

        for column in range(self._game.board.get_columns):
            for row in range(self._game.board.get_rows):
                # in pygame, rect(surface, color, rect, width=0)
                pygame.draw.rect(screen, blue, (column*size, row*size+size, size, size))

        for column in range(self._game.board.get_columns):
            for row in range(self._game.board.get_rows):
                if self._game.board.get_board[row][column] == 'X':
                    pygame.draw.circle(screen, red, (column*size+radius, row*size+size+radius), radius)
                elif self._game.board.get_board[row][column] == 'O':
                    pygame.draw.circle(screen, yellow, (column*size+radius, row*size+size+radius), radius)

        # After a change on the board, we update the board for correct display
        pygame.display.update()

    def start(self):
        # We initialize all imported Pygame modules
        pygame.init()

        # We set the size of a square of the board (number correspond to pixels).
        # Also we set the width and the height of the screen
        size = 100
        width = self._game.board.get_columns * size
        # We add one additional row for our piece movement
        height = (self._game.board.get_rows+1) * size
        radius = size // 2

        screen_size = (width, height)
        screen = pygame.display.set_mode(screen_size)
        self.draw_board(screen, screen_size)
        pygame.display.update()

        game_font = pygame.font.SysFont('monospace', 75)

        # We initialize pygame colors
        red = pygame.Color(255, 0, 0)
        white = pygame.Color(255, 255, 255)

        done = False
        human_turn = True

        while not done:
            # self.draw_board(screen, screen_size)
            # Being an event based library, every action taken by the player is considered an individual event.
            for event in pygame.event.get():
                # Enable the game to exit.
                if event.type == pygame.QUIT:
                    sys.exit()

                # This is for the case when you move the piece above the board
                if event.type == pygame.MOUSEMOTION:
                    # We draw an additional rectangle above the board for creating a place to move the piece
                    pygame.draw.rect(screen, white, (0, 0, width, size))
                    click_position = event.pos[0]
                    if human_turn == 1:
                        pygame.draw.circle(screen, red, (click_position, size // 2), radius)

                pygame.display.update()

                # We manage what happens in the case of a mouse-click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(screen, white, (0, 0, width, size))

                    if human_turn == 1:
                        click_position = event.pos[0]
                        column = int(math.floor(click_position // size))

                        if self._game.board.is_valid(column):
                            row = self._game.board.get_open_row(column)
                            self._game.human_move(row, column, 'X')

                            if self._game.board.is_winning_move('X'):
                                text = game_font.render('You win!', True, red)
                                screen.blit(text, (40, 10))
                                done = True

                            self.draw_board(screen, screen_size)
                            human_turn = not human_turn

            if human_turn is False and not done:
                self._game.computer_move('O')

                if self._game.board.is_winning_move('O'):
                    text = game_font.render('Computer wins!', True, red)
                    screen.blit(text, (40, 10))
                    done = True

                self.draw_board(screen, screen_size)

                human_turn = not human_turn

            if done is True:
                pygame.time.wait(2000)
