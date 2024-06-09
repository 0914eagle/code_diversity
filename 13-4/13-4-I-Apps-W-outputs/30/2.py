
def is_tourist_friendly(n, roads):
    visited = [False] * n
    stack = [0]
    while stack:
        city = stack.pop()
        if visited[city]:
            continue
        visited[city] = True
        for road in roads:
            if road[0] == city:
                stack.append(road[1])
                break
    return all(visited)

def solve(n, roads):
    if len(roads) == 0:
        return "NO"
    for i in range(len(roads)):
        for j in range(i+1, len(roads)):
            if roads[i][0] == roads[j][1] and roads[i][1] == roads[j][0]:
                roads[i][0], roads[i][1] = roads[j][1], roads[j][0]
                break
        if is_tourist_friendly(n, roads):
            return "YES\n" + "\n".join([" ".join(map(str, road)) for road in roads])
    return "NO"

