
def game(g, k, p):
    # Initialize the probability of Gon winning as 0
    prob_gon_wins = 0
    
    # Loop through all possible strings of length 10^100 that Gon and Killua can form
    for i in range(10**100):
        # Check if the current string is a substring of Gon's string
        if g in str(i):
            # If it is, add the probability of Gon winning to the total probability
            prob_gon_wins += p**i * (1-p)**(10**100-i)
    
    # Return the total probability of Gon winning
    return prob_gon_wins

def main():
    # Read input from stdin
    g, k, p = input().split()
    
    # Call the game function and print the result
    print(game(g, k, float(p)))

if __name__ == '__main__':
    main()

