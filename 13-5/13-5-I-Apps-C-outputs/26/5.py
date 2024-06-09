
import math

def f1(w, h, u, d, l, r):
    # Calculate the probability of the ball bouncing up, down, left, or right from any open space
    p_up = u / 100
    p_down = d / 100
    p_left = l / 100
    p_right = r / 100
    
    # Calculate the probability of the ball hitting a target
    p_target = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'T':
                p_target += calculate_probability(i, j, p_up, p_down, p_left, p_right)
    
    return p_target

def f2(w, h, u, d, l, r):
    # Calculate the probability of the ball hitting a target given that it has already hit one target
    p_target_given_hit = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'T':
                p_target_given_hit += calculate_probability(i, j, p_up, p_down, p_left, p_right)
    
    return p_target_given_hit

def calculate_probability(i, j, p_up, p_down, p_left, p_right):
    # Calculate the probability of the ball hitting a target at a given position
    probability = 0
    if i > 0 and grid[i-1][j] != 'X':
        probability += p_up * calculate_probability(i-1, j, p_up, p_down, p_left, p_right)
    if i < h-1 and grid[i+1][j] != 'X':
        probability += p_down * calculate_probability(i+1, j, p_up, p_down, p_left, p_right)
    if j > 0 and grid[i][j-1] != 'X':
        probability += p_left * calculate_probability(i, j-1, p_up, p_down, p_left, p_right)
    if j < w-1 and grid[i][j+1] != 'X':
        probability += p_right * calculate_probability(i, j+1, p_up, p_down, p_left, p_right)
    if grid[i][j] == 'T':
        probability += 1
    
    return probability

if __name__ == '__main__':
    w, h = map(int, input().split())
    u, d, l, r = map(int, input().split())
    grid = [input() for i in range(h)]
    print(f1(w, h, u, d, l, r))
    print(f2(w, h, u, d, l, r))

