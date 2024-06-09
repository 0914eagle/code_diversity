
def solve(N, dice_rolls):
    # Initialize a variable to keep track of the current doublet
    current_doublet = False

    # Iterate through the dice rolls
    for i in range(N - 2):
        # Check if the current roll and the next two rolls form a doublet
        if dice_rolls[i] == dice_rolls[i + 1] == dice_rolls[i + 2]:
            # If they do, set the current doublet to True
            current_doublet = True
            break

    # Check if there was at least one doublet in a row
    if current_doublet:
        return "Yes"
    else:
        return "No"

