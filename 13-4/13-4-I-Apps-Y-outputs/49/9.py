
def get_road_counts(n, m, roads):
    # Initialize a dictionary to store the number of roads connected to each city
    road_counts = {}
    for i in range(1, n + 1):
        road_counts[i] = 0

    # Iterate through the roads and increment the count for each city
    for road in roads:
        city1, city2 = road
        road_counts[city1] += 1
        road_counts[city2] += 1

    return road_counts

def main():
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        roads.append(tuple(map(int, input().split())))
    road_counts = get_road_counts(n, m, roads)
    for city, count in road_counts.items():
        print(count)

if __name__ == '__main__':
    main()

