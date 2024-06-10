
def is_leaf(graph, vertex):
    neighbors = graph[vertex]
    return len(neighbors) == 1

def bfs(graph, start, visited):
    queue = [start]
    visited[start] = True
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
    return visited

def find_distinct_roots(graph, pigs):
    roots = []
    for i in range(len(pigs)):
        root = pigs[i]
        for j in range(i+1, len(pigs)):
            if pigs[j] in graph[root]:
                root = -1
                break
        if root != -1:
            roots.append(root)
    return roots

def get_distinct_leaves(graph, roots):
    leaves = []
    for root in roots:
        visited = [False] * len(graph)
        bfs(graph, root, visited)
        for i in range(len(graph)):
            if visited[i] and is_leaf(graph, i):
                leaves.append(i)
    return leaves

def solve(graph, pigs):
    roots = find_distinct_roots(graph, pigs)
    leaves = get_distinct_leaves(graph, roots)
    return len(roots) - len(leaves)

def main():
    v, p = map(int, input().split())
    graph = [[] for i in range(v)]
    for i in range(v-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    pigs = list(map(int, input().split()))
    print(solve(graph, pigs))

if __name__ == '__main__':
    main()

