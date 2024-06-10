
def read_input():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        edges.append(list(map(int, input().split())))
    return n, m, edges

def get_max_independent_set(n, edges):
    visited = [False] * (n + 1)
    max_independent_set = 0
    for edge in edges:
        if not visited[edge[0]] and not visited[edge[1]]:
            visited[edge[0]] = visited[edge[1]] = True
            max_independent_set += 1
    return max_independent_set

def main():
    n, m, edges = read_input()
    print(get_max_independent_set(n, edges))

if __name__ == '__main__':
    main()

