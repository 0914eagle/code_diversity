
def get_adjacent_islands(n, bridge):
    adjacent_islands = []
    for i in range(n):
        for j in range(i+1, n):
            if bridge[i][j] == 1:
                adjacent_islands.append((i, j))
    return adjacent_islands

def can_rearrange_statues(n, a, b):
    bridge = [[0] * n for _ in range(n)]
    for i in range(n-1):
        bridge[i][i+1] = 1
        bridge[i+1][i] = 1
    bridge[n-1][0] = 1
    bridge[0][n-1] = 1

    adjacent_islands = get_adjacent_islands(n, bridge)

    visited = [False] * n
    visited[0] = True
    queue = [0]

    while queue:
        curr_island = queue.pop(0)
        for island in adjacent_islands:
            if island[0] == curr_island and not visited[island[1]]:
                queue.append(island[1])
                visited[island[1]] = True

    for i in range(n):
        if visited[i] and a[i] != b[i]:
            return False
    return True

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print("YES") if can_rearrange_statues(n, a, b) else print("NO")

if __name__ == '__main__':
    main()

