
import math

def f1(N, L):
    # Initialize variables
    prob = 0
    T = 0
    
    # Loop through each possible value of T
    for t in range(L, L+10):
        # Calculate the probability of being in B-ville after T days
        prob = calculate_probability(N, t)
        
        # If the probability is greater than or equal to 95%, return T
        if prob >= 0.95:
            return t
    
    # If no value of T satisfies the condition, return -1
    return -1

def calculate_probability(N, T):
    # Initialize variables
    prob = 1
    
    # Loop through each day of the trip
    for i in range(1, T+1):
        # Calculate the probability of being in B-ville on day i
        prob *= calculate_day_probability(N, i)
    
    # Return the probability
    return prob

def calculate_day_probability(N, i):
    # Initialize variables
    prob = 0
    
    # Loop through each place
    for j in range(1, N+1):
        # Calculate the probability of being in place j on day i
        prob += calculate_place_probability(N, i, j)
    
    # Return the probability
    return prob

def calculate_place_probability(N, i, j):
    # Initialize variables
    prob = 0
    
    # If place j is not B-ville, calculate the probability of being in place j on day i
    if j != N:
        prob = (1 / (N-1)) * (1 / (N-j))
    
    # Return the probability
    return prob

if __name__ == '__main__':
    N, L = map(int, input().split())
    print(f1(N, L))

