
def solve(a, b):
    # Initialize the count of ways for each outcome
    first_wins = 0
    draw = 0
    second_wins = 0
    
    # Iterate over all possible values of the dice
    for i in range(1, 7):
        # Check which player wins based on the difference between the written numbers and the dice value
        if abs(a - i) < abs(b - i):
            first_wins += 1
        elif abs(a - i) > abs(b - i):
            second_wins += 1
        else:
            draw += 1
    
    # Return the count of ways for each outcome
    return first_wins, draw, second_wins

