
def f1(n, pebbles):
    # f1 should return the most distant pebble that can be reached by a sequence of jumps
    # according to the given rules
    
    # Initialize a dictionary to store the number of spots on each pebble
    pebble_spots = {}
    for i in range(n):
        pebble_spots[i] = pebbles[i]
    
    # Initialize a list to store the distances between each pair of pebbles
    distances = []
    for i in range(n-1):
        for j in range(i+1, n):
            distances.append(j-i)
    
    # Initialize a list to store the pairs of pebbles that can be jumped between
    jump_pairs = []
    for i in range(n-1):
        for j in range(i+1, n):
            if pebble_spots[i] + pebble_spots[j] == distances[j-i-1]:
                jump_pairs.append((i, j))
    
    # Initialize a list to store the distances from the first pebble to each pebble that can be reached by a sequence of jumps
    distances_from_first = [0] * n
    distances_from_first[0] = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if (i, j) in jump_pairs:
                distances_from_first[j] = max(distances_from_first[i] + 1, distances_from_first[j])
    
    # Return the most distant pebble that can be reached by a sequence of jumps
    return max(distances_from_first)

def f2(n, pebbles):
    # f2 should return the number of pebbles that can be reached by a sequence of jumps
    # according to the given rules
    
    # Initialize a dictionary to store the number of spots on each pebble
    pebble_spots = {}
    for i in range(n):
        pebble_spots[i] = pebbles[i]
    
    # Initialize a list to store the distances between each pair of pebbles
    distances = []
    for i in range(n-1):
        for j in range(i+1, n):
            distances.append(j-i)
    
    # Initialize a list to store the pairs of pebbles that can be jumped between
    jump_pairs = []
    for i in range(n-1):
        for j in range(i+1, n):
            if pebble_spots[i] + pebble_spots[j] == distances[j-i-1]:
                jump_pairs.append((i, j))
    
    # Initialize a list to store the distances from the first pebble to each pebble that can be reached by a sequence of jumps
    distances_from_first = [0] * n
    distances_from_first[0] = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if (i, j) in jump_pairs:
                distances_from_first[j] = max(distances_from_first[i] + 1, distances_from_first[j])
    
    # Return the number of pebbles that can be reached by a sequence of jumps
    return sum(1 for i in range(n) if distances_from_first[i] > 0)

if __name__ == '__main__':
    n = int(input())
    pebbles = list(map(int, input().split()))
    print(f1(n, pebbles))
    print(f2(n, pebbles))

