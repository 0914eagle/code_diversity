
import sys

def get_input():
    n, m = map(int, input().split())
    corridors = []
    for _ in range(m):
        u, v = map(int, input().split())
        corridors.append((u, v))
    return n, m, corridors

def remove_corridors(n, m, corridors):
    visited = [False] * (n + 1)
    stack = []
    removed = 0
    for u, v in corridors:
        if visited[u] and visited[v]:
            continue
        stack.append((u, v))
        while stack:
            u, v = stack.pop()
            if visited[u] and visited[v]:
                continue
            visited[u] = True
            visited[v] = True
            removed += 1
            if removed > m // 2:
                break
    return removed

def main():
    n, m, corridors = get_input()
    print(remove_corridors(n, m, corridors))

if __name__ == '__main__':
    main()

