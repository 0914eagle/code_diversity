
def get_dice_to_pick(k, t, rolls):
    # Initialize a dictionary to store the number of dice to pick and their corresponding probabilities
    dice_to_pick = {}

    # Iterate over the rolls and calculate the probability of each dice to be rolled again
    for roll in rolls:
        # Calculate the probability of the current dice to be rolled again
        prob = (t - roll) / (6 * (k - 1))

        # If the probability is non-zero, add the dice to the dictionary with its probability
        if prob > 0:
            dice_to_pick[roll] = prob

    # Sort the dictionary by probability in descending order
    sorted_dice_to_pick = sorted(dice_to_pick.items(), key=lambda x: x[1], reverse=True)

    # Return the number of dice to pick with the highest probability
    return sorted_dice_to_pick[0][0]

def main():
    k, t = map(int, input().split())
    rolls = list(map(int, input().split()))
    print(get_dice_to_pick(k, t, rolls))

if __name__ == '__main__':
    main()

