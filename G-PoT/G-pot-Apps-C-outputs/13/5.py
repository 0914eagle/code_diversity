
def count_valid_joke_sets(N, jokes, relationships):
    graph = {}
    for i in range(1, N+1):
        graph[i] = set()
    for a, b in relationships:
        graph[b].add(a)

    def is_consecutive_set(jokes):
        return sorted(jokes) == list(range(min(jokes), max(jokes)+1))

    def dfs(node):
        valid_joke_sets = set()
        for child in graph[node]:
            child_jokes = jokes[child-1]
            if child_jokes and is_consecutive_set(child_jokes):
                valid_joke_sets.add(tuple(child_jokes))
            valid_joke_sets.update(dfs(child))
        return valid_joke_sets

    petar_jokes = jokes[0]
    valid_sets = set()
    if petar_jokes and is_consecutive_set(petar_jokes):
        valid_sets.add(tuple(petar_jokes))
    valid_sets.update(dfs(1))

    return len(valid_sets)

# Read input
N = int(input())
jokes = list(map(int, input().split()))
relationships = [list(map(int, input().split())) for _ in range(N-1)]

# Call the function and print the output
print(count_valid_joke_sets(N, jokes, relationships))
