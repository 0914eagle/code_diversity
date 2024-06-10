
def remove_corridors(rooms, corridors):
    # Initialize a graph with the rooms as nodes and the corridors as edges
    graph = {i: set() for i in range(1, rooms + 1)}
    for u, v in corridors:
        graph[u].add(v)
        graph[v].add(u)

    # Find all cycles in the graph
    cycles = []
    for node in graph:
        for neighbor in graph[node]:
            if neighbor in graph[neighbor]:
                cycles.append([node, neighbor])

    # Remove half of the corridors that form cycles
    removed_corridors = set()
    for cycle in cycles:
        if len(cycle) % 2 == 0:
            removed_corridors.add(cycle[0])
            removed_corridors.add(cycle[1])

    return len(removed_corridors), removed_corridors

def main():
    rooms, corridors = map(int, input().split())
    corridors = [tuple(map(int, input().split())) for _ in range(corridors)]
    print(*remove_corridors(rooms, corridors))

if __name__ == '__main__':
    main()

