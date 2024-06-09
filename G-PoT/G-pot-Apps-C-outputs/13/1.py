
def count_sets_of_jokes(N, jokes, relationships):
    graph = {i: [] for i in range(1, N+1)}
    for supervisor, employee in relationships:
        graph[supervisor].append(employee)

    def dfs(node):
        nonlocal count
        jokes_set = set()
        for employee in graph[node]:
            jokes_set.add(jokes[employee-1])
            dfs(employee)
        if sorted(jokes_set) == list(range(min(jokes_set), max(jokes_set)+1)):
            count += 1

    count = 0
    dfs(1)
    return count

# Input processing
N = int(input())
jokes = list(map(int, input().split()))
relationships = [tuple(map(int, input().split())) for _ in range(N-1)]

result = count_sets_of_jokes(N, jokes, relationships)
print(result)
