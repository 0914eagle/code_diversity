
def solve(dice_rolls):
    # Initialize a variable to keep track of the previous two rolls
    prev_rolls = []
    
    # Iterate through the list of dice rolls
    for roll in dice_rolls:
        # Check if the current roll is the same as the previous two rolls
        if roll in prev_rolls:
            # If it is, return "Yes"
            return "Yes"
        # Add the current roll to the list of previous rolls
        prev_rolls.append(roll)
        # If the list of previous rolls is longer than two, remove the first element
        if len(prev_rolls) > 2:
            prev_rolls.pop(0)
    
    # If the loop completes and no doublets are found, return "No"
    return "No"

