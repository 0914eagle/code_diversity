
def get_input():
    N, M = map(int, input().split())
    roads = []
    for _ in range(M):
        a, b = map(int, input().split())
        roads.append((a, b))
    return N, M, roads

def count_roads(N, roads):
    roads_per_city = [0] * (N + 1)
    for a, b in roads:
        roads_per_city[a] += 1
        roads_per_city[b] += 1
    return roads_per_city[1:]

def main():
    N, M, roads = get_input()
    roads_per_city = count_roads(N, roads)
    for i in range(1, N + 1):
        print(roads_per_city[i])

if __name__ == '__main__':
    main()

