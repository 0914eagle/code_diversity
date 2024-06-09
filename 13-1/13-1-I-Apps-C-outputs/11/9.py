
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
    distances_to_most_distant = {}
    for i in range(n):
        distances_to_most_distant[i] = 0

    # Loop through each pair of pebbles that can be jumped between and update the distances from each pebble to the most distant pebble that can be reached
    for i, j in jump_pairs:
        if distances_to_most_distant[i] + 1 > distances_to_most_distant[j]:
            distances_to_most_distant[j] = distances_to_most_distant[i] + 1

    # Find the most distant pebble that can be reached
    most_distant = 0
    for i in range(n):
        if distances_to_most_distant[i] > distances_to_most_distant[most_distant]:
            most_distant = i

    return most_distant

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
    distances_to_most_distant = {}
    for i in range(n):
        distances_to_most_distant[i] = 0

    # Loop through each pair of pebbles that can be jumped between and update the distances from each pebble to the most distant pebble that can be reached
    for i, j in jump_pairs:
        if distances_to_most_distant[i] + 1 > distances_to_most_distant[j]:
            distances_to_most_distant[j] = distances_to_most_distant[i] + 1

    # Find the most distant pebble that can be reached
    most_distant = 0
    for i in range(n):
        if distances_to_most_distant[i] > distances_to_most_distant[most_distant]:
            most_distant = i

    return most_distant

if __name__ == '__main__':
    n = int(input())
    pebbles = list(map(int, input().split()))
    print(f1(n, pebbles))
    print(f2(n, pebbles))

