
def is_tourist_friendly(cities, roads):
    # Check if the road network is tourist-friendly
    for city in cities:
        visited = set()
        queue = [city]
        while queue:
            current = queue.pop(0)
            if current not in visited:
                visited.add(current)
                for road in roads:
                    if road[0] == current:
                        queue.append(road[1])
            if len(visited) == len(cities):
                return True
    return False

def solve(cities, roads):
    # Redirect some of the roads to make the road network tourist-friendly
    for road in roads:
        if not is_tourist_friendly(cities, roads):
            road.reverse()
    if is_tourist_friendly(cities, roads):
        return "YES\n" + "\n".join([" ".join(map(str, road)) for road in roads])
    else:
        return "NO"

