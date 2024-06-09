
def f1(n, pebbles):
    # Initialize a dictionary to store the pairs of pebbles that can be jumped between
    jump_pairs = {}
    for i in range(n - 1):
        for j in range(i + 1, n):
            if pebbles[i] + pebbles[j] == j - i:
                jump_pairs[i, j] = True
    
    # Initialize a list to store the distances of the pebbles that can be reached
    reachable_distances = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            if jump_pairs.get((i, j - 1), False):
                reachable_distances.append(j)
    
    # Return the maximum distance
    return max(reachable_distances)

def f2(n, pebbles):
    # Initialize a dictionary to store the pairs of pebbles that can be jumped between
    jump_pairs = {}
    for i in range(n - 1):
        for j in range(i + 1, n):
            if pebbles[i] + pebbles[j] == j - i:
                jump_pairs[i, j] = True
    
    # Initialize a list to store the distances of the pebbles that can be reached
    reachable_distances = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            if jump_pairs.get((i, j - 1), False):
                reachable_distances.append(j)
    
    # Return the maximum distance
    return max(reachable_distances)

if __name__ == '__main__':
    n = int(input())
    pebbles = list(map(int, input().split()))
    print(f1(n, pebbles))
    print(f2(n, pebbles))

