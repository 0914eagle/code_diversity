
def count_joke_sets(N, jokes, relationships):
    graph = {i: [] for i in range(1, N+1)}
    for a, b in relationships:
        graph[a].append(b)

    def dfs(node):
        nonlocal count
        if node == 1:
            jokeset = set()
        else:
            jokeset = {jokes[node-1]}
        
        for child in graph[node]:
            child_jokeset = dfs(child)
            jokeset.update(child_jokeset)
        
        if jokeset == set(range(min(jokeset), max(jokeset)+1)):
            count += 1
        
        return jokeset

    count = 0
    dfs(1)
    return count

# Input
N = int(input())
jokes = list(map(int, input().split()))
relationships = [tuple(map(int, input().split())) for _ in range(N-1)]

# Output
print(count_joke_sets(N, jokes, relationships))
