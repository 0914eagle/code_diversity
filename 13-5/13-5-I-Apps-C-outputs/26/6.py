
import math

def f1(w, h, u, d, l, r):
    # Calculate the probability of the ball bouncing up, down, left, or right
    p_up = u / 100
    p_down = d / 100
    p_left = l / 100
    p_right = r / 100
    
    # Initialize the probability of each target
    prob = [0] * h
    
    # Loop through each target
    for i in range(h):
        # Calculate the probability of the target being hit
        prob[i] = f2(w, h, i, p_up, p_down, p_left, p_right)
    
    # Return the probability of each target
    return prob

def f2(w, h, i, p_up, p_down, p_left, p_right):
    # Calculate the probability of the target being hit
    prob = 0
    
    # Loop through each space in the grid
    for j in range(w):
        # Calculate the probability of the ball bouncing up, down, left, or right
        p = p_up if i > 0 and j > 0 else 0
        p += p_down if i < h-1 and j > 0 else 0
        p += p_left if i > 0 and j > 0 else 0
        p += p_right if i > 0 and j < w-1 else 0
        
        # Add the probability of the ball bouncing to the target
        prob += p
    
    # Return the probability of the target being hit
    return prob

if __name__ == '__main__':
    w, h = map(int, input().split())
    u, d, l, r = map(int, input().split())
    prob = f1(w, h, u, d, l, r)
    for p in prob:
        print(f'{p:.6f}')

