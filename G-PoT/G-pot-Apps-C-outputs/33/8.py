
from collections import defaultdict

def dfs(node, parent, values, dp, graph):
    dp[node] = values[node]
    for child in graph[node]:
        if child != parent:
            dp[node] = max(dp[node], dfs(child, node, values, dp, graph))
    return dp[node]

def solve():
    n = int(input())
    values = [0] * (n + 1)
    parents = [0] * (n + 1)
    graph = defaultdict(list)
    for i in range(1, n + 1):
        v, p = map(int, input().split())
        values[i] = v
        parents[i] = p
        graph[p].append(i)
    
    dp = [0] * (n + 1)
    dfs(1, 0, values, dp, graph)
    
    return dp[1]

print(solve())
