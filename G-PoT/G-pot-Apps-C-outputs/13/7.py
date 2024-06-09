
def count_sets_of_jokes(N, jokes, relationships):
    graph = {i: [] for i in range(1, N+1)}
    for a, b in relationships:
        graph[a].append(b)

    def dfs(node):
        nonlocal count
        if node == 1:
            jokes_set = set()
        else:
            jokes_set = set([jokes[node-1]])

        for child in graph[node]:
            child_jokes_set = dfs(child)
            jokes_set.update(child_jokes_set)

        if jokes_set == set(range(min(jokes_set), max(jokes_set)+1)):
            count += 1

        return jokes_set

    count = 0
    dfs(1)
    return count

# Read input
N = int(input())
jokes = list(map(int, input().split()))
relationships = [list(map(int, input().split())) for _ in range(N-1)]

# Calculate and print output
result = count_sets_of_jokes(N, jokes, relationships)
print(result)
