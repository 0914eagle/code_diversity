
import math

def get_c(n, p, s, v):
    # Calculate the time it takes to run the algorithm with the optimal parameter c
    time_algorithm = s * (1 + 1 / c) / v
    
    # Calculate the time it takes to distribute the keys
    time_distribution = n * (math.log(n) ** (c * math.sqrt(2))) / (p * 10 ** 9)
    
    # Calculate the total time it takes
    total_time = time_algorithm + time_distribution
    
    # Return the optimal parameter c and the total time
    return c, total_time

def main():
    n, p, s, v = map(float, input().split())
    c, total_time = get_c(n, p, s, v)
    print(total_time, c)

if __name__ == '__main__':
    main()

