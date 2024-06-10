
import itertools

def explosion_probability(your_minions, opponent_minions, damage):
    # Calculate the total health of both players
    total_health = sum(your_minions) + sum(opponent_minions)
    
    # Initialize a list to store the probability of each possible outcome
    probabilities = [0] * (total_health + 1)
    
    # Set the initial probability of the first outcome (all opponent minions dead)
    probabilities[0] = 1
    
    # Iterate through each possible outcome
    for i in range(1, total_health + 1):
        # Calculate the probability of the current outcome
        probability = 0
        for j in range(1, damage + 1):
            # Calculate the probability of the current damage amount
            damage_probability = 1 / total_health
            
            # Calculate the probability of the current outcome given the current damage amount
            outcome_probability = 0
            for k in range(1, total_health + 1):
                if k - j >= 0:
                    outcome_probability += probabilities[k - j] / total_health
            
            # Add the probability of the current damage amount to the total probability
            probability += damage_probability * outcome_probability
        
        # Add the probability of the current outcome to the list
        probabilities[i] = probability
    
    # Return the probability of all opponent minions dead
    return probabilities[total_health]

def main():
    # Read the input
    n, m, d = map(int, input().split())
    your_minions = list(map(int, input().split()))
    opponent_minions = list(map(int, input().split()))
    
    # Calculate the probability
    probability = explosion_probability(your_minions, opponent_minions, d)
    
    # Print the output
    print(probability)

if __name__ == '__main__':
    main()

