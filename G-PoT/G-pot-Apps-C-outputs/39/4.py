
def shortest_article_length(n, theorems):
    dp = [0] * (1 << n)
    
    for i in range(n):
        for j in range(1, theorems[i][0] + 1):
            mask = 0
            for k in range(theorems[i][j] + 1):
                mask |= 1 << theorems[i][j]
            for k in range(1 << n):
                dp[k | mask] = max(dp[k | mask], dp[k] + theorems[i][j])
    
    return dp[(1 << n) - 1]

n = int(input())
theorems = []
for _ in range(n):
    p = int(input())
    proof_lengths = list(map(int, input().split()))
    theorems.append(proof_lengths)

result = shortest_article_length(n, theorems)
print(result)
