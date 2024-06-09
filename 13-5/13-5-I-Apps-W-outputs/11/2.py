
def solve(a, b):
    # Initialize the count of ways for each outcome
    first_wins = 0
    draw = 0
    second_wins = 0
    
    # Iterate over all possible values of the dice
    for i in range(1, 7):
        # Calculate the absolute difference between the written numbers and the dice value
        abs_diff_a = abs(a - i)
        abs_diff_b = abs(b - i)
        
        # Check if the first player wins, draws, or the second player wins
        if abs_diff_a < abs_diff_b:
            first_wins += 1
        elif abs_diff_a == abs_diff_b:
            draw += 1
        else:
            second_wins += 1
    
    # Return the count of ways for each outcome
    return first_wins, draw, second_wins

