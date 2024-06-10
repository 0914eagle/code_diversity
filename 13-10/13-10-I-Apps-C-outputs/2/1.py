
import sys

def find_parent(element):
    if element != parent[element]:
        parent[element] = find_parent(parent[element])
    return parent[element]

def union_sets(element1, element2):
    parent1 = find_parent(element1)
    parent2 = find_parent(element2)
    if parent1 != parent2:
        parent[parent1] = parent2

def are_connected(element1, element2):
    return find_parent(element1) == find_parent(element2)

def process_queries(N, Q):
    parent = {}
    for i in range(N):
        parent[i] = i
    for _ in range(Q):
        query = sys.stdin.readline().strip()
        if query.startswith("?"):
            element1, element2 = map(int, query.split()[1:])
            if are_connected(element1, element2):
                print("yes")
            else:
                print("no")
        else:
            element1, element2 = map(int, query.split()[1:])
            union_sets(element1, element2)

if __name__ == '__main__':
    N, Q = map(int, sys.stdin.readline().strip().split())
    process_queries(N, Q)

