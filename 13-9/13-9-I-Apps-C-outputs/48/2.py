
def is_leaf(graph, vertex):
    return len(graph[vertex]) == 1

def can_move(graph, vertex, wolf_vertices):
    return vertex not in wolf_vertices and len(graph[vertex]) > 0

def bfs(graph, start, wolf_vertices):
    queue = [start]
    visited = set()
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            if is_leaf(graph, vertex):
                return True
            for neighbor in graph[vertex]:
                if can_move(graph, neighbor, wolf_vertices):
                    queue.append(neighbor)
    return False

def solve(graph, pigs):
    wolf_vertices = set(range(len(graph))) - set(pigs)
    for pig in pigs:
        if not bfs(graph, pig, wolf_vertices):
            return -1
    return len(wolf_vertices)

def main():
    v, p = map(int, input().split())
    graph = [[] for _ in range(v)]
    for _ in range(v - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    pigs = list(map(int, input().split()))
    print(solve(graph, pigs))

if __name__ == '__main__':
    main()

