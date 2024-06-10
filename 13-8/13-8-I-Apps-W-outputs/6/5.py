
def read_input():
    n = int(input())
    vehicles = []
    for i in range(n):
        x, v = map(int, input().split())
        vehicles.append((x, v))
    return n, vehicles

def get_closest_distance(vehicles):
    # Sort the vehicles by their position
    vehicles.sort(key=lambda x: x[0])
    
    # Initialize the closest distance to infinity
    closest_distance = float('inf')
    
    # Iterate over the vehicles and calculate the distance between them
    for i in range(len(vehicles) - 1):
        x1, v1 = vehicles[i]
        x2, v2 = vehicles[i + 1]
        distance = abs(x2 - x1)
        closest_distance = min(closest_distance, distance)
    
    return closest_distance

def get_minimum_range(vehicles, closest_distance):
    # Calculate the minimum range needed to cover all the vehicles
    minimum_range = 0
    for x, v in vehicles:
        minimum_range = max(minimum_range, abs(x) + closest_distance)
    
    return minimum_range

def main():
    n, vehicles = read_input()
    closest_distance = get_closest_distance(vehicles)
    minimum_range = get_minimum_range(vehicles, closest_distance)
    print(minimum_range)

if __name__ == '__main__':
    main()

