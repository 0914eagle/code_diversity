
import sys

def solve(r1, c1, r2, c2):
    # Calculate the number of paths for each (i, j) pair
    paths = [[0] * (c2 + 1) for _ in range(r2 + 1)]
    for i in range(r2 + 1):
        for j in range(c2 + 1):
            if i == 0 and j == 0:
                paths[i][j] = 1
            elif i == 0:
                paths[i][j] = paths[i][j - 1]
            elif j == 0:
                paths[i][j] = paths[i - 1][j]
            else:
                paths[i][j] = (paths[i - 1][j] + paths[i][j - 1]) % (10**9 + 7)
    
    # Sum the paths for the given range
    result = 0
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            result = (result + paths[i][j]) % (10**9 + 7)
    
    return result

if __name__ == '__main__':
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
    print(solve(r1, c1, r2, c2))

