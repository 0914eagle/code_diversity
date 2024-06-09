
def f1(n, spots):
    # Initialize a list to store the distances between pebbles
    distances = [0] * (n + 1)
    # Initialize a list to store the number of spots on each pebble
    num_spots = [0] * (n + 1)
    
    # Populate the list of distances and number of spots on each pebble
    for i in range(1, n + 1):
        distances[i] = i
        num_spots[i] = spots[i - 1]
    
    # Loop through each pebble and check if it can be reached from the previous pebble
    for i in range(2, n + 1):
        for j in range(1, i):
            # If the sum of the number of spots on the current pebble and the previous pebble is equal to the distance between them, update the distance of the current pebble
            if num_spots[i] + num_spots[j] == distances[i] - distances[j]:
                distances[i] = min(distances[i], distances[j] + 1)
    
    # Return the maximum distance
    return max(distances)

def f2(n, spots):
    # Initialize a list to store the distances between pebbles
    distances = [0] * (n + 1)
    # Initialize a list to store the number of spots on each pebble
    num_spots = [0] * (n + 1)
    
    # Populate the list of distances and number of spots on each pebble
    for i in range(1, n + 1):
        distances[i] = i
        num_spots[i] = spots[i - 1]
    
    # Loop through each pebble and check if it can be reached from the previous pebble
    for i in range(2, n + 1):
        for j in range(1, i):
            # If the sum of the number of spots on the current pebble and the previous pebble is equal to the distance between them, update the distance of the current pebble
            if num_spots[i] + num_spots[j] == distances[i] - distances[j]:
                distances[i] = min(distances[i], distances[j] + 1)
    
    # Return the maximum distance
    return max(distances)

if __name__ == '__main__':
    n = int(input())
    spots = list(map(int, input().split()))
    print(f1(n, spots))
    print(f2(n, spots))

