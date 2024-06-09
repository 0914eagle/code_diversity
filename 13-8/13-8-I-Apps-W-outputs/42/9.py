
import sys
import math

def solve(r1, c1, r2, c2):
    # Calculate the number of paths for each cell in the grid
    # and store the results in a dictionary for faster access
    paths = {}
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            if i == 0 and j == 0:
                paths[i, j] = 1
            elif i == 0:
                paths[i, j] = paths[i, j-1]
            elif j == 0:
                paths[i, j] = paths[i-1, j]
            else:
                paths[i, j] = (paths[i-1, j] + paths[i, j-1]) % (10**9+7)
    
    # Calculate the sum of paths for all cells in the grid
    sum = 0
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            sum = (sum + paths[i, j]) % (10**9+7)
    
    return sum

if __name__ == '__main__':
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
    print(solve(r1, c1, r2, c2))

