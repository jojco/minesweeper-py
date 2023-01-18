"""
This is simple minesweeper console game.
Enyoj and have a fun.
"""
from typing import Dict
import yaml
from src.game import Minesweeper


def parse_yaml(filepath: str) -> Dict:

    with open(filepath, 'r', encoding="utf-8") as file:
        data = yaml.safe_load(file)
    return data


if __name__ == "__main__":
    config = parse_yaml("config.yaml")
    print(config)

    game = Minesweeper(10, 10, 10)
    game.print_board()
    while game.reveal(int(input("Enter row: ")), int(input("Enter column: "))):
        game.print_board()
    game.print_board()
