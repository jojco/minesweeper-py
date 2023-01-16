"""
This is simple minesweeper console game.
Enyoj and have a fun.
"""
import yaml
from src.game import Minesweeper


if __name__ == "__main__":
    with open("config.yaml", "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
        print(data)

    game = Minesweeper(10, 10, 10)
    game.print_board()
    while game.reveal(int(input("Enter row: ")), int(input("Enter column: "))):
        game.print_board()
    game.print_board()
