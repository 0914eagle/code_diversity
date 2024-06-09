
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
            # If the sum of the number of spots on the current and previous pebbles is equal to the distance between them, add the pair to the list of pairs
            if num_spots + prev_num_spots == i - j:
                pairs.append((j, i))
        # If the current pebble has no spots, set its distance to 0
        if num_spots == 0:
            distances[i] = 0
        # Otherwise, set its distance to the maximum distance of the previous pebbles plus 1
        else:
            distances[i] = max(distances[j] for j in range(i)) + 1
    # Initialize the most distant pebble to the first pebble
    most_distant_pebble = 0
    # Iterate over the pairs of pebbles
    for j, i in pairs:
        # If the distance of the current pebble is greater than the distance of the most distant pebble, update the most distant pebble
        if distances[i] > distances[most_distant_pebble]:
            most_distant_pebble = i
    # Return the distance of the most distant pebble
    return distances[most_distant_pebble]

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
            # If the sum of the number of spots on the current and previous pebbles is equal to the distance between them, add the pair to the list of pairs
            if num_spots + prev_num_spots == i - j:
                pairs.append((j, i))
        # If the current pebble has no spots, set its distance to 0
        if num_spots == 0:
            distances[i] = 0
        # Otherwise, set its distance to the maximum distance of the previous pebbles plus 1
        else:
            distances[i] = max(distances[j] for j in range(i)) + 1
    # Initialize the most distant pebble to the first pebble
    most_distant_pebble = 0
    # Iterate over the pairs of pebbles
    for j, i in pairs:
        # If the distance of the current pebble is greater than the distance of the most distant pebble, update the most distant pebble
        if distances[i] > distances[most_distant_pebble]:
            most_distant_pebble = i
    # Return the distance of the most distant pebble
    return distances[most_distant_pebble]

if __name__ == '__main__':
    n = int(input())
    spots = list(map(int, input().split()))
    print(f1(n, spots))
    print(f2(n, spots))

