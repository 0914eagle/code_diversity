
def is_tourist_friendly(n, roads):
    visited = [False] * n
    tour = []
    for city in range(n):
        if not visited[city]:
            stack = [city]
            while stack:
                current = stack.pop()
                visited[current] = True
                for neighbor in roads[current]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
            tour.append(current)
    return tour == list(range(n))

def solve(n, m, roads):
    if len(roads) == 0:
        return "YES"
    for city in range(n):
        for neighbor in roads[city]:
            if city < neighbor:
                roads[city].remove(neighbor)
                roads[neighbor].remove(city)
                if is_tourist_friendly(n, roads):
                    return "YES"
                roads[city].append(neighbor)
                roads[neighbor].append(city)
    return "NO"

