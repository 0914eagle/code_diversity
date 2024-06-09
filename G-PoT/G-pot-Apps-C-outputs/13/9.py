
def count_joke_sets(N, jokes, relationships):
    graph = {i: [] for i in range(1, N+1)}
    for a, b in relationships:
        graph[a].append(b)

    def dfs(node):
        nonlocal count
        jokes_set = set()
        for child in graph[node]:
            jokes_set.add(jokes[child-1])
            dfs(child)
        jokes_set.add(jokes[node-1])
        if sorted(jokes_set) == list(jokes_set):
            count += 1

    count = 0
    dfs(1)
    return count

# Input processing
N = int(input())
jokes = list(map(int, input().split()))
relationships = [tuple(map(int, input().split())) for _ in range(N-1)]

# Call the function and print the output
result = count_joke_sets(N, jokes, relationships)
print(result)
