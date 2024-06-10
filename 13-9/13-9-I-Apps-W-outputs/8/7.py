
import sys
input = sys.stdin.read().split()

N, Q = map(int, input[0:2])
edges = [(int(input[i]), int(input[i+1])) for i in range(2, 2*N, 2)]
operations = [(int(input[i]), int(input[i+1])) for i in range(2*N, 2*N + Q, 2)]

def get_subtree(vertex, tree):
    subtree = [vertex]
    for edge in tree:
        if edge[0] == vertex:
            subtree += get_subtree(edge[1], tree)
    return subtree

def solve(edges, operations):
    tree = edges[:]
    counters = [0] * (N + 1)
    for operation in operations:
        subtree = get_subtree(operation[0], tree)
        for vertex in subtree:
            counters[vertex] += operation[1]
    return counters

if __name__ == '__main__':
    print(*solve(edges, operations))

