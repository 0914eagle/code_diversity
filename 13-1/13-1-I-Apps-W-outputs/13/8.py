
def f1(p, s, r):
    # Initialize the probability of Hasan winning as 0
    probability = 0
    
    # Loop through all possible scores that Hasan can score
    for i in range(r, s+1):
        # Calculate the probability of Hasan scoring i goals and winning the game
        probability += calculate_probability(p, s, r, i)
    
    # Return the probability of Hasan winning
    return probability

def calculate_probability(p, s, r, i):
    # Initialize the probability as 0
    probability = 0
    
    # Calculate the probability of Hasan scoring i goals and winning the game
    probability = (i * (s-i)) / (p * (p-1))
    
    # Return the probability
    return probability

def f2(p, s, r):
    # Calculate the probability of Hasan winning
    probability = f1(p, s, r)
    
    # Calculate the modular inverse of probability
    modular_inverse = pow(probability, -1, 998244353)
    
    # Return the modular inverse
    return modular_inverse

if __name__ == '__main__':
    p, s, r = map(int, input().split())
    print(f2(p, s, r))

