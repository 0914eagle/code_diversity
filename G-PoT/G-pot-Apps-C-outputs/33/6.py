
def find_largest_subset(nodes):
    dp = [0] * len(nodes)
    for i in range(len(nodes) - 1, -1, -1):
        dp[i] = 1
        for j in range(i + 1, len(nodes)):
            if nodes[i][0] > nodes[j][0]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

n = int(input())
nodes = []
for _ in range(n):
    v, p = map(int, input().split())
    nodes.append((v, p))

print(find_largest_subset(nodes))
