
def get_shortest_distance(distances, s, t):
    n = len(distances)
    if s == t:
        return 0
    if s > t:
        s, t = t, s
    dist = [float('inf') for _ in range(n)]
    dist[s] = 0
    for i in range(n):
        for j in range(n):
            dist[j] = min(dist[j], dist[i] + distances[i][j])
    return dist[t]

def main():
    n = int(input())
    distances = []
    for i in range(n):
        distances.append([int(x) for x in input().split()])
    s, t = map(int, input().split())
    print(get_shortest_distance(distances, s, t))

if __name__ == '__main__':
    main()

