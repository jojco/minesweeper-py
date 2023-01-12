"""
This is simple minesweeper console game.
Enyoj and have a fun.
"""

import random
from termcolor import colored


class Minesweeper:

    def __init__(self, rows, columns, mines):
        self.rows = rows
        self.columns = columns
        self.mines = mines
        self.board = [[0 for _ in range(columns)] for _ in range(rows)]
        self.hidden_board = [
            [True for _ in range(columns)] for _ in range(rows)]
        self.generate_board()

    def generate_board(self):
        mines_placed = 0
        while mines_placed < self.mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.columns - 1)
            if self.board[row][col] != -1:
                self.board[row][col] = -1
                mines_placed += 1
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= row + i < self.rows and 0 <= col + j < self.columns and self.board[row + i][col + j] != -1:
                            self.board[row + i][col + j] += 1

    def reveal(self, row, col):

        if self.board[row][col] == -1:
            print(colored("You hit a mine! Game over.",
                  "red", "on_red", ["bold", "underline"]))
            return False
        if not self.hidden_board[row][col]:
            print(colored("You have already revealed this cell.", "red"))
            return True
        self.hidden_board[row][col] = False
        if self.board[row][col] == 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= row + i < self.rows and 0 <= col + j < self.columns:
                        self.reveal(row + i, col + j)
        return True

    def print_board(self):
        # for column in range(self.columns):
        #     print(f"{column}", end=" ")
        for row in self.board:
            # print(f"{self.board.index(row)}", end=" ")
            for cell in row:
                if self.hidden_board[self.board.index(row)][row.index(cell)]:
                    print("*️", end=" ")
                else:
                    if cell == -1:
                        print("X", end=" ")
                    else:
                        print(cell, end=" ")
            print()


if __name__ == "__main__":
    game = Minesweeper(10, 10, 10)
    game.print_board()
    while game.reveal(int(input("Enter row: ")), int(input("Enter column: "))):
        game.print_board()
    game.print_board()
