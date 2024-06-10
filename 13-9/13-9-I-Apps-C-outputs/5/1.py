
def find_max_reachable_vertices():
    # Implement this function to find the plan which maximizes the number of reachable vertices
    return ...

def find_min_reachable_vertices():
    # Implement this function to find the plan which minimizes the number of reachable vertices
    return ...

if __name__ == '__main__':
    n, m, s = map(int, input().split())
    edges = []
    for i in range(m):
        t, u, v = map(int, input().split())
        edges.append((t, u, v))
    print(find_max_reachable_vertices())
    print(find_min_reachable_vertices())

