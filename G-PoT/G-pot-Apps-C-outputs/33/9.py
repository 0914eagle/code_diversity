
def max_heap_subset(nodes):
    dp = [0] * len(nodes)
    
    def dfs(node):
        if dp[node] != 0:
            return dp[node]
        
        max_subset = 1
        for child in nodes[node]:
            max_subset = max(max_subset, 1 + dfs(child))
        
        dp[node] = max_subset
        return max_subset
    
    return dfs(0)

n = int(input())
nodes = [[] for _ in range(n)]
for i in range(n):
    v, p = map(int, input().split())
    if p != 0:
        nodes[p-1].append(i)
        
print(max_heap_subset(nodes))
