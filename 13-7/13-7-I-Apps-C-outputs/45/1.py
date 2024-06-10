
def read_input():
    N = int(input())
    cities = []
    for i in range(N):
        y, d, r = map(int, input().split())
        cities.append((y, d, r))
    return N, cities

def find_shortest_path(start, cities):
    visited = set([start])
    queue = [(0, start)]
    while queue:
        time, city = heapq.heappop(queue)
        if city == N:
            return time
        for next_city, next_time in cities[city-1]:
            if next_city not in visited:
                visited.add(next_city)
                heapq.heappush(queue, (time+next_time, next_city))
    return -1

def solve(cities):
    N = len(cities)
    return [find_shortest_path(1, cities) for i in range(N)]

def main():
    N, cities = read_input()
    print(*solve(cities), sep='\n')

if __name__ == '__main__':
    main()

