
def get_input():
    N, M = map(int, input().split())
    roads = []
    for _ in range(M):
        a, b = map(int, input().split())
        roads.append((a, b))
    return N, M, roads

def count_roads(N, M, roads):
    city_roads = [0] * (N + 1)
    for a, b in roads:
        city_roads[a] += 1
        city_roads[b] += 1
    return city_roads[1:]

def main():
    N, M, roads = get_input()
    city_roads = count_roads(N, M, roads)
    for i in range(1, N + 1):
        print(city_roads[i])

if __name__ == '__main__':
    main()

