
import math

def f1(w, h, u, d, l, r):
    # Calculate the probability of the ball bouncing up, down, left, or right
    p_up = u / 100
    p_down = d / 100
    p_left = l / 100
    p_right = r / 100
    
    # Initialize the probability of hitting each target
    prob = [0] * h
    
    # Loop through each target
    for i in range(h):
        # Calculate the probability of hitting the target
        prob[i] = calculate_probability(w, h, i, p_up, p_down, p_left, p_right)
    
    # Return the probability of hitting each target
    return prob

def f2(w, h, u, d, l, r):
    # Calculate the probability of the ball bouncing up, down, left, or right
    p_up = u / 100
    p_down = d / 100
    p_left = l / 100
    p_right = r / 100
    
    # Initialize the probability of hitting each target
    prob = [0] * h
    
    # Loop through each target
    for i in range(h):
        # Calculate the probability of hitting the target
        prob[i] = calculate_probability(w, h, i, p_up, p_down, p_left, p_right)
    
    # Return the probability of hitting each target
    return prob

def calculate_probability(w, h, i, p_up, p_down, p_left, p_right):
    # Calculate the probability of hitting the target
    prob = 0
    
    # Loop through each space in the grid
    for j in range(w):
        # Calculate the probability of hitting the target from this space
        prob += calculate_space_probability(w, h, i, j, p_up, p_down, p_left, p_right)
    
    # Return the probability of hitting the target
    return prob

def calculate_space_probability(w, h, i, j, p_up, p_down, p_left, p_right):
    # Calculate the probability of hitting the target from this space
    prob = 0
    
    # If the space is an obstacle, return 0
    if grid[i][j] == 'X':
        return 0
    
    # If the space is a target, return 1
    if grid[i][j] == 'T':
        return 1
    
    # If the space is not an obstacle or a target, calculate the probability of hitting the target
    prob = (p_up * calculate_probability(w, h, i - 1, j, p_up, p_down, p_left, p_right) +
            p_down * calculate_probability(w, h, i + 1, j, p_up, p_down, p_left, p_right) +
            p_left * calculate_probability(w, h, i, j - 1, p_up, p_down, p_left, p_right) +
            p_right * calculate_probability(w, h, i, j + 1, p_up, p_down, p_left, p_right))
    
    # Return the probability of hitting the target
    return prob

if __name__ == '__main__':
    w, h, u, d, l, r = map(int, input().split())
    grid = [input() for _ in range(h)]
    prob = f1(w, h, u, d, l, r)
    for i in range(h):
        print(f"{prob[i]:.6f}")

