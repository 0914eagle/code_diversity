
import itertools
import math

def explosion(n, m, d):
    # Initialize a list to store the probability of each combination of health
    probabilities = [0] * (m + 1)
    probabilities[0] = 1

    # Iterate over each possible combination of health for the opponent's minions
    for health in itertools.product(range(1, 7), repeat=m):
        # Calculate the probability of the explosion removing all minions
        probability = 1
        for i in range(m):
            probability *= (d - i) / (6 - health[i] + 1)

        # Add the probability to the list of probabilities
        probabilities[sum(health)] += probability

    # Return the sum of the probabilities
    return sum(probabilities)

def main():
    n, m, d = map(int, input().split())
    print(explosion(n, m, d))

if __name__ == '__main__':
    main()

