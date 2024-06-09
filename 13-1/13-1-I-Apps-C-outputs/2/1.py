
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

    # Iterate through the rolls
    while roll_index < len(rolls):
        # Get the current roll
        roll = rolls[roll_index]

        # Check if the roll is valid for the current category
        if roll in [1, 2, 3, 4, 5, 6]:
            # Update the score for the current category
            scores[category] += roll

            # Increment the roll index
            roll_index += 1

            # Check if the category is a Yahtzee or Chance
            if category == 9 or category == 10:
                # Break out of the loop
                break
            else:
                # Increment the category
                category += 1
        else:
            # Break out of the loop
            break

    # Return the maximum score
    return max(scores)

