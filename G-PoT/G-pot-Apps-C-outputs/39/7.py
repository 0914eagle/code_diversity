
def shortest_article_length(n, theorems):
    dp = [0] * (1 << n)
    
    for i in range(1, 1 << n):
        dp[i] = float('inf')
        for j in range(n):
            if i & (1 << j):
                prev_proof = 0
                for k in range(theorems[j][1]):
                    prev_proof = max(prev_proof, theorems[j][2][k])
                dp[i] = min(dp[i], dp[i - (1 << j)] + theorems[j][0] - prev_proof)
    
    return dp[(1 << n) - 1]

# Input processing
n = int(input())
theorems = []
for _ in range(n):
    p = int(input())
    proofs = []
    for _ in range(p):
        l, k, *dependencies = map(int, input().split())
        proofs.append((l, k, dependencies))
    theorems.append((p, proofs))

# Call the function and print the result
print(shortest_article_length(n, theorems))
