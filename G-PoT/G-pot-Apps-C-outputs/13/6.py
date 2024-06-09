
def count_sets_of_jokes(N, jokes, relationships):
    graph = {i: [] for i in range(1, N+1)}
    for a, b in relationships:
        graph[a].append(b)

    def dfs(node):
        nonlocal count
        jokes_set = set()
        for child in graph[node]:
            jokes_set.add(jokes[child-1])
            dfs(child)
        if jokes[node-1] not in jokes_set:
            count += 1

    count = 0
    dfs(1)
    return count

# Read input
N = int(input())
jokes = list(map(int, input().split()))
relationships = [list(map(int, input().split())) for _ in range(N-1)]

# Calculate and print the result
result = count_sets_of_jokes(N, jokes, relationships)
print(result)
