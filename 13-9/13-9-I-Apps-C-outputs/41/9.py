
import itertools

def compute_probability(n, m, d, my_minions, opp_minions):
    
    # Initialize the probability to 0
    probability = 0

    # Iterate over all possible combinations of damage distribution
    for damage_distribution in itertools.product(range(d + 1), repeat=m):
        # Calculate the number of minions that will be removed
        num_removed = sum(1 for i in range(m) if damage_distribution[i] > 0)

        # If all opponent's minions are removed, add the probability to the total
        if num_removed == m:
            probability += 1 / len(list(itertools.product(range(d + 1), repeat=m)))

    return probability

def main():
    # Read the input
    n, m, d = map(int, input().split())
    my_minions = list(map(int, input().split()))
    opp_minions = list(map(int, input().split()))

    # Call the compute_probability function
    probability = compute_probability(n, m, d, my_minions, opp_minions)

    # Print the output
    print(probability)

if __name__ == '__main__':
    main()

