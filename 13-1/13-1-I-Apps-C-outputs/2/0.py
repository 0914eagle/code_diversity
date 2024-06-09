
def get_max_score(rolls):
    # Initialize the score for each category
    scores = [0] * 13
    scores[0] = 5  # 1's
    scores[1] = 2  # 2's
    scores[2] = 3  # 3's
    scores[3] = 4  # 4's
    scores[4] = 5  # 5's
    scores[5] = 6  # 6's
    scores[6] = 25 # Full House
    scores[7] = 30 # Small Straight
    scores[8] = 40 # Long Straight
    scores[9] = 50 # Yahtzee
    scores[10] = 0  # Chance

    # Initialize the number of dice for each category
    num_dice = [0] * 13

    # Iterate through the rolls and update the score and number of dice for each category
    for roll in rolls:
        for i in range(13):
            if roll == i + 1:
                scores[i] += 1
                num_dice[i] += 1

    # Check if a category is a Yahtzee
    for i in range(13):
        if num_dice[i] == 5 and scores[i] == 5:
            return scores[i]

    # Check if a category is a Full House
    for i in range(13):
        if num_dice[i] == 3 and scores[i] == 25:
            return scores[i]

    # Check if a category is a Small Straight
    for i in range(13):
        if num_dice[i] == 4 and scores[i] == 30:
            return scores[i]

    # Check if a category is a Long Straight
    for i in range(13):
        if num_dice[i] == 5 and scores[i] == 40:
            return scores[i]

    # Check if a category is a Chance
    for i in range(13):
        if num_dice[i] == 5 and scores[i] == 0:
            return scores[i]

    # If no category is a Yahtzee, Full House, Small Straight, Long Straight, or Chance, return the sum of all scores
    return sum(scores)

