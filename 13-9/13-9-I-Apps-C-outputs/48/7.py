
def is_leaf(graph, vertex):
    
    neighbors = graph[vertex]
    return len(neighbors) == 1

def get_pigs_on_vertex(pigs, vertex):
    
    return len([pig for pig in pigs if pig == vertex])

def get_wolves_to_remove(graph, pigs, wolf_vertices):
    
    num_pigs = len(pigs)
    num_vertices = len(graph)
    visited = [False] * num_vertices
    queue = []
    for pig in pigs:
        visited[pig] = True
        queue.append(pig)
    while queue:
        vertex = queue.pop(0)
        if is_leaf(graph, vertex):
            continue
        for neighbor in graph[vertex]:
            if not visited[neighbor] and get_pigs_on_vertex(pigs, neighbor) == 0:
                queue.append(neighbor)
                visited[neighbor] = True
    return num_vertices - sum(visited) - len(wolf_vertices)

def main():
    num_vertices, num_pigs = map(int, input().split())
    graph = [[] for _ in range(num_vertices)]
    for _ in range(num_vertices - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    pigs = list(map(int, input().split()))
    wolf_vertices = set()
    for i in range(num_vertices):
        if i not in pigs:
            wolf_vertices.add(i)
    print(get_wolves_to_remove(graph, pigs, wolf_vertices))

if __name__ == '__main__':
    main()

