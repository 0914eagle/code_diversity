
import itertools

def f1(n, m, d):
    # Calculate the probability of removing all opponent's minions
    # using the "Explosion" spell
    
    # Initialize a list to store the probability of removing each minion
    probabilities = [0] * (m + 1)
    
    # Iterate over all possible combinations of minions remaining
    for remaining in itertools.combinations(range(m), m):
        # Calculate the probability of removing all minions
        probability = 1
        for i in range(m):
            if i in remaining:
                probability *= (d - i) / (m - i)
            else:
                probability *= i / (m - i)
        # Add the probability to the list
        probabilities[len(remaining)] += probability
    
    # Return the sum of the probabilities
    return sum(probabilities)

def f2(n, m, d):
    # Calculate the probability of removing all opponent's minions
    # using the "Explosion" spell, assuming all your own minions die
    
    # Initialize a list to store the probability of removing each minion
    probabilities = [0] * (m + 1)
    
    # Iterate over all possible combinations of minions remaining
    for remaining in itertools.combinations(range(m), m):
        # Calculate the probability of removing all minions
        probability = 1
        for i in range(m):
            if i in remaining:
                probability *= (d - i) / (m - i)
            else:
                probability *= i / (m - i)
        # Add the probability to the list
        probabilities[len(remaining)] += probability
    
    # Return the sum of the probabilities
    return sum(probabilities)

if __name__ == '__main__':
    n, m, d = map(int, input().split())
    print(f1(n, m, d))
    print(f2(n, m, d))

