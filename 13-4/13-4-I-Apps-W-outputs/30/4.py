
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
    # Check if the road network is already tourist-friendly
    if is_tourist_friendly(cities, roads):
        return "YES"
    
    # If not, try to redirect some of the roads to make it tourist-friendly
    for i in range(len(roads)):
        road = roads[i]
        if road[0] != road[1]:
            roads[i] = (road[1], road[0])
            if is_tourist_friendly(cities, roads):
                return "YES"
            roads[i] = road
    
    # If no redirection works, return "NO"
    return "NO"

