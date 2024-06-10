
def get_input():
    n, m = map(int, input().split())
    corridors = [tuple(map(int, input().split())) for _ in range(m)]
    return n, m, corridors

def remove_corridors(n, m, corridors):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for u, v in corridors:
        graph[u-1].append(v-1)
    
    # Remove at most half of the corridors
    removed_corridors = set()
    for i in range(m//2):
        # Find a cycle in the graph
        cycle = find_cycle(graph)
        if not cycle:
            break
        # Remove the edge with the smallest index in the cycle
        removed_corridors.add(min(cycle))
        # Update the graph by removing the edge
        graph[cycle[0]-1].remove(cycle[1]-1)
        graph[cycle[1]-1].remove(cycle[0]-1)
    
    return len(removed_corridors), removed_corridors

def find_cycle(graph):
    # Initialize a visited array and a queue
    visited = [False] * len(graph)
    queue = [0]
    
    while queue:
        node = queue.pop(0)
        if visited[node]:
            continue
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
            else:
                return [node, neighbor]
    return None

def main():
    n, m, corridors = get_input()
    removed_corridors = remove_corridors(n, m, corridors)
    print(len(removed_corridors))
    for corridor in removed_corridors:
        print(corridor+1)

if __name__ == '__main__':
    main()

