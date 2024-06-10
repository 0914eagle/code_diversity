
import sys

def get_input():
    V, P = map(int, input().split())
    assert 3 <= P <= V <= 200000
    edges = []
    for _ in range(V - 1):
        u, v = map(int, input().split())
        assert 0 <= u, v <= V - 1
        edges.append((u, v))
    assert len(set(edges)) == V - 1
    initial_vertices = list(map(int, input().split()))
    assert len(initial_vertices) == P
    assert all(0 <= v <= V - 1 for v in initial_vertices)
    assert len(set(initial_vertices)) == P
    return V, P, edges, initial_vertices

def get_leaves(edges):
    leaves = set()
    for u, v in edges:
        if v not in leaves:
            leaves.add(v)
    return leaves

def get_vertices_to_remove(V, P, edges, initial_vertices):
    leaves = get_leaves(edges)
    vertices_to_remove = []
    for v in range(V):
        if v not in leaves and v not in initial_vertices:
            vertices_to_remove.append(v)
    return vertices_to_remove

def count_remaining_pigs(V, P, edges, initial_vertices, vertices_to_remove):
    remaining_pigs = P
    for v in vertices_to_remove:
        if v in initial_vertices:
            remaining_pigs -= 1
    return remaining_pigs

def main():
    V, P, edges, initial_vertices = get_input()
    vertices_to_remove = get_vertices_to_remove(V, P, edges, initial_vertices)
    print(count_remaining_pigs(V, P, edges, initial_vertices, vertices_to_remove))

if __name__ == '__main__':
    main()

