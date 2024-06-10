
import math

def compute_c(n, p, s, v):
    # Compute the time it takes for the algorithm to produce an approximation of the optimal tour
    time_algorithm = s / (v * (1 + 1 / c))
    
    # Compute the number of operations the computer can execute in that time
    num_operations = p * time_algorithm * math.log(n, 2) ** (c * math.sqrt(2))
    
    # Compute the value of c that gives the optimal approximation
    c = (math.log(n, 2) ** (1 / (c * math.sqrt(2))) * num_operations) ** (1 / (n * math.log(n, 2)))
    
    return c

def compute_time(n, p, s, v, c):
    # Compute the time it takes for the algorithm to produce an approximation of the optimal tour
    time_algorithm = s / (v * (1 + 1 / c))
    
    # Add the time it takes to fly around Europe and distribute the keys
    time_total = time_algorithm + n / v
    
    return time_total, c

def main():
    n, p, s, v = map(float, input().split())
    c = compute_c(n, p, s, v)
    time_total, c = compute_time(n, p, s, v, c)
    print(time_total, c)

if __name__ == '__main__':
    main()

