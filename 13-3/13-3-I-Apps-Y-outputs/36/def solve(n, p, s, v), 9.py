
import math

def solve(n, p, s, v):
    # Calculate the time it takes for the algorithm to run
    time_algorithm = s * (math.log(n) ** (0.5 * (1 + 1 / c))) / (p * 10 ** 9)
    
    # Calculate the time it takes for Miroslava to complete the tour
    time_tour = s / v
    
    # Calculate the total time it takes for Miroslava to run the algorithm and distribute the keys
    time_total = time_algorithm + time_tour
    
    # Find the optimal value of c that minimizes the total time
    c = optimize_c(n, p, s, v, time_total)
    
    return time_total, c

def optimize_c(n, p, s, v, time_total):
    # Initialize the lower and upper bounds for binary search
    lower_bound = 0
    upper_bound = 100
    
    while upper_bound - lower_bound > 1e-6:
        # Calculate the time it takes for the algorithm to run with the current value of c
        time_algorithm = s * (math.log(n) ** (0.5 * (1 + 1 / c))) / (p * 10 ** 9)
        
        # Calculate the time it takes for Miroslava to complete the tour with the current value of c
        time_tour = s / v
        
        # Calculate the total time it takes for Miroslava to run the algorithm and distribute the keys with the current value of c
        time_total_current = time_algorithm + time_tour
        
        # Check if the total time is within the desired range
        if abs(time_total_current - time_total) <= 1e-6:
            return c
        
        # Update the bounds based on the comparison with the desired total time
        if time_total_current < time_total:
            lower_bound = c
        else:
            upper_bound = c
        
        # Calculate the new value of c based on the bounds
        c = (lower_bound + upper_bound) / 2
    
    return c

n, p, s, v = map(float, input().split())
time_total, c = solve(n, p, s, v)
print(time_total, c)

