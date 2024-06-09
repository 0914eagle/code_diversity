
def count_sets_of_jokes(N, jokes, relationships):
    graph = {i: [] for i in range(1, N+1)}
    for A, B in relationships:
        graph[A].append(B)

    def dfs(node, jokes_seen):
        if node == 1:
            jokes_seen = set()
        jokes_seen.add(jokes[node-1])
        valid_sets = 0
        for child in graph[node]:
            valid_sets += dfs(child, jokes_seen.copy())
        if len(jokes_seen) == max(jokes_seen) - min(jokes_seen) + 1:
            return valid_sets + 1
        return valid_sets

    return dfs(1, set())

# Read input
N = int(input())
jokes = list(map(int, input().split()))
relationships = [list(map(int, input().split())) for _ in range(N-1)]

# Calculate and print output
result = count_sets_of_jokes(N, jokes, relationships)
print(result)
