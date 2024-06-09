
import math

def f1(w, h, u, d, l, r):
    # Calculate the probability of the ball bouncing up, down, left, or right
    p_up = u / 100
    p_down = d / 100
    p_left = l / 100
    p_right = r / 100
    
    # Initialize the probability matrix with the probability of the ball landing on a target
    prob = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'T':
                prob[i][j] = 1
    
    # Calculate the probability of the ball landing on a target from each space
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '.':
                prob[i][j] = p_up * prob[i - 1][j] + p_down * prob[i + 1][j] + p_left * prob[i][j - 1] + p_right * prob[i][j + 1]
    
    # Calculate the total probability of the ball landing on a target
    total_prob = sum(map(sum, prob))
    
    # Calculate the probability of each target being hit
    target_prob = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'T':
                target_prob.append(prob[i][j] / total_prob)
    
    return target_prob

def f2(w, h, u, d, l, r):
    # Calculate the probability of the ball bouncing up, down, left, or right
    p_up = u / 100
    p_down = d / 100
    p_left = l / 100
    p_right = r / 100
    
    # Initialize the probability matrix with the probability of the ball landing on a target
    prob = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'T':
                prob[i][j] = 1
    
    # Calculate the probability of the ball landing on a target from each space
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '.':
                prob[i][j] = p_up * prob[i - 1][j] + p_down * prob[i + 1][j] + p_left * prob[i][j - 1] + p_right * prob[i][j + 1]
    
    # Calculate the total probability of the ball landing on a target
    total_prob = sum(map(sum, prob))
    
    # Calculate the probability of each target being hit
    target_prob = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'T':
                target_prob.append(prob[i][j] / total_prob)
    
    # Calculate the expected number of balls needed to hit each target
    expected_balls = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'T':
                expected_balls.append(1 / target_prob[i * w + j])
    
    return expected_balls

if __name__ == '__main__':
    w, h = map(int, input().split())
    u, d, l, r = map(int, input().split())
    grid = [input() for _ in range(h)]
    target_prob = f1(w, h, u, d, l, r)
    expected_balls = f2(w, h, u, d, l, r)
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'T':
                print(f"{target_prob[i * w + j]:.6f}")

