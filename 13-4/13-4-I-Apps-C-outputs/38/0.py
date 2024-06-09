
def f1(n, spots):
    # Initialize a list to store the distances between pebbles
    distances = [0] * (n + 1)
    # Initialize a list to store the pairs of pebbles that can be jumped between
    pairs = []
    # Iterate over the input list of spots
    for i in range(n):
        # Get the number of spots on the current pebble
        num_spots = spots[i]
        # Iterate over the previous pebbles
        for j in range(i):
            # Get the number of spots on the previous pebble
            prev_num_spots = spots[j]
            # If the sum of the number of spots is equal to the distance between the pebbles, add the pair to the list of pairs
            if num_spots + prev_num_spots == i - j:
                pairs.append((j, i))
    # Initialize a variable to store the maximum distance
    max_distance = 0
    # Iterate over the pairs of pebbles
    for pair in pairs:
        # Get the distance between the two pebbles
        distance = pair[1] - pair[0]
        # If the distance is greater than the maximum distance, update the maximum distance
        if distance > max_distance:
            max_distance = distance
    # Return the maximum distance
    return max_distance

def f2(n, spots):
    # Initialize a list to store the distances between pebbles
    distances = [0] * (n + 1)
    # Initialize a list to store the pairs of pebbles that can be jumped between
    pairs = []
    # Iterate over the input list of spots
    for i in range(n):
        # Get the number of spots on the current pebble
        num_spots = spots[i]
        # Iterate over the previous pebbles
        for j in range(i):
            # Get the number of spots on the previous pebble
            prev_num_spots = spots[j]
            # If the sum of the number of spots is equal to the distance between the pebbles, add the pair to the list of pairs
            if num_spots + prev_num_spots == i - j:
                pairs.append((j, i))
    # Initialize a variable to store the maximum distance
    max_distance = 0
    # Iterate over the pairs of pebbles
    for pair in pairs:
        # Get the distance between the two pebbles
        distance = pair[1] - pair[0]
        # If the distance is greater than the maximum distance, update the maximum distance
        if distance > max_distance:
            max_distance = distance
    # Return the maximum distance
    return max_distance

if __name__ == '__main__':
    n = int(input())
    spots = list(map(int, input().split()))
    print(f1(n, spots))

