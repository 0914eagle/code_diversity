
def solve(a, b):
    # Initialize the count of ways for each scenario
    first_player_wins = 0
    draw = 0
    second_player_wins = 0
    
    # Iterate over all possible values of the dice
    for i in range(1, 7):
        # Calculate the absolute difference between the written numbers and the dice value
        abs_diff_a = abs(a - i)
        abs_diff_b = abs(b - i)
        
        # Check which player has the smaller absolute difference
        if abs_diff_a < abs_diff_b:
            first_player_wins += 1
        elif abs_diff_a > abs_diff_b:
            second_player_wins += 1
        else:
            draw += 1
    
    # Return the count of ways for each scenario
    return first_player_wins, draw, second_player_wins
