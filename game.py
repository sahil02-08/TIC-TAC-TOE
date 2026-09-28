"""
Core game mechanics and win condition validation.
"""

def custom_sum(a, b, c):
    """Calculates the sum of three positions."""
    return a + b + c


def check_win(x_state, z_state, winning_combinations):
    """
    Evaluates whether player X or player O has won.
    Returns:
        1 if X wins
        0 if O wins
       -1 if no winner yet
    """
    for win in winning_combinations:
        if custom_sum(x_state[win[0]], x_state[win[1]], x_state[win[2]]) == 3:
            print("\nX Won the match!")
            return 1
        if custom_sum(z_state[win[0]], z_state[win[1]], z_state[win[2]]) == 3:
            print("\nO Won the match!")
            return 0
            
    return -1
