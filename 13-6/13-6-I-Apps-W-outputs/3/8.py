
def count_arrays(n, m):
    # Initialize a 2D array to store the number of arrays for each pair of elements
    dp = [[0] * (m + 1) for _ in range(m + 1)]
    
    # Base case: only one array with one element
    for i in range(1, m + 1):
        dp[i][i] = 1
    
    # Populate the 2D array using the recurrence relation
    for i in range(2, n + 1):
        for j in range(1, m + 1):
            for k in range(1, m + 1):
                if j != k:
                    dp[j][k] += dp[j - 1][k - 1]
    
    # Return the number of arrays that meet all the conditions
    return sum(dp[m]) % 998244353

def main():
    n, m = map(int, input().split())
    print(count_arrays(n, m))

if __name__ == '__main__':
    main()

