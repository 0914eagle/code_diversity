
def read_input():
    n, m = map(int, input().split())
    corridors = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        corridors[u].append(v)
    return n, m, corridors

def remove_corridors(n, m, corridors):
    visited = [False] * (n + 1)
    stack = [1]
    removed = 0
    while stack:
        current = stack.pop()
        if visited[current]:
            continue
        visited[current] = True
        for neighbor in corridors[current]:
            if not visited[neighbor]:
                stack.append(neighbor)
        if removed < m // 2:
            removed += 1
            corridors[current] = []
    return removed, corridors

def write_output(removed, corridors):
    print(removed)
    for i in range(1, len(corridors)):
        for j in corridors[i]:
            print(i, j)

if __name__ == '__main__':
    n, m, corridors = read_input()
    removed, corridors = remove_corridors(n, m, corridors)
    write_output(removed, corridors)

