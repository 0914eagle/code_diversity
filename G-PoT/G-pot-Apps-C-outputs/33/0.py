
def max_heap_subset(nodes):
    dp = [0] * len(nodes)
    for i in range(len(nodes) - 1, -1, -1):
        dp[i] = 1
        for child in nodes[i]:
            dp[i] += dp[child]
    return max(dp)

n = int(input())
nodes = [[] for _ in range(n)]
for i in range(n):
    v, p = map(int, input().split())
    if p != 0:
        nodes[p - 1].append(i)
print(max_heap_subset(nodes))
