
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
    
    # Return the probability of being in B-ville after T days
    return prob

def calculate_day_probability(N, i):
    # Initialize variables
    prob = 0
    
    # Loop through each place
    for j in range(1, N+1):
        # Calculate the probability of being in place j on day i
        prob += calculate_place_probability(N, i, j)
    
    # Return the probability of being in any place on day i
    return prob / N

def calculate_place_probability(N, i, j):
    # Initialize variables
    prob = 0
    
    # Loop through each connection leaving place j on day i
    for k in range(1, N+1):
        # Calculate the probability of being in place k on day i+1
        prob += calculate_connection_probability(N, i, j, k)
    
    # Return the probability of being in any place on day i+1
    return prob / N

def calculate_connection_probability(N, i, j, k):
    # Initialize variables
    prob = 0
    
    # Loop through each connection leaving place j on day i
    for l in range(1, N+1):
        # Calculate the probability of being in place l on day i+1
        prob += calculate_place_probability(N, i+1, l)
    
    # Return the probability of being in place k on day i+1
    return prob / N

if __name__ == '__main__':
    N = int(input())
    L = int(input())
    print(f1(N, L))

