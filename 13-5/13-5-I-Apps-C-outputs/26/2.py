
import math

def f1(w, h, u, d, l, r):
    # Calculate the probability of the ball bouncing up, down, left, or right
    p_up = u / 100
    p_down = d / 100
    p_left = l / 100
    p_right = r / 100
    
    # Initialize the probability of each target
    probabilities = [0] * h
    
    # Loop through each target
    for i in range(h):
        # Calculate the probability of the target being hit
        probabilities[i] = calculate_probability(w, h, i, p_up, p_down, p_left, p_right)
    
    return probabilities

def f2(w, h, u, d, l, r):
    # Calculate the probability of the ball bouncing up, down, left, or right
    p_up = u / 100
    p_down = d / 100
    p_left = l / 100
    p_right = r / 100
    
    # Initialize the probability of each target
    probabilities = [0] * h
    
    # Loop through each target
    for i in range(h):
        # Calculate the probability of the target being hit
        probabilities[i] = calculate_probability(w, h, i, p_up, p_down, p_left, p_right)
    
    return probabilities

def calculate_probability(w, h, i, p_up, p_down, p_left, p_right):
    # Calculate the probability of the target being hit
    probability = 0
    
    # Loop through each space in the grid
    for j in range(w):
        # Calculate the probability of the ball hitting the target from this space
        probability += calculate_space_probability(w, h, i, j, p_up, p_down, p_left, p_right)
    
    return probability

def calculate_space_probability(w, h, i, j, p_up, p_down, p_left, p_right):
    # Calculate the probability of the ball hitting the target from this space
    probability = 0
    
    # Check if the space is an obstacle
    if grid[i][j] == 'X':
        return 0
    
    # Check if the space is a target
    if grid[i][j] == 'T':
        return 1
    
    # Calculate the probability of the ball bouncing up, down, left, or right from this space
    p_bounce = p_up if i > 0 and grid[i - 1][j] != 'X' else 0
    p_bounce += p_down if i < h - 1 and grid[i + 1][j] != 'X' else 0
    p_bounce += p_left if j > 0 and grid[i][j - 1] != 'X' else 0
    p_bounce += p_right if j < w - 1 and grid[i][j + 1] != 'X' else 0
    
    # Calculate the probability of the ball hitting the target from this space
    probability = p_bounce * calculate_space_probability(w, h, i + 1, j, p_up, p_down, p_left, p_right)
    
    return probability

if __name__ == '__main__':
    w, h = map(int, input().split())
    u, d, l, r = map(int, input().split())
    grid = [input() for _ in range(h)]
    
    probabilities = f1(w, h, u, d, l, r)
    
    for i in range(h):
        print(f'{probabilities[i]:.6f}')

