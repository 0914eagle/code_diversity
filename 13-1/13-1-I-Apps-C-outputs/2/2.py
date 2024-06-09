
def get_max_score(rolls):
    # Initialize the score for each category
    scores = [0] * 13
    scores[0] = 5  # 1's
    scores[1] = 2  # 2's
    scores[2] = 3  # 3's
    scores[3] = 4  # 4's
    scores[4] = 5  # 5's
    scores[5] = 6  # 6's
    scores[6] = 25  # Full House
    scores[7] = 30  # Small Straight
    scores[8] = 40  # Long Straight
    scores[9] = 50  # Yahtzee
    scores[10] = 0  # Chance

    # Initialize the current category and roll index
    category = 0
    roll_index = 0

    # Loop through each roll
    for roll in rolls:
        # Check if the roll is in the current category
        if roll == category + 1:
            # Increment the score for the current category
            scores[category] += 1
        else:
            # Move to the next category
            category += 1
            # Reset the score for the new category
            scores[category] = 1

        # Increment the roll index
        roll_index += 1

        # Check if all 13 categories have been used
        if category == 12:
            # Break out of the loop
            break

    # Return the maximum score
    return max(scores)

