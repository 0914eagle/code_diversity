
import math

def count_ways(n, m, p):
    # Calculate the number of ways to place the minimum number of obstacles
    num_ways = 0
    for i in range(n):
        for j in range(m):
            # Check if the current cell is part of a 2x2 subgrid with at least one obstacle
            if i + 1 < n and j + 1 < m:
                if (i + 1, j) in obstacles or (i, j + 1) in obstacles or (i + 1, j + 1) in obstacles:
                    num_ways += 1
    
    return num_ways % p

def main():
    n, m, p = map(int, input().split())
    print(count_ways(n, m, p))

if __name__ == "__main__":
    main()

