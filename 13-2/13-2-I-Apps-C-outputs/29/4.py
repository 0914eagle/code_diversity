
def get_dice_to_pick(k, t, rolls):
    # Initialize a dictionary to store the number of dice to pick and their corresponding probabilities
    dice_to_pick = {}

    # Loop through each dice and calculate the probability of getting the target number
    for i in range(k):
        # Calculate the probability of getting the target number with the current dice
        prob = (rolls[i] == t) / 6

        # If the probability is non-zero, add it to the dictionary
        if prob > 0:
            dice_to_pick[i] = prob

    # Return the key (dice to pick) with the highest value (probability)
    return max(dice_to_pick, key=dice_to_pick.get)

def main():
    k, t = map(int, input().split())
    rolls = list(map(int, input().split()))
    print(get_dice_to_pick(k, t, rolls))

if __name__ == '__main__':
    main()

