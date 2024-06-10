
def probability_of_gon_winning(g, k, p):
    # Initialize variables
    gon_wins = 0
    killua_wins = 0
    draws = 0
    
    # Loop through all possible coin flips
    for i in range(10**100):
        # Flip a coin
        if random.random() < p:
            result = "H"
        else:
            result = "T"
        
        # Check if Gon or Killua has won
        if g in result and k in result:
            draws += 1
        elif g in result:
            gon_wins += 1
        elif k in result:
            killua_wins += 1
    
    # Return the probability of Gon winning
    return gon_wins / (gon_wins + killua_wins + draws)

def main():
    # Read input from stdin
    g = input()
    k = input()
    p = float(input())
    
    # Call the probability_of_gon_winning function
    probability = probability_of_gon_winning(g, k, p)
    
    # Print the output to stdout
    print(probability)

if __name__ == '__main__':
    main()

