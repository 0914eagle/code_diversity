
def shortest_article_length(n, theorems):
    dp = [0] * (1 << n)
    
    for i in range(1 << n):
        for j in range(n):
            if i & (1 << j) == 0:
                continue
            for proof in theorems[j]:
                dp[i] = max(dp[i], dp[i - (1 << j) - (1 << proof[1])] + proof[0])
    
    return dp[(1 << n) - 1]

n = int(input())
theorems = []
for _ in range(n):
    p = int(input())
    proofs = []
    for _ in range(p):
        l, k, *dependencies = map(int, input().split())
        proofs.append((l, k, dependencies))
    theorems.append(proofs)

print(shortest_article_length(n, theorems))
