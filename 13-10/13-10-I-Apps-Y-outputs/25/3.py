
import math

def solve(n, p, s, v):
    # Approximate the running time of the algorithm
    t_alg = n * (math.log(n) ** (1.5 * math.sqrt(2))) / (p * 1e9)
    
    # Choose the parameter c that minimizes the total time
    c = (s * (1 + 1 / c) / v - t_alg) / (s / v)
    
    # Return the total time and the value of c
    return t_alg + s / v, c

def main():
    n, p, s, v = map(float, input().split())
    t, c = solve(n, p, s, v)
    print(t, c)

if __name__ == '__main__':
    main()

