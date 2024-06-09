
def get_dice_to_roll(k, t, rolls):
    # Initialize a dictionary to store the number of dice to roll and their corresponding probabilities
    dice_to_roll = {}

    # Loop through each die and calculate the probability of getting the target number
    for i in range(1, k+1):
        # Calculate the probability of getting the target number with i dice
        prob = get_probability(i, t, rolls)

        # If the probability is non-zero, add it to the dictionary
        if prob != 0:
            dice_to_roll[i] = prob

    # Return the key (number of dice to roll) with the highest value in the dictionary
    return max(dice_to_roll, key=dice_to_roll.get)

def get_probability(i, t, rolls):
    # Initialize a variable to store the probability
    prob = 0

    # Loop through each combination of i dice and calculate the probability of getting the target number
    for combination in itertools.combinations(rolls, i):
        # Calculate the sum of the dice rolled in the current combination
        sum_rolls = sum(combination)

        # If the sum is equal to the target number, increment the probability
        if sum_rolls == t:
            prob += 1 / math.factorial(i)

    # Return the probability
    return prob

if __name__ == '__main__':
    k, t = map(int, input().split())
    rolls = list(map(int, input().split()))
    print(get_dice_to_roll(k, t, rolls))

