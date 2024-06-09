
import math

def f1(N, L):
    # Initialize variables
    prob = 0
    T = 0
    
    # Loop through each possible value of T
    for t in range(L, L+10):
        # Calculate the probability of being in B-ville after t days
        prob = calculate_probability(N, t)
        
        # If the probability is greater than or equal to 95%, return T
        if prob >= 0.95:
            return T
        
        # Otherwise, increment T and continue looping
        T += 1
    
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
    
    # If place j is the last place, return the probability of being in B-ville
    if j == N:
        return 1
    
    # Loop through each connection from place j
    for k in range(1, N+1):
        # If place k is connected to place j, calculate the probability of being in place k on day i
        if a[j][k] != 0:
            prob += calculate_place_probability(N, i-1, k) * a[j][k] / sum(a[j])
    
    # Return the probability
    return prob

# Main function
if __name__ == '__main__':
    # Read input from stdin
    N, L = map(int, input().split())
    a = []
    for i in range(N):
        a.append(list(map(int, input().split())))
    
    # Call function f1 and print the result
    print(f1(N, L))

