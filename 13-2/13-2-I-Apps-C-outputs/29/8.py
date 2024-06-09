
def get_dice_to_roll(k, t, rolls):
    # Initialize a dictionary to store the number of dice to roll and their corresponding probabilities
    dice_probabilities = {}

    # Iterate over the rolls and calculate the probability of each dice
    for roll in rolls:
        if roll in dice_probabilities:
            dice_probabilities[roll] += 1
        else:
            dice_probabilities[roll] = 1

    # Initialize the maximum probability to 0
    max_probability = 0

    # Iterate over the dice probabilities and calculate the probability of getting the target number
    for dice, probability in dice_probabilities.items():
        probability /= len(rolls)
        if probability > max_probability:
            max_probability = probability

    # Return the number of dice to roll that have the maximum probability of getting the target number
    return max_probability

def main():
    k, t = map(int, input().split())
    rolls = list(map(int, input().split()))
    print(get_dice_to_roll(k, t, rolls))

if __name__ == '__main__':
    main()

