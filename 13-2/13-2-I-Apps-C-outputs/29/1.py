
def f1(K, T, rolls):
    # Initialize a dictionary to store the number of dice to pick up and their corresponding probabilities
    dice_to_pick = {}

    # Iterate over all possible numbers of dice to pick up
    for i in range(1, K + 1):
        # Calculate the probability of getting the target number with the current number of dice to pick up
        prob = calc_probability(rolls, i, T)

        # If the probability is non-zero, add it to the dictionary
        if prob != 0:
            dice_to_pick[i] = prob

    # Return the key (number of dice to pick up) with the highest value (probability)
    return max(dice_to_pick, key=dice_to_pick.get)

def f2(K, T, rolls):
    # Initialize a dictionary to store the number of dice to pick up and their corresponding probabilities
    dice_to_pick = {}

    # Iterate over all possible numbers of dice to pick up
    for i in range(1, K + 1):
        # Calculate the probability of getting the target number with the current number of dice to pick up
        prob = calc_probability(rolls, i, T)

        # If the probability is non-zero, add it to the dictionary
        if prob != 0:
            dice_to_pick[i] = prob

    # Return the key (number of dice to pick up) with the highest value (probability)
    return max(dice_to_pick, key=dice_to_pick.get)

def calc_probability(rolls, num_dice, target):
    # Calculate the probability of getting the target number with the current number of dice to pick up
    prob = 0
    for roll in rolls:
        if roll <= target:
            prob += (target - roll + 1) / 6 ** num_dice
    return prob

if __name__ == '__main__':
    K, T = map(int, input().split())
    rolls = list(map(int, input().split()))
    print(f1(K, T, rolls))
    print(f2(K, T, rolls))

