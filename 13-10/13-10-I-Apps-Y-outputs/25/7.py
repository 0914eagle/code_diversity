
import math

def get_optimal_parameter(n, p, s, v):
    # Function to find the optimal parameter c for the Arora-Mitchell algorithm
    # n: number of airports
    # p: number of billions of operations the computer can execute per second
    # s: length of the optimal tour of all European airports in meters
    # v: speed of the private jet in meters per second
    
    # Initialize c to a small value
    c = 0.001
    
    # Iterate until the optimal parameter c is found
    while True:
        # Calculate the time it takes to run the algorithm with parameter c
        t = get_algorithm_time(n, p, c)
        
        # Calculate the time it takes to complete the tour produced by the algorithm
        t_total = t + s / v
        
        # If the time it takes to complete the tour is less than the current minimum time, update the optimal parameter c and minimum time
        if t_total < min_t:
            min_t = t_total
            min_c = c
        
        # Increment c by a small value
        c += 0.001
        
        # If the current value of c is greater than the maximum value, break the loop
        if c > 50:
            break
    
    return min_c, min_t

def get_algorithm_time(n, p, c):
    # Function to calculate the time it takes to run the Arora-Mitchell algorithm with a given parameter c
    # n: number of airports
    # p: number of billions of operations the computer can execute per second
    # c: parameter for the Arora-Mitchell algorithm
    
    # Calculate the time it takes to run the algorithm with parameter c
    t = n * (math.log2(n) ** (c * math.sqrt(2))) / (p * 1e9)
    
    return t

def get_total_time(n, p, s, v, c):
    # Function to calculate the total time it takes to distribute the keys
    # n: number of airports
    # p: number of billions of operations the computer can execute per second
    # s: length of the optimal tour of all European airports in meters
    # v: speed of the private jet in meters per second
    # c: parameter for the Arora-Mitchell algorithm
    
    # Calculate the time it takes to run the algorithm with parameter c
    t = get_algorithm_time(n, p, c)
    
    # Calculate the time it takes to complete the tour produced by the algorithm
    t_total = t + s / v
    
    return t_total

def main():
    # Read input from stdin
    n, p, s, v = map(float, input().split())
    
    # Use the get_optimal_parameter function to find the optimal parameter c for the Arora-Mitchell algorithm
    c, t = get_optimal_parameter(n, p, s, v)
    
    # Print the output
    print(c, t)

if __name__ == '__main__':
    main()

