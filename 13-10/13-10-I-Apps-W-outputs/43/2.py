
def get_ancestors(parent, n):
    ancestors = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        if parent[i] != -1:
            ancestors[i].append(parent[i])
            ancestors[i].extend(ancestors[parent[i]])
    return ancestors

def get_non_respecting_vertices(c, ancestors):
    non_respecting_vertices = []
    for i in range(1, len(c)):
        if c[i] == 1 and all(ancestor not in non_respecting_vertices for ancestor in ancestors[i]):
            non_respecting_vertices.append(i)
    return non_respecting_vertices

def get_deletion_order(parent, c):
    n = len(parent) - 1
    ancestors = get_ancestors(parent, n)
    non_respecting_vertices = get_non_respecting_vertices(c, ancestors)
    if not non_respecting_vertices:
        return -1
    deletion_order = []
    while non_respecting_vertices:
        vertex = min(non_respecting_vertices)
        deletion_order.append(vertex)
        non_respecting_vertices.remove(vertex)
        for child in range(1, n+1):
            if parent[child] == vertex:
                parent[child] = parent[vertex]
                non_respecting_vertices.append(child)
    return deletion_order

def main():
    n = int(input())
    parent = [-1]
    c = [0]
    for i in range(n):
        parent.append(int(input()))
        c.append(int(input()))
    print(get_deletion_order(parent, c))

if __name__ == '__main__':
    main()

