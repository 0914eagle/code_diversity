
import sys

def f1(w, h, u, d, l, r):
    # Initialize the grid with the given dimensions and probabilities
    grid = [[0] * w for _ in range(h)]
    grid[0] = [1] + [0] * (w - 1)
    for i in range(1, h):
        for j in range(w):
            if grid[i - 1][j] == 1:
                grid[i][j] = [u, d, l, r]
            else:
                grid[i][j] = [0, 0, 0, 0]
    
    # Calculate the probability of each target being hit
    probs = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'T':
                probs.append(calculate_probability(grid, i, j))
    
    return probs

def f2(w, h, u, d, l, r):
    # Initialize the grid with the given dimensions and probabilities
    grid = [[0] * w for _ in range(h)]
    grid[0] = [1] + [0] * (w - 1)
    for i in range(1, h):
        for j in range(w):
            if grid[i - 1][j] == 1:
                grid[i][j] = [u, d, l, r]
            else:
                grid[i][j] = [0, 0, 0, 0]
    
    # Calculate the probability of each target being hit
    probs = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'T':
                probs.append(calculate_probability(grid, i, j))
    
    # Display the probabilities
    for prob in probs:
        print(prob)

def calculate_probability(grid, i, j):
    # Calculate the probability of the target being hit
    prob = 0
    for k in range(4):
        prob += grid[i][j][k] * calculate_probability_helper(grid, i, j, k)
    return prob

def calculate_probability_helper(grid, i, j, k):
    # Base case: if the target is hit, return 1
    if grid[i][j] == 'T':
        return 1
    
    # Calculate the probability of the target being hit in the next step
    prob = 0
    for l in range(4):
        if grid[i][j][l] != 0:
            prob += grid[i][j][l] * calculate_probability_helper(grid, i + directions[k][0], j + directions[k][1], l)
    
    return prob

directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

if __name__ == '__main__':
    w, h = map(int, input().split())
    u, d, l, r = map(int, input().split())
    probs = f1(w, h, u, d, l, r)
    f2(w, h, u, d, l, r)

