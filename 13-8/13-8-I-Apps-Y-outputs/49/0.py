
import math

def get_optimal_c(n, p, s, v):
    # Function to find the optimal value of c
    c = (n * (math.log(n)**(1.5)) / (p * 10**9))**(1/s)
    return c

def get_time_to_distribute_keys(n, p, s, v, c):
    # Function to find the time to distribute the keys
    time = s * (1 + 1/c) / v
    return time

def main():
    n, p, s, v = map(float, input().split())
    c = get_optimal_c(n, p, s, v)
    time = get_time_to_distribute_keys(n, p, s, v, c)
    print(time, c)

if __name__ == '__main__':
    main()

