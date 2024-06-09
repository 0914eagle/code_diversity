
def f1(K, T):
    # Initialize a dictionary to store the number of dice to pick up and their corresponding probabilities
    dice_probabilities = {}
    
    # Loop through each possible number of dice to pick up
    for i in range(1, K+1):
        # Calculate the probability of getting the target number with the current number of dice
        probability = calc_probability(i, T, K)
        
        # Add the probability to the dictionary
        dice_probabilities[i] = probability
    
    # Find the key (number of dice to pick up) with the highest value in the dictionary
    max_key = max(dice_probabilities, key=dice_probabilities.get)
    
    return max_key

def f2(K, T, rolls):
    # Initialize a dictionary to store the number of dice to pick up and their corresponding probabilities
    dice_probabilities = {}
    
    # Loop through each possible number of dice to pick up
    for i in range(1, K+1):
        # Calculate the probability of getting the target number with the current number of dice
        probability = calc_probability(i, T, K, rolls)
        
        # Add the probability to the dictionary
        dice_probabilities[i] = probability
    
    # Find the key (number of dice to pick up) with the highest value in the dictionary
    max_key = max(dice_probabilities, key=dice_probabilities.get)
    
    return max_key

def calc_probability(num_dice, target, total_dice, rolls=None):
    # Calculate the probability of getting the target number with the current number of dice
    probability = 0
    
    # If rolls is not provided, calculate the probability of getting the target number on the first roll
    if rolls is None:
        # Loop through each possible roll of the dice
        for roll in range(1, 7):
            # Calculate the probability of getting the target number with the current roll
            probability += (roll == target) / 6**num_dice
    # If rolls is provided, calculate the probability of getting the target number on the second roll
    else:
        # Loop through each possible roll of the dice
        for roll in range(1, 7):
            # Calculate the probability of getting the target number with the current roll
            probability += (roll == target) / 6**(num_dice - len(rolls))
    
    return probability

if __name__ == '__main__':
    K, T = map(int, input().split())
    rolls = list(map(int, input().split()))
    print(f2(K, T, rolls))

