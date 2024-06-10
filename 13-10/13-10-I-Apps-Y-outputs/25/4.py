
import math

def approximate_tsp(n, p, s, v):
    # Use the Arora-Mitchell algorithm to approximate the optimal tour
    c = ...
    t_approximation = ...
    
    # Calculate the total time to distribute the keys
    t_total = t_approximation + s / v
    
    return t_total, c

def main():
    n, p, s, v = map(float, input().split())
    t, c = approximate_tsp(n, p, s, v)
    print("%.6f %.6f" % (t, c))

if __name__ == '__main__':
    main()

