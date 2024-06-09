
def f1(n, spots):
    # Initialize a list to store the distances of the pebbles
    distances = [0] * (n + 1)
    # Initialize a list to store the previous pebble for each pebble
    previous = [0] * (n + 1)
    # Initialize the maximum distance as 0
    max_distance = 0
    # Loop through each pebble
    for i in range(1, n + 1):
        # Loop through each pebble again
        for j in range(1, n + 1):
            # Check if the sum of the spots on the current pebble and the previous pebble is equal to the distance between them
            if spots[i - 1] + spots[j - 1] == i - j:
                # If the distance between the current pebble and the previous pebble is greater than the current maximum distance, update the maximum distance
                if distances[j] + 1 > max_distance:
                    max_distance = distances[j] + 1
                # Update the distance and previous pebble for the current pebble
                distances[i] = max_distance
                previous[i] = j
    # Return the maximum distance
    return max_distance

def f2(n, spots):
    # Initialize a list to store the distances of the pebbles
    distances = [0] * (n + 1)
    # Initialize a list to store the previous pebble for each pebble
    previous = [0] * (n + 1)
    # Initialize the maximum distance as 0
    max_distance = 0
    # Loop through each pebble
    for i in range(1, n + 1):
        # Loop through each pebble again
        for j in range(1, n + 1):
            # Check if the sum of the spots on the current pebble and the previous pebble is equal to the distance between them
            if spots[i - 1] + spots[j - 1] == i - j:
                # If the distance between the current pebble and the previous pebble is greater than the current maximum distance, update the maximum distance
                if distances[j] + 1 > max_distance:
                    max_distance = distances[j] + 1
                # Update the distance and previous pebble for the current pebble
                distances[i] = max_distance
                previous[i] = j
    # Return the maximum distance
    return max_distance

if __name__ == '__main__':
    n = int(input())
    spots = list(map(int, input().split()))
    print(f1(n, spots))
    print(f2(n, spots))

