
def get_valid_ways(A, B):
    n = len(A)
    if n == 0:
        return 0
    
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        for j in range(i):
            if A[j] == B[i - 1]:
                dp[i] += dp[j]
    
    return dp[n]

def main():
    A, B = input().split()
    print(get_valid_ways(A, B))

if __name__ == '__main__':
    main()

