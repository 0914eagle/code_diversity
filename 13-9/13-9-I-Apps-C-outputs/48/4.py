
def get_initial_pig_positions(pig_positions):
    return {pig: position for position, pig in enumerate(pig_positions)}

def get_graph_adjacency_list(num_vertices, edges):
    graph = [[] for _ in range(num_vertices)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph

def get_initial_wolf_positions(num_vertices, num_pigs):
    return {wolf: vertex for wolf in range(num_vertices - num_pigs)}

def bfs(graph, source, visited):
    queue = [source]
    visited.add(source)
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

def get_num_escaped_pigs(graph, initial_pig_positions, initial_wolf_positions, num_vertices):
    escaped_pigs = 0
    visited = set()
    for pig in initial_pig_positions:
        if pig in initial_wolf_positions:
            continue
        bfs(graph, pig, visited)
        if len(visited) == num_vertices:
            escaped_pigs += 1
    return escaped_pigs

def get_min_num_wolves_to_remove(graph, initial_pig_positions, initial_wolf_positions, num_vertices):
    min_wolves_to_remove = 0
    while True:
        num_escaped_pigs = get_num_escaped_pigs(graph, initial_pig_positions, initial_wolf_positions, num_vertices)
        if num_escaped_pigs == len(initial_pig_positions):
            break
        min_wolves_to_remove += 1
        initial_wolf_positions.pop()
    return min_wolves_to_remove

def main():
    num_vertices, num_pigs = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(num_vertices - 1)]
    initial_pig_positions = tuple(map(int, input().split()))
    graph = get_graph_adjacency_list(num_vertices, edges)
    initial_wolf_positions = get_initial_wolf_positions(num_vertices, num_pigs)
    min_num_wolves_to_remove = get_min_num_wolves_to_remove(graph, initial_pig_positions, initial_wolf_positions, num_vertices)
    print(min_num_wolves_to_remove)

if __name__ == '__main__':
    main()

