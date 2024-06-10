
def get_lifelines(edges):
    lifelines = set()
    for edge in edges:
        lifelines.add(frozenset(edge))
    return len(lifelines)

def count_lifelines(n, edges):
    vertices = set(range(1, n + 1))
    for edge in edges:
        if len(edge) != 2:
            return 0
        if edge[0] not in vertices or edge[1] not in vertices:
            return 0
        vertices.remove(edge[0])
        vertices.remove(edge[1])
    return get_lifelines(edges)

if __name__ == '__main__':
    n = int(input())
    edges = []
    for _ in range(n - 1):
        edges.append(tuple(map(int, input().split())))
    print(count_lifelines(n, edges))

