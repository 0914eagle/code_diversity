
def read_input():
    p, r, l = map(int, input().split())
    logs = []
    for _ in range(l):
        e1, e2 = map(int, input().split())
        logs.append((e1, e2))
    return p, r, l, logs

def find_stable_path(p, r, l, logs):
    # Initialize a graph with the boulders and logs as nodes
    graph = {i: [] for i in range(-2, r)}
    for e1, e2 in logs:
        graph[e1].append(e2)
        graph[e2].append(e1)

    # Breadth-first search from the left bank to find the shortest path to the right bank
    queue = [(0, -2)]
    visited = set()
    while queue:
        cost, node = queue.pop(0)
        if node == -1:
            return cost
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((cost + 1, neighbor))
    return -1

def find_min_people(p, r, l, logs):
    # Initialize a graph with the boulders and logs as nodes
    graph = {i: [] for i in range(-2, r)}
    for e1, e2 in logs:
        graph[e1].append(e2)
        graph[e2].append(e1)

    # Breadth-first search from the left bank to find the shortest path to the right bank
    queue = [(0, -2)]
    visited = set()
    while queue:
        cost, node = queue.pop(0)
        if node == -1:
            return p
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((cost + 1, neighbor))
    return -1

def main():
    p, r, l, logs = read_input()
    print(find_stable_path(p, r, l, logs))

if __name__ == '__main__':
    main()

