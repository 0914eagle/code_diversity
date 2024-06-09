
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
        
        jokes_set.add(jokes[node-1])
        jokes_list = list(jokes_set)
        jokes_list.sort()
        
        if jokes_list == list(range(min(jokes_list), max(jokes_list)+1)):
            count += 1

    count = 0
    dfs(1)
    return count

# Input reading
N = int(input())
jokes = list(map(int, input().split()))
relationships = [tuple(map(int, input().split())) for _ in range(N-1)]

result = count_sets_of_jokes(N, jokes, relationships)
print(result)
