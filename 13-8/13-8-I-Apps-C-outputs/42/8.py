
import sys
import math

def get_input():
    n, k = map(int, input().strip().split())
    courses = []
    for i in range(n):
        course, difficulty = input().strip().split()
        courses.append((course, int(difficulty)))
    return n, k, courses

def find_min_sum(n, k, courses):
    # Initialize the dp table with infinity
    dp = [[math.inf] * (k+1) for _ in range(n+1)]
    
    # Initialize the first row with 0
    for i in range(k+1):
        dp[0][i] = 0
    
    # Fill in the dp table
    for i in range(1, n+1):
        for j in range(1, k+1):
            if j >= courses[i-1][1]:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-courses[i-1][1]] + courses[i-1][1])
            else:
                dp[i][j] = dp[i-1][j]
    
    # Return the minimum sum
    return dp[n][k]

def main():
    n, k, courses = get_input()
    print(find_min_sum(n, k, courses))

if __name__ == '__main__':
    main()

