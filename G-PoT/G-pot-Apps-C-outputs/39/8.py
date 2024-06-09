
def shortest_article_length(n, theorems):
    dp = [[0] * (1 << n) for _ in range(n)]
    
    for i in range(n):
        for j in range(theorems[i][0]):
            mask = 0
            for k in range(theorems[i][j+1][1]):
                mask |= (1 << theorems[i][j+1][2+k])
            for k in range(1 << n):
                dp[i][k | (1 << i)] = max(dp[i][k | (1 << i)], dp[i][k] + theorems[i][j+1][0])
                dp[i][k | mask] = max(dp[i][k | mask], dp[i][k] + theorems[i][j+1][0])
    
    result = 0
    for i in range(n):
        result = max(result, dp[i][(1 << n) - 1])
    
    return result

n = int(input())
theorems = []
for _ in range(n):
    p = int(input())
    proofs = []
    for _ in range(p):
        l, k, *dependencies = map(int, input().split())
        proofs.append((l, k, dependencies))
    theorems.append((p, proofs))

print(shortest_article_length(n, theorems))
