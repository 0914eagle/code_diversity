
import math

def optimize(n, p, s, v):
    # Function to optimize
    def time_to_distribute_keys(c):
        return s * (1 + 1 / c) / v + n * math.log2(n) ** (c * math.sqrt(2)) / (p * 1e9)
    
    # Boundaries for binary search
    left = 0
    right = 100
    
    # Initialize best solution
    best_c = 0
    best_time = math.inf
    
    while left <= right:
        # Calculate midpoint
        mid = (left + right) // 2
        
        # Calculate time for current c
        time = time_to_distribute_keys(mid)
        
        # Check if time is better than current best
        if time < best_time:
            best_c = mid
            best_time = time
        
        # Update boundaries
        if time_to_distribute_keys(left) < time:
            right = mid - 1
        else:
            left = mid + 1
    
    return best_c, best_time

def main():
    n, p, s, v = map(float, input().split())
    c, time = optimize(n, p, s, v)
    print(time, c)

if __name__ == '__main__':
    main()

