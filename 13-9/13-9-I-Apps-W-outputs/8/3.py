
import sys

def read_data():
    N, Q = map(int, sys.stdin.readline().split())
    edges = []
    for i in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        edges.append((a, b))
    operations = []
    for i in range(Q):
        p, x = map(int, sys.stdin.readline().split())
        operations.append((p, x))
    return N, Q, edges, operations

def parent_child_dict(edges):
    parent_child = {}
    for edge in edges:
        parent, child = edge
        if parent not in parent_child:
            parent_child[parent] = [child]
        else:
            parent_child[parent].append(child)
    return parent_child

def bfs(start, parent_child):
    queue = [start]
    visited = set()
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            if node in parent_child:
                queue.extend(parent_child[node])
            yield node

def increment_counters(start, parent_child, operations):
    counter = [0] * (len(parent_child) + 1)
    for node in bfs(start, parent_child):
        for operation in operations:
            if node == operation[0]:
                counter[node] += operation[1]
    return counter

def main():
    N, Q, edges, operations = read_data()
    parent_child = parent_child_dict(edges)
    counter = increment_counters(1, parent_child, operations)
    print(*counter, sep=' ')

if __name__ == '__main__':
    main()

