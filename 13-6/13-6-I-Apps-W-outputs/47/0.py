
def solve(n, m):
    # Calculate the probability of Alex successfully performing the trick
    probability = 0
    
    # Iterate over each possible combination of cards
    for i in range(1, n+1):
        for j in range(1, m+1):
            # Calculate the probability of Alex taking i cards with value j from m decks
            probability += (i * j * (m-1)**(n-i)) / (n * m**n)
    
    return probability

