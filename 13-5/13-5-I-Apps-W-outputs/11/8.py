
def solve(a, b):
    # Initialize the count of ways for each scenario
    first_player_wins = 0
    draw = 0
    second_player_wins = 0
    
    # Iterate over all possible values of the dice
    for i in range(1, 7):
        # Check which player wins based on the difference between the written numbers and the dice value
        if abs(a - i) < abs(b - i):
            first_player_wins += 1
        elif abs(a - i) == abs(b - i):
            draw += 1
        else:
            second_player_wins += 1
    
    # Return the count of ways for each scenario
    return first_player_wins, draw, second_player_wins

