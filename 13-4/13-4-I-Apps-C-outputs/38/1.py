
def f1(n, pebbles):
    # f1 should return the most distant pebble that can be reached by a sequence of jumps
    # according to the given rules and starting from the first pebble
    
    # Initialize a dictionary to store the number of spots on each pebble
    pebble_spots = {}
    for i in range(n):
        pebble_spots[i] = pebbles[i]
    
    # Initialize a set to store the pairs of pebbles that can be jumped between
    jump_pairs = set()
    
    # Iterate through the pebbles and find the pairs of pebbles that can be jumped between
    for i in range(n-1):
        for j in range(i+1, n):
            if pebble_spots[i] + pebble_spots[j] == j-i:
                jump_pairs.add((i, j))
    
    # Initialize a variable to store the most distant pebble that can be reached
    max_dist = 0
    
    # Iterate through the pairs of pebbles and find the pair that can be jumped between to reach the most distant pebble
    for i, j in jump_pairs:
        if j-i > max_dist:
            max_dist = j-i
    
    # Return the most distant pebble that can be reached
    return max_dist

def f2(n, pebbles):
    # f2 should return the number of spots on the most distant pebble that can be reached by a sequence of jumps
    # according to the given rules and starting from the first pebble
    
    # Initialize a dictionary to store the number of spots on each pebble
    pebble_spots = {}
    for i in range(n):
        pebble_spots[i] = pebbles[i]
    
    # Initialize a set to store the pairs of pebbles that can be jumped between
    jump_pairs = set()
    
    # Iterate through the pebbles and find the pairs of pebbles that can be jumped between
    for i in range(n-1):
        for j in range(i+1, n):
            if pebble_spots[i] + pebble_spots[j] == j-i:
                jump_pairs.add((i, j))
    
    # Initialize a variable to store the most distant pebble that can be reached
    max_dist = 0
    
    # Iterate through the pairs of pebbles and find the pair that can be jumped between to reach the most distant pebble
    for i, j in jump_pairs:
        if j-i > max_dist:
            max_dist = j-i
    
    # Return the number of spots on the most distant pebble that can be reached
    return pebble_spots[max_dist]

if __name__ == '__main__':
    n = int(input())
    pebbles = list(map(int, input().split()))
    print(f1(n, pebbles))
    print(f2(n, pebbles))

