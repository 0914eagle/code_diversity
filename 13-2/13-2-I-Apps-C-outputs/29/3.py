
def get_dice_to_roll(dice, target, rolls):
    # Initialize a dictionary to store the number of dice to roll and their corresponding probabilities
    dice_to_roll = {}

    # Iterate over the rolls and calculate the probability of each dice to roll
    for roll in rolls:
        # Check if the roll is already in the dictionary
        if roll in dice_to_roll:
            # If it is, increment the count of dice to roll with this value
            dice_to_roll[roll] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            dice_to_roll[roll] = 1

    # Iterate over the dictionary and calculate the probability of each dice to roll
    for roll, count in dice_to_roll.items():
        # Calculate the probability of rolling the target number with this dice
        probability = count / dice

        # Check if the probability is greater than or equal to the current maximum probability
        if probability >= max(dice_to_roll.values()):
            # If it is, return the number of dice to roll
            return count

    # If no dice to roll has a probability greater than or equal to the current maximum, return 0
    return 0

def main():
    # Read the input
    dice, target = map(int, input().split())
    rolls = list(map(int, input().split()))

    # Call the function to get the number of dice to roll
    dice_to_roll = get_dice_to_roll(dice, target, rolls)

    # Print the output
    print(dice_to_roll)

if __name__ == '__main__':
    main()

