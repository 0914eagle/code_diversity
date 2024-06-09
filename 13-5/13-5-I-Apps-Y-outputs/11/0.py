
def solve(N, dice_rolls):
    # Initialize a variable to keep track of the current streak
    current_streak = 0
    
    # Iterate through the dice rolls
    for i in range(N-2):
        # Check if the current roll is a doublet
        if dice_rolls[i] == dice_rolls[i+1] == dice_rolls[i+2]:
            # Increment the current streak
            current_streak += 1
        else:
            # Reset the current streak
            current_streak = 0
    
    # Check if the current streak is at least 3
    if current_streak >= 3:
        return "Yes"
    else:
        return "No"

