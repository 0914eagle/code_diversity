
def shortest_article_length(n, proofs):
    dp = [0] * (1 << n)
    
    for i in range(n):
        for j in range(1, proofs[i][0] + 1):
            mask = 0
            for k in range(proofs[i][j] + 1):
                mask |= 1 << proofs[i][j + k]
            dp[mask] = max(dp[mask], proofs[i][j - 1])
    
    for mask in range(1, 1 << n):
        for submask in range(mask, 0, -1):
            submask = (submask - 1) & mask
            dp[mask] = max(dp[mask], dp[submask] + dp[mask ^ submask])
    
    return dp[(1 << n) - 1]

n = int(input())
proofs = []
for _ in range(n):
    p = int(input())
    proof = list(map(int, input().split()))
    proofs.append(proof)

print(shortest_article_length(n, proofs))
