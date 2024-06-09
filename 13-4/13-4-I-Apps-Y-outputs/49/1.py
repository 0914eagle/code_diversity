
def get_input():
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        a, b = map(int, input().split())
        roads.append((a, b))
    return n, m, roads

def count_roads(n, roads):
    city_roads = [0] * (n + 1)
    for a, b in roads:
        city_roads[a] += 1
        city_roads[b] += 1
    return city_roads[1:]

def main():
    n, m, roads = get_input()
    city_roads = count_roads(n, roads)
    for i in range(1, n + 1):
        print(city_roads[i])

if __name__ == '__main__':
    main()

