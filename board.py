"""
Handles rendering the Tic Tac Toe grid to the console output.
"""

def render_board(x_state, z_state, symbols):
    """Prints the current 3x3 game board state."""
    x_sym = symbols.get("player_x", "X")
    o_sym = symbols.get("player_o", "O")

    board_positions = []
    for i in range(9):
        if x_state[i]:
            board_positions.append(x_sym)
        elif z_state[i]:
            board_positions.append(o_sym)
        else:
            board_positions.append(str(i))

    print(f"\n {board_positions[0]} | {board_positions[1]} | {board_positions[2]} ")
    print("---|---|---")
    print(f" {board_positions[3]} | {board_positions[4]} | {board_positions[5]} ")
    print("---|---|---")
    print(f" {board_positions[6]} | {board_positions[7]} | {board_positions[8]} \n")
