
import itertools

def get_probability(n, m, d, your_minions, opponent_minions):
    # Calculate the total number of combinations
    total_combinations = len(list(itertools.product(range(1, 7), repeat=n)))
    
    # Initialize a counter for the number of combinations that result in all opponent's minions being removed
    removed_combinations = 0
    
    # Iterate over all possible combinations of healths for your minions
    for combination in itertools.product(range(1, 7), repeat=n):
        # Calculate the number of remaining opponent's minions after the explosion
        remaining_opponent_minions = m
        for i in range(n):
            if combination[i] - d <= 0:
                remaining_opponent_minions -= 1
        
        # If all opponent's minions were removed, increase the counter
        if remaining_opponent_minions == 0:
            removed_combinations += 1
    
    # Return the probability of all opponent's minions being removed
    return removed_combinations / total_combinations

def main():
    n, m, d = map(int, input().split())
    your_minions = list(map(int, input().split()))
    opponent_minions = list(map(int, input().split()))
    print(get_probability(n, m, d, your_minions, opponent_minions))

if __name__ == '__main__':
    main()

