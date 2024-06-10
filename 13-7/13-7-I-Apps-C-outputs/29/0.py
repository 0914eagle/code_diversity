
def get_cycle_length(graph):
    visited = set()
    queue = []
    for node in graph:
        if node not in visited:
            queue.append(node)
            visited.add(node)
            while queue:
                node = queue.pop(0)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
                        return len(visited)
    return -1

def get_shortest_cycle_length(graph):
    visited = set()
    queue = []
    for node in graph:
        if node not in visited:
            queue.append(node)
            visited.add(node)
            while queue:
                node = queue.pop(0)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
                        return len(visited)
    return -1

def main():
    n = int(input())
    graph = {}
    for i in range(n):
        graph[i] = []
    for i in range(n):
        a = int(input())
        for j in range(n):
            if i != j and a & j:
                graph[i].append(j)
    print(get_shortest_cycle_length(graph))

if __name__ == '__main__':
    main()

