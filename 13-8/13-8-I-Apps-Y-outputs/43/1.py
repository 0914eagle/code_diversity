
def get_input():
    N, M = map(int, input().split())
    heights = list(map(int, input().split()))
    roads = []
    for _ in range(M):
        a, b = map(int, input().split())
        roads.append((a, b))
    return N, M, heights, roads

def get_good_observatories(N, M, heights, roads):
    visited = [False] * (N + 1)
    good_observatories = 0
    for i in range(1, N + 1):
        if not visited[i]:
            queue = [i]
            visited[i] = True
            while queue:
                current = queue.pop(0)
                for road in roads:
                    if road[0] == current or road[1] == current:
                        other = road[0] if road[1] == current else road[1]
                        if not visited[other] and heights[current] <= heights[other]:
                            queue.append(other)
                            visited[other] = True
            if not visited[i]:
                good_observatories += 1
    return good_observatories

def main():
    N, M, heights, roads = get_input()
    print(get_good_observatories(N, M, heights, roads))

if __name__ == '__main__':
    main()

