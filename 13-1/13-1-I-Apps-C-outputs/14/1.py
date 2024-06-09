
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
    current_place = 1
    
    # Loop through each day of the trip
    for day in range(T):
        # Calculate the probability of moving to the next place
        prob *= calculate_move_probability(N, current_place)
        
        # Move to the next place
        current_place = move_to_next_place(N, current_place)
    
    # Return the probability of being in B-ville after T days
    return prob

def calculate_move_probability(N, current_place):
    # Initialize variables
    prob = 0
    
    # Loop through each possible move
    for move in range(1, N+1):
        # Calculate the probability of moving to the next place
        prob += calculate_move_probability_helper(N, current_place, move)
    
    # Return the probability of moving to the next place
    return prob / N

def calculate_move_probability_helper(N, current_place, move):
    # Initialize variables
    prob = 0
    
    # Calculate the probability of moving to the next place
    if current_place + move <= N:
        prob = 1 / (N - current_place)
    
    # Return the probability of moving to the next place
    return prob

def move_to_next_place(N, current_place):
    # Initialize variables
    move = 0
    
    # Loop through each possible move
    for move in range(1, N+1):
        # Calculate the probability of moving to the next place
        if current_place + move <= N:
            break
    
    # Return the next place
    return current_place + move

if __name__ == '__main__':
    N, L = map(int, input().split())
    print(f1(N, L))

