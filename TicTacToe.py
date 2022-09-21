# Author: Karen Calpo
# Date: 2/29/2020
# Description: Program that simulates a tic-tac-toe game.


class TicTacToe:
    """Main class for tic-tac-toe game"""
    def __init__(self):
        """Initialize method that initializes private variable for board and state."""
        self._board = [['', '', ''], ['', '', ''], ['', '', '']]
        self._state = "UNFINISHED"

    def get_current_state(self):
        """Class method that gets current state of the game."""
        return self._state

    def make_move(self, row, column, move):
        """Class method that allows two players to make a move in the game."""
        if row < 0 or row > 2:
            return False
        elif column < 0 or column > 2:
            return False
        elif self._board[row][column] != '':
            return False
        elif self._state == "X_WON" or self._state == "O_WON" or self._state == "DRAW":
            return False
        else:
            if "" in self._board[0] or "" in self._board[1] or "" in self._board[2]:
                if self._board[row][column] == '':
                    self._board[row][column] = move.lower()
                    if "" not in self._board[0] and "" not in self._board[1] and "" not in self._board[2]:
                        self._state = "DRAW"

            if self._board[0][0] == "x" and self._board[0][1] == "x" and self._board[0][2] == "x":
                self._state = "X_WON"
            elif self._board[0][0] == "o" and self._board[0][1] == "o" and self._board[0][2] == "o":
                self._state = "O_WON"
            elif self._board[1][0] == "x" and self._board[1][1] == "x" and self._board[1][2] == "x":
                self._state = "X_WON"
            elif self._board[1][0] == "o" and self._board[1][1] == "o" and self._board[1][2] == "o":
                self._state = "O_WON"
            elif self._board[2][0] == "x" and self._board[2][1] == "x" and self._board[2][2] == "x":
                self._state = "X_WON"
            elif self._board[2][0] == "o" and self._board[2][1] == "o" and self._board[2][2] == "o":
                self._state = "O_WON"
            elif self._board[0][0] == "x" and self._board[1][0] == "x" and self._board[2][0] == "x":
                self._state = "X_WON"
            elif self._board[0][0] == "o" and self._board[1][0] == "o" and self._board[2][0] == "o":
                self._state = "O_WON"
            elif self._board[0][1] == "x" and self._board[1][1] == "x" and self._board[2][1] == "x":
                self._state = "X_WON"
            elif self._board[0][1] == "o" and self._board[1][1] == "o" and self._board[2][1] == "o":
                self._state = "O_WON"
            elif self._board[0][2] == "x" and self._board[1][2] == "x" and self._board[2][2] == "x":
                self._state = "X_WON"
            elif self._board[0][2] == "o" and self._board[1][2] == "o" and self._board[2][2] == "o":
                self._state = "O_WON"
            elif self._board[0][1] == "x" and self._board[1][1] == "x" and self._board[2][2] == "x":
                self._state = "X_WON"
            elif self._board[0][1] == "o" and self._board[1][1] == "o" and self._board[2][2] == "o":
                self._state = "O_WON"
            elif self._board[2][2] == "x" and self._board[1][1] == "x" and self._board[0][1] == "x":
                self._state = "X_WON"
            elif self._board[2][2] == "o" and self._board[1][1] == "o" and self._board[0][1] == "o":
                self._state = "O_WON"

        self.show_board()
        print(self._state)

        return True

    def show_board(self):
        """Class method that prints the current state of the board."""
        print(self._board)