
def read_input():
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        a, b, d = map(int, input().split())
        roads.append((a, b, d))
    return n, m, roads

def get_shortest_path(roads, start, end):
    visited = set()
    queue = [(0, start)]
    while queue:
        dist, curr = queue.pop(0)
        if curr == end:
            return dist
        if curr in visited:
            continue
        visited.add(curr)
        for road in roads:
            if road[0] == curr or road[1] == curr:
                queue.append((dist + road[2], road[0] if road[1] == curr else road[1]))
    return -1

def solve(n, m, roads):
    shortest_paths = []
    for i in range(n):
        shortest_paths.append(get_shortest_path(roads, i, 1))
    if -1 in shortest_paths:
        return "impossible"
    shortest_path = min(shortest_paths)
    path = []
    curr = 0
    for i in range(n):
        if shortest_paths[i] == shortest_path:
            path.append(i)
            curr = i
            break
    while curr != 1:
        for road in roads:
            if road[0] == curr or road[1] == curr:
                curr = road[0] if road[1] == curr else road[1]
                path.append(curr)
                break
    return len(path), *path

def main():
    n, m, roads = read_input()
    print(solve(n, m, roads))

if __name__ == '__main__':
    main()

