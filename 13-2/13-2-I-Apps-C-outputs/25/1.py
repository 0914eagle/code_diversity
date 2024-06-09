
import itertools

def f1(n, m, d):
    # Calculate the probability of removing all opponent's minions
    # when there are n minions and m opponent's minions
    # and the explosion deals d units of damage
    
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
    
    # Initialize a list to store the number of minions that will be removed
    removed_minions = []
    
    # Iterate over the combination of minion healths
    for i in range(len(combination)):
        # Calculate the number of minions that will be removed for this combination of minion healths
        num_removed = calculate_num_removed(combination, i, m, d)
        removed_minions.append(num_removed)
    
    # Return the probability of removing all opponent's minions for this combination of minion healths
    return sum(removed_minions) / len(combination)

def calculate_num_removed(combination, i, m, d):
    # Calculate the number of minions that will be removed for a given combination of minion healths and a given index
    
    # Initialize a list to store the number of minions that will be removed
    num_removed = 0
    
    # Iterate over the combination of minion healths
    for j in range(len(combination)):
        # Calculate the number of minions that will be removed for this combination of minion healths and this index
        if j != i:
            num_removed += 1
    
    # Return the number of minions that will be removed
    return num_removed

if __name__ == '__main__':
    n, m, d = map(int, input().split())
    print(f1(n, m, d))

