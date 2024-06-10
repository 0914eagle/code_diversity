
import math

def find_optimal_c(n, p, s, v):
    # Find the optimal value of c for the Arora-Mitchell algorithm
    c = (math.log(n) / s) * (v / p)
    return c

def find_time(n, p, s, v, c):
    # Find the time it takes to run the algorithm and distribute the keys
    time = (n * (math.log(n) ** (c * math.sqrt(2))) / (p * 10**9)) + (s / v)
    return time

def main():
    n, p, s, v = map(float, input().split())
    c = find_optimal_c(n, p, s, v)
    time = find_time(n, p, s, v, c)
    print(time, c)

if __name__ == '__main__':
    main()

