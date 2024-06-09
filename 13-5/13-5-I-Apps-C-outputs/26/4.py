
import math

def f1(w, h, u, d, l, r):
    # Calculate the probability of the ball bouncing up, down, left, or right from any open space
    p_up = u / 100
    p_down = d / 100
    p_left = l / 100
    p_right = r / 100
    
    # Initialize the probability of each target being hit
    probabilities = [0] * h
    
    # Loop through each row of the grid
    for i in range(h):
        # Loop through each column of the grid
        for j in range(w):
            # If the current space is a target, update the probability of it being hit
            if grid[i][j] == 'T':
                probabilities[i] += p_up * (1 - p_up) * (1 - p_down) * (1 - p_left) * (1 - p_right)
    
    # Return the probability of each target being hit
    return probabilities

def f2(w, h, u, d, l, r):
    # Calculate the probability of the ball bouncing up, down, left, or right from any open space
    p_up = u / 100
    p_down = d / 100
    p_left = l / 100
    p_right = r / 100
    
    # Initialize the probability of each target being hit
    probabilities = [0] * h
    
    # Loop through each row of the grid
    for i in range(h):
        # Loop through each column of the grid
        for j in range(w):
            # If the current space is a target, update the probability of it being hit
            if grid[i][j] == 'T':
                probabilities[i] += p_up * (1 - p_up) * (1 - p_down) * (1 - p_left) * (1 - p_right)
    
    # Return the probability of each target being hit
    return probabilities

if __name__ == '__main__':
    w, h, u, d, l, r = map(int, input().split())
    grid = [input() for _ in range(h)]
    probabilities = f1(w, h, u, d, l, r)
    for i in range(h):
        print(f"{probabilities[i]:.6f}")

