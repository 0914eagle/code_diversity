
def get_road_counts(cities, roads):
    road_counts = [0] * cities
    for road in roads:
        city1, city2 = road
        road_counts[city1-1] += 1
        road_counts[city2-1] += 1
    return road_counts

