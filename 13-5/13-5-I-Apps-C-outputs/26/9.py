
import math

def f1(w, h, u, d, l, r):
    # Calculate the probability of the ball bouncing up, down, left, or right
    p_up = u / 100
    p_down = d / 100
    p_left = l / 100
    p_right = r / 100
    
    # Initialize the grid with the given dimensions
    grid = [[0] * w for _ in range(h)]
    
    # Set the targets to 1 and the obstacles to -1
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'T':
                grid[i][j] = 1
            elif grid[i][j] == 'X':
                grid[i][j] = -1
    
    # Calculate the probability of reaching each target from the top row
    probabilities = [0] * h
    for i in range(h):
        probabilities[i] = calculate_probability(grid, i, 0, p_up, p_down, p_left, p_right)
    
    # Return the probabilities in order from top to bottom, breaking ties left to right
    return [probabilities[i] for i in range(h) if grid[i][0] == 1]

def calculate_probability(grid, i, j, p_up, p_down, p_left, p_right):
    # Base case: if the ball reaches a target, return the probability of reaching that target
    if grid[i][j] == 1:
        return 1
    
    # Calculate the probability of bouncing up, down, left, or right from the current space
    probabilities = [0] * 4
    if i > 0 and grid[i - 1][j] != -1:
        probabilities[0] = p_up
    if i < len(grid) - 1 and grid[i + 1][j] != -1:
        probabilities[1] = p_down
    if j > 0 and grid[i][j - 1] != -1:
        probabilities[2] = p_left
    if j < len(grid[0]) - 1 and grid[i][j + 1] != -1:
        probabilities[3] = p_right
    
    # Calculate the probability of reaching each space from the current space
    total_probability = 0
    for k in range(4):
        if probabilities[k] != 0:
            total_probability += probabilities[k] * calculate_probability(grid, i + d_i[k], j + d_j[k], p_up, p_down, p_left, p_right)
    
    # Return the total probability of reaching the current space
    return total_probability

d_i = [-1, 1, 0, 0]
d_j = [0, 0, -1, 1]

if __name__ == '__main__':
    w, h, u, d, l, r = map(int, input().split())
    print(*f1(w, h, u, d, l, r), sep='\n')

