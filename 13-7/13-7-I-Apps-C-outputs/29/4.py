
def get_shortest_cycle(graph):
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
                        if neighbor == node:
                            return len(visited)
    return -1

def solve():
    n = int(input())
    graph = {}
    for i in range(n):
        graph[i] = []
    for i in range(n):
        a = int(input())
        for j in range(i+1, n):
            b = int(input())
            if a & b != 0:
                graph[i].append(j)
                graph[j].append(i)
    return get_shortest_cycle(graph)

if __name__ == '__main__':
    print(solve())

