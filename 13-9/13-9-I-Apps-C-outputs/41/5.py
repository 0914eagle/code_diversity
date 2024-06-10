
import itertools

def number_of_ways_to_kill_opponent(n_opponent, n_self, d):
    
    # Base case: if there are no opponent's minions, there is only one way to kill them (do nothing)
    if n_opponent == 0:
        return 1
    
    # Initialize the number of ways to kill the opponent's minions to 0
    num_ways = 0
    
    # Iterate over all possible ways to distribute the damage
    for damage_distribution in itertools.combinations(range(d), n_opponent):
        # Initialize the number of remaining opponent's minions to n_opponent
        remaining_opponent = n_opponent
        
        # Iterate over the damage distribution
        for damage in damage_distribution:
            # If the damage is not 0, subtract 1 from the number of remaining opponent's minions
            if damage != 0:
                remaining_opponent -= 1
        
        # If the number of remaining opponent's minions is 0, add 1 to the number of ways to kill the opponent's minions
        if remaining_opponent == 0:
            num_ways += 1
    
    # Return the number of ways to kill the opponent's minions
    return num_ways

def probability_of_killing_opponent(n_opponent, n_self, d):
    
    # Calculate the number of ways to kill the opponent's minions
    num_ways = number_of_ways_to_kill_opponent(n_opponent, n_self, d)
    
    # Calculate the probability that the Explosion spell will kill all the opponent's minions
    probability = num_ways / (2 ** n_opponent)
    
    # Return the probability
    return probability

def main():
    # Read the input
    n_opponent, n_self, d = map(int, input().split())
    opponent_health = list(map(int, input().split()))
    self_health = list(map(int, input().split()))
    
    # Calculate the probability that the Explosion spell will kill all the opponent's minions
    probability = probability_of_killing_opponent(n_opponent, n_self, d)
    
    # Print the probability
    print(probability)

if __name__ == '__main__':
    main()

