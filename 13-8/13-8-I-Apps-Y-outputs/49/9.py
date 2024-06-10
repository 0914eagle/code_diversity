
import math

def get_c(n, p, s, v):
    # Calculate the time it takes to run the algorithm with the optimal parameter c
    time_algorithm = s * (1 + 1 / c) / v
    
    # Calculate the total time it takes to run the algorithm and distribute the keys
    time_total = time_algorithm + n * time_algorithm
    
    # Return the optimal parameter c and the total time
    return c, time_total

def main():
    n, p, s, v = map(float, input().split())
    c, time_total = get_c(n, p, s, v)
    print(f"{time_total:.6f} {c:.6f}")

if __name__ == '__main__':
    main()

