
def find_min_distance(n, k, rooms):
    # Initialize the minimum distance to a large value
    min_distance = float('inf')
    # Iterate over the possible starting positions of Farmer John's room
    for i in range(n - k):
        # Initialize the distance to 0
        distance = 0
        # Iterate over the k cows
        for j in range(k):
            # Calculate the distance between the current room and the next cow's room
            distance += rooms[i + j + 1] - rooms[i + j]
        # Update the minimum distance if necessary
        min_distance = min(min_distance, distance)
    # Return the minimum distance
    return min_distance

def main():
    n, k = map(int, input().split())
    rooms = list(map(int, input()))
    print(find_min_distance(n, k, rooms))

if __name__ == '__main__':
    main()

