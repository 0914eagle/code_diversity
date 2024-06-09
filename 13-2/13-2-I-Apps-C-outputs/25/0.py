
import itertools

def f1(n, m, d):
    # Calculate the probability of removing all opponent's minions
    # when there are n minions and m opponent's minions
    # and the explosion deals d units of damage
    
    # Initialize the probability to 0
    probability = 0
    
    # Iterate over all possible combinations of minions that can be removed
    for combination in itertools.combinations(range(m), n):
        # Calculate the probability of removing this combination of minions
        probability += calculate_probability(n, m, d, combination)
    
    # Return the total probability
    return probability

def calculate_probability(n, m, d, combination):
    # Calculate the probability of removing the given combination of minions
    # when the explosion deals d units of damage
    
    # Initialize the probability to 1
    probability = 1
    
    # Iterate over each minion in the combination
    for i in combination:
        # Calculate the probability of removing this minion
        probability *= (m-i)/m
        # Decrease the health of the minion by 1
        m -= 1
        # Decrease the damage dealt by 1
        d -= 1
    
    # Return the probability
    return probability

def f2(n, m, d):
    # Calculate the probability of removing all opponent's minions
    # when there are n minions and m opponent's minions
    # and the explosion deals d units of damage
    
    # Initialize the probability to 0
    probability = 0
    
    # Iterate over all possible combinations of minions that can be removed
    for combination in itertools.combinations(range(m), n):
        # Calculate the probability of removing this combination of minions
        probability += calculate_probability(n, m, d, combination)
    
    # Return the total probability
    return probability

def calculate_probability(n, m, d, combination):
    # Calculate the probability of removing the given combination of minions
    # when the explosion deals d units of damage
    
    # Initialize the probability to 1
    probability = 1
    
    # Iterate over each minion in the combination
    for i in combination:
        # Calculate the probability of removing this minion
        probability *= (m-i)/m
        # Decrease the health of the minion by 1
        m -= 1
        # Decrease the damage dealt by 1
        d -= 1
    
    # Return the probability
    return probability

if __name__ == '__main__':
    n, m, d = map(int, input().split())
    print(f1(n, m, d))

