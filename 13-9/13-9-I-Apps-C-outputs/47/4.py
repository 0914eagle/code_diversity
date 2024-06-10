
def probability_of_winning(g, k, p):
    # Initialize the probability of Gon winning as 0
    probability_gon_wins = 0
    
    # Loop through each possible outcome of the coin flip
    for i in range(len(g) + 1):
        # Calculate the probability of Gon winning in this outcome
        probability_gon_wins_this_outcome = probability_of_winning_in_outcome(g, k, p, i)
        
        # Add the probability of Gon winning in this outcome to the total probability
        probability_gon_wins += probability_gon_wins_this_outcome
    
    # Return the total probability of Gon winning
    return probability_gon_wins

def probability_of_winning_in_outcome(g, k, p, i):
    # Initialize the probability of Gon winning in this outcome as 0
    probability_gon_wins_this_outcome = 0
    
    # Calculate the probability of Gon winning in this outcome
    probability_gon_wins_this_outcome = probability_of_winning_in_one_turn(g, k, p, i)
    
    # Return the probability of Gon winning in this outcome
    return probability_gon_wins_this_outcome

def probability_of_winning_in_one_turn(g, k, p, i):
    # Initialize the probability of Gon winning in one turn as 0
    probability_gon_wins_one_turn = 0
    
    # Calculate the probability of Gon winning in one turn
    probability_gon_wins_one_turn = (1 - p)**(len(g) - i) * p**i
    
    # Return the probability of Gon winning in one turn
    return probability_gon_wins_one_turn

def main():
    # Read the input
    g, k, p = input().split()
    
    # Calculate the probability of Gon winning
    probability_gon_wins = probability_of_winning(g, k, float(p))
    
    # Print the result
    print(probability_gon_wins)

if __name__ == '__main__':
    main()

