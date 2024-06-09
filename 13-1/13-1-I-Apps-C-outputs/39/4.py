
def get_min_distance(adil_x, adil_y, bera_x, bera_y, recycling_bin_x, recycling_bin_y, bottles):
    # Calculate the distance from Adil's current position to each bottle
    distances = []
    for bottle in bottles:
        distances.append(((bottle[0] - adil_x) ** 2 + (bottle[1] - adil_y) ** 2) ** 0.5)
    
    # Sort the distances in ascending order
    distances.sort()
    
    # Initialize the minimum distance as the distance from Adil's current position to the closest bottle
    min_distance = distances[0]
    
    # Loop through the distances and calculate the minimum distance by considering both Adil and Bera's paths
    for i in range(1, len(distances)):
        distance = distances[i]
        min_distance = min(min_distance, distance + get_min_distance(adil_x + distance, adil_y, bera_x, bera_y, recycling_bin_x, recycling_bin_y, bottles[i:]))
    
    return min_distance

def main():
    adil_x, adil_y, bera_x, bera_y, recycling_bin_x, recycling_bin_y = map(int, input().split())
    n = int(input())
    bottles = []
    for i in range(n):
        x, y = map(int, input().split())
        bottles.append((x, y))
    print(get_min_distance(adil_x, adil_y, bera_x, bera_y, recycling_bin_x, recycling_bin_y, bottles))

if __name__ == '__main__':
    main()

