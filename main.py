"""
Main application entry point and interactive game loop.
"""

import json
from board import render_board
from game_logic import check_win


def load_config(config_path="config.json"):
    """Loads board and game configuration from external JSON file."""
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "symbols": {"player_x": "X", "player_o": "O"},
            "winning_combinations": [
                [0, 1, 2], [3, 4, 5], [6, 7, 8],
                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                [0, 4, 8], [2, 4, 6]
            ]
        }


def run_game():
    config = load_config()
    symbols = config["symbols"]
    winning_combinations = config["winning_combinations"]

    x_state = [0] * 9
    z_state = [0] * 9
    turn = 1  # 1 for X, 0 for O

    print("=================================")
    print("      Welcome to Tic Tac Toe     ")
    print("=================================")

    while True:
        render_board(x_state, z_state, symbols)

        if turn == 1:
            print("X's Turn")
            value = int(input("Please enter a position (0-8): "))
            x_state[value] = 1
        else:
            print("O's Turn")
            value = int(input("Please enter a position (0-8): "))
            z_state[value] = 1

        game_result = check_win(x_state, z_state, winning_combinations)
        if game_result != -1:
            render_board(x_state, z_state, symbols)
            print("Match Over!")
            break

        turn = 1 - turn


if __name__ == "__main__":
    run_game()
