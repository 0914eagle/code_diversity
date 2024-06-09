
def count_sets_of_jokes(N, jokes, relationships):
    graph = {i: [] for i in range(1, N+1)}
    for A, B in relationships:
        graph[A].append(B)

    def dfs(node):
        if not graph[node]:
            return {jokes[node-1]}
        
        all_jokes = set()
        for child in graph[node]:
            child_jokes = dfs(child)
            all_jokes.update(child_jokes)
        
        if jokes[node-1] in all_jokes:
            all_jokes.add(jokes[node-1])
        
        return all_jokes

    total_sets = len(dfs(1))
    return total_sets

# Input processing
N = int(input())
jokes = list(map(int, input().split()))
relationships = [tuple(map(int, input().split())) for _ in range(N-1)]

result = count_sets_of_jokes(N, jokes, relationships)
print(result)
