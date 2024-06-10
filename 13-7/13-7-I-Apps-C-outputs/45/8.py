
def read_input():
    N = int(input())
    cities = []
    for i in range(N):
        y, d, r = map(int, input().split())
        cities.append((y, d, r))
    return N, cities

def find_shortest_path(start, cities):
    visited = [False] * len(cities)
    queue = [(0, start)]
    while queue:
        time, city = queue.pop(0)
        if visited[city]:
            continue
        visited[city] = True
        for next_city, y, d, r in cities:
            if visited[next_city]:
                continue
            if abs(y - cities[next_city][0]) >= d:
                queue.append((time + r + abs(y - cities[next_city][0]), next_city))
    return visited

def solve(N, cities):
    visited = find_shortest_path(0, cities)
    return [visited[i+1] * (cities[i+1][1] + cities[i+1][2]) for i in range(N-1)]

if __name__ == '__main__':
    N, cities = read_input()
    print(*solve(N, cities), sep='\n')

