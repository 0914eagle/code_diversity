
def solve_article_length(n, theorems):
    dp = [0] * (1 << n)
    
    for i in range(n):
        for j in range(1, theorems[i][0] + 1):
            mask = 0
            for k in range(theorems[i][j] + 1):
                mask |= 1 << theorems[i][j + k]
            dp[mask] = max(dp[mask], theorems[i][j - 1])
    
    for mask in range(1, 1 << n):
        for submask in range(mask, 0, -1):
            submask = (submask - 1) & mask
            dp[mask] = max(dp[mask], dp[submask] + dp[mask ^ submask])
    
    return dp[(1 << n) - 1]

# Read input
n = int(input())
theorems = []
for _ in range(n):
    p = int(input())
    proof = list(map(int, input().split()))
    theorems.append(proof)

# Solve and output
result = solve_article_length(n, theorems)
print(result)
