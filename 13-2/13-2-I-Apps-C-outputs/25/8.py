
import itertools

def f1(n, m, d):
    # Calculate the probability of removing all opponent's minions
    # when there are n minions and m opponent's minions
    # and the explosion deals d damage
    
    # Initialize a list to store the probability of removing all opponent's minions
    probabilities = []
    
    # Iterate over all possible combinations of minion healths
    for combination in itertools.product(range(1, 7), repeat=n):
        # Calculate the probability of removing all opponent's minions for this combination of minion healths
        probability = calculate_probability(combination, m, d)
        probabilities.append(probability)
    
    # Return the sum of all probabilities
    return sum(probabilities)

def calculate_probability(combination, m, d):
    # Calculate the probability of removing all opponent's minions for a given combination of minion healths
    
    # Initialize a list to store the probability of removing each opponent's minion
    probabilities = []
    
    # Iterate over all possible combinations of opponent's minion healths
    for opponent_combination in itertools.product(range(1, 7), repeat=m):
        # Calculate the probability of removing all opponent's minions for this combination of opponent's minion healths
        probability = calculate_opponent_probability(combination, opponent_combination, d)
        probabilities.append(probability)
    
    # Return the sum of all probabilities
    return sum(probabilities)

def calculate_opponent_probability(combination, opponent_combination, d):
    # Calculate the probability of removing all opponent's minions for a given combination of minion healths and opponent's minion healths
    
    # Initialize a list to store the probability of removing each opponent's minion
    probabilities = []
    
    # Iterate over all possible combinations of damage dealt to each opponent's minion
    for damage in range(1, d+1):
        # Calculate the probability of removing each opponent's minion for this combination of damage
        probability = calculate_damage_probability(combination, opponent_combination, damage)
        probabilities.append(probability)
    
    # Return the sum of all probabilities
    return sum(probabilities)

def calculate_damage_probability(combination, opponent_combination, damage):
    # Calculate the probability of removing all opponent's minions for a given combination of minion healths, opponent's minion healths, and damage dealt
    
    # Initialize a list to store the probability of removing each opponent's minion
    probabilities = []
    
    # Iterate over all possible combinations of minion healths and opponent's minion healths after damage is dealt
    for new_combination, new_opponent_combination in itertools.product(range(1, 7), repeat=2):
        # Calculate the probability of removing each opponent's minion for this combination of minion healths and opponent's minion healths
        probability = calculate_probability(new_combination, new_opponent_combination, d-damage)
        probabilities.append(probability)
    
    # Return the sum of all probabilities
    return sum(probabilities)

if __name__ == '__main__':
    n, m, d = map(int, input().split())
    combination = tuple(map(int, input().split()))
    opponent_combination = tuple(map(int, input().split()))
    print(f1(n, m, d))

