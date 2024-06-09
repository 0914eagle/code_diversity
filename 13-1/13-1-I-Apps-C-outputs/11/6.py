
def f1(n, pebbles):
    # Initialize a dictionary to store the number of spots on each pebble
    pebble_spots = {}
    for i in range(n):
        pebble_spots[i] = pebbles[i]

    # Initialize a list to store the distances between each pair of pebbles
    distances = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            distances.append(abs(i - j))

    # Initialize a list to store the pairs of pebbles that can be jumped between
    jump_pairs = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            if pebble_spots[i] + pebble_spots[j] in distances:
                jump_pairs.append((i, j))

    # Initialize a dictionary to store the distances from each pebble to the most distant pebble that can be reached
    distances_from_pebble = {}
    for i in range(n):
        distances_from_pebble[i] = 0

    # Loop through the pairs of pebbles that can be jumped between and update the distances from each pebble to the most distant pebble that can be reached
    for i, j in jump_pairs:
        if distances_from_pebble[i] + 1 > distances_from_pebble[j]:
            distances_from_pebble[j] = distances_from_pebble[i] + 1

    # Find the most distant pebble that can be reached
    max_distance = 0
    most_distant_pebble = 0
    for i in range(n):
        if distances_from_pebble[i] > max_distance:
            max_distance = distances_from_pebble[i]
            most_distant_pebble = i

    return max_distance

def f2(n, pebbles):
    # Initialize a list to store the distances between each pair of pebbles
    distances = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            distances.append(abs(i - j))

    # Initialize a list to store the pairs of pebbles that can be jumped between
    jump_pairs = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            if pebbles[i] + pebbles[j] in distances:
                jump_pairs.append((i, j))

    # Initialize a dictionary to store the distances from each pebble to the most distant pebble that can be reached
    distances_from_pebble = {}
    for i in range(n):
        distances_from_pebble[i] = 0

    # Loop through the pairs of pebbles that can be jumped between and update the distances from each pebble to the most distant pebble that can be reached
    for i, j in jump_pairs:
        if distances_from_pebble[i] + 1 > distances_from_pebble[j]:
            distances_from_pebble[j] = distances_from_pebble[i] + 1

    # Find the most distant pebble that can be reached
    max_distance = 0
    most_distant_pebble = 0
    for i in range(n):
        if distances_from_pebble[i] > max_distance:
            max_distance = distances_from_pebble[i]
            most_distant_pebble = i

    return max_distance

if __name__ == '__main__':
    n = int(input())
    pebbles = list(map(int, input().split()))
    print(f1(n, pebbles))
    print(f2(n, pebbles))

