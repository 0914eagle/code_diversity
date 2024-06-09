
def count_sets_of_jokes(N, jokes, relationships):
    graph = {}
    for i in range(1, N+1):
        graph[i] = set()
    
    for A, B in relationships:
        graph[B].add(A)
    
    def dfs(node):
        nonlocal count
        if node == 1:
            count += 1
        for neighbor in graph[node]:
            if jokes[neighbor-1] == jokes[node-1] or jokes[neighbor-1] - jokes[node-1] not in [-1, 1]:
                continue
            dfs(neighbor)
    
    count = 0
    dfs(1)
    
    return count

# Read input
N = int(input())
jokes = list(map(int, input().split()))
relationships = [list(map(int, input().split())) for _ in range(N-1)]

# Call the function and print the output
print(count_sets_of_jokes(N, jokes, relationships))
