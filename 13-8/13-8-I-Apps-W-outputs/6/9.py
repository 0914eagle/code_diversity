
import math

def get_closest_distance(vehicles):
    # Sort the vehicles by their position
    vehicles.sort(key=lambda x: x[0])
    
    # Initialize the minimum distance as the distance between the first two vehicles
    min_distance = abs(vehicles[1][0] - vehicles[0][0])
    
    # Loop through the vehicles and calculate the distance between each pair of vehicles
    for i in range(len(vehicles) - 1):
        distance = abs(vehicles[i + 1][0] - vehicles[i][0])
        min_distance = min(min_distance, distance)
    
    return min_distance

def get_vehicle_positions(n):
    positions = []
    for i in range(n):
        x, v = map(int, input().split())
        positions.append((x, v))
    return positions

def main():
    n = int(input())
    positions = get_vehicle_positions(n)
    min_distance = get_closest_distance(positions)
    print(min_distance)

if __name__ == '__main__':
    main()

