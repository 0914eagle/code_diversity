
import math

def f1(w, h, u, d, l, r):
    # Calculate the probability of the ball bouncing up, down, left, or right
    p_up = u / 100
    p_down = d / 100
    p_left = l / 100
    p_right = r / 100
    
    # Initialize the grid with the given dimensions
    grid = [[0] * w for _ in range(h)]
    
    # Set the target positions
    target_positions = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'T':
                target_positions.append((i, j))
    
    # Calculate the probability of each target being hit
    probabilities = []
    for i, j in target_positions:
        # Calculate the probability of the ball visiting each space on its way to the target
        prob = 1
        for k in range(1, math.ceil(math.sqrt(w * h))):
            prob *= (1 - p_up - p_down - p_left - p_right)
            prob += p_up * (i - k >= 0 and grid[i - k][j] != 'X')
            prob += p_down * (i + k < h and grid[i + k][j] != 'X')
            prob += p_left * (j - k >= 0 and grid[i][j - k] != 'X')
            prob += p_right * (j + k < w and grid[i][j + k] != 'X')
        
        # Add the probability of the ball hitting the target
        probabilities.append(prob * (grid[i][j] == 'T'))
    
    return probabilities

def f2(w, h, u, d, l, r):
    # Calculate the probability of the ball bouncing up, down, left, or right
    p_up = u / 100
    p_down = d / 100
    p_left = l / 100
    p_right = r / 100
    
    # Initialize the grid with the given dimensions
    grid = [[0] * w for _ in range(h)]
    
    # Set the target positions
    target_positions = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'T':
                target_positions.append((i, j))
    
    # Calculate the probability of each target being hit
    probabilities = []
    for i, j in target_positions:
        # Calculate the probability of the ball visiting each space on its way to the target
        prob = 1
        for k in range(1, math.ceil(math.sqrt(w * h))):
            prob *= (1 - p_up - p_down - p_left - p_right)
            prob += p_up * (i - k >= 0 and grid[i - k][j] != 'X')
            prob += p_down * (i + k < h and grid[i + k][j] != 'X')
            prob += p_left * (j - k >= 0 and grid[i][j - k] != 'X')
            prob += p_right * (j + k < w and grid[i][j + k] != 'X')
        
        # Add the probability of the ball hitting the target
        probabilities.append(prob * (grid[i][j] == 'T'))
    
    return probabilities

if __name__ == '__main__':
    w, h, u, d, l, r = map(int, input().split())
    grid = [input() for _ in range(h)]
    probabilities = f1(w, h, u, d, l, r)
    for i, prob in enumerate(probabilities):
        print(f"{i+1}: {prob:.6f}")

