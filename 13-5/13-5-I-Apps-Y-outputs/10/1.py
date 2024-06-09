
def get_edges(n):
    edges = []
    for i in range(n - 1):
        a, b = map(int, input().split())
        edges.append((a, b))
    return edges

def get_paths(edges, a, b, c):
    paths = []
    for edge in edges:
        if edge[0] == a and edge[1] == b:
            paths.append(edge)
        elif edge[0] == b and edge[1] == c:
            paths.append(edge)
        elif edge[0] == a and edge[1] == c:
            paths.append(edge)
    return paths

def get_max_edges(edges, a, b, c):
    paths = get_paths(edges, a, b, c)
    max_edges = len(set(paths))
    return max_edges

def get_best_answer(edges):
    n = len(edges) + 1
    max_edges = 0
    best_answer = []
    for a in range(1, n):
        for b in range(1, n):
            if a == b:
                continue
            for c in range(1, n):
                if a == c or b == c:
                    continue
                edges_count = get_max_edges(edges, a, b, c)
                if edges_count > max_edges:
                    max_edges = edges_count
                    best_answer = [a, b, c]
    return best_answer

def main():
    n = int(input())
    edges = get_edges(n)
    best_answer = get_best_answer(edges)
    print(max_edges)
    print(" ".join(map(str, best_answer)))

if __name__ == '__main__':
    main()

