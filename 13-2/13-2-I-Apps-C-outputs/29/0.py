
def get_dice_to_roll(k, t, rolls):
    # Initialize a dictionary to store the number of dice to roll and their corresponding probabilities
    dice_probabilities = {}

    # Loop through each die and calculate the probability of getting the target number
    for i in range(1, k+1):
        # Calculate the probability of getting the target number with i dice
        probability = (rolls.count(i) + 1) / (len(rolls) + k)

        # Add the probability and the number of dice to the dictionary
        dice_probabilities[i] = probability

    # Find the key (number of dice) with the highest probability
    max_probability = max(dice_probabilities.values())
    dice_to_roll = [key for key, value in dice_probabilities.items() if value == max_probability]

    # If there is a tie, return the smallest number of dice to roll
    if len(dice_to_roll) > 1:
        return min(dice_to_roll)
    else:
        return dice_to_roll[0]

def main():
    k, t = map(int, input().split())
    rolls = list(map(int, input().split()))
    print(get_dice_to_roll(k, t, rolls))

if __name__ == '__main__':
    main()

