
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
    for i in range(T):
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
    for i in range(1, N+1):
        # If the move is possible, calculate the probability of moving to that place
        if is_move_possible(N, current_place, i):
            prob += 1 / N
    
    # Return the probability of moving to the next place
    return prob

def move_to_next_place(N, current_place):
    # Initialize variables
    next_place = 0
    
    # Loop through each possible move
    for i in range(1, N+1):
        # If the move is possible, move to that place
        if is_move_possible(N, current_place, i):
            next_place = i
            break
    
    # Return the next place
    return next_place

def is_move_possible(N, current_place, next_place):
    # Initialize variables
    possible = False
    
    # Check if the move is possible
    if next_place != current_place and next_place != 0:
        possible = True
    
    # Return whether the move is possible
    return possible

if __name__ == '__main__':
    N = int(input())
    L = int(input())
    print(f1(N, L))

