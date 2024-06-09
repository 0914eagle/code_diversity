
def shortest_article_length(n, theorems):
    dp = [0] * (1 << n)
    for i in range(n):
        for j in range(len(theorems[i])):
            mask = 0
            for k in range(2, len(theorems[i][j])):
                mask |= 1 << theorems[i][j][k]
            for k in range((1 << n) - 1, -1, -1):
                dp[k | mask] = max(dp[k | mask], dp[k] + theorems[i][j][0])

    return dp[(1 << n) - 1]

# Input parsing
n = int(input())
theorems = []
for _ in range(n):
    p = int(input())
    theorem = []
    for _ in range(p):
        theorem.append(list(map(int, input().split())))
    theorems.append(theorem)

# Calculate and print the shortest possible length of David's article
print(shortest_article_length(n, theorems))
