
def solve(N, dice_rolls):
    # Initialize a variable to keep track of the current streak
    current_streak = 0
    
    # Iterate through the dice rolls
    for i in range(N-2):
        # Check if the current roll and the next two rolls are the same
        if dice_rolls[i] == dice_rolls[i+1] == dice_rolls[i+2]:
            # If they are, increment the current streak
            current_streak += 1
        else:
            # If they are not, reset the current streak
            current_streak = 0
    
    # Check if the current streak is at least 3
    if current_streak >= 3:
        return "Yes"
    else:
        return "No"

