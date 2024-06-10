
def read_input():
    H, W = map(int, input().split())
    costs = []
    for i in range(10):
        costs.append(list(map(int, input().split())))
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    return H, W, costs, A

def solve(H, W, costs, A):
    # Initialize the dp table with the minimum cost to turn a single digit into 1
    dp = [[[10**3] * 10 for _ in range(10)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if A[i][j] != -1:
                dp[i][j][A[i][j]] = 0

    # Fill in the dp table using the recurrence relation
    for i in range(H):
        for j in range(W):
            if A[i][j] != -1:
                for k in range(10):
                    if k != A[i][j]:
                        dp[i][j][k] = min(dp[i][j][k], dp[i][j][A[i][j]] + costs[A[i][j]][k])

    # Find the minimum cost to turn all digits into 1
    min_cost = 10**3
    for i in range(H):
        for j in range(W):
            if A[i][j] != -1:
                min_cost = min(min_cost, dp[i][j][1])

    return min_cost

def main():
    H, W, costs, A = read_input()
    print(solve(H, W, costs, A))

if __name__ == '__main__':
    main()

