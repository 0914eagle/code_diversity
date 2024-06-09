
def shortest_article_length(n, theorems):
    dp = [0] * n
    for i in range(n):
        length = theorems[i][0]
        dependencies = theorems[i][1:]
        for j in dependencies:
            length = max(length, dp[j])
        dp[i] = length
    return max(dp)

# Read input
n = int(input())
theorems = []
for _ in range(n):
    p = int(input())
    proof_lengths = []
    for _ in range(p):
        proof = list(map(int, input().split()))
        proof_lengths.append(proof[0])
    theorems.append(proof_lengths)

# Calculate and print the shortest possible length of David's article
print(shortest_article_length(n, theorems))
